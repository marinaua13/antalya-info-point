from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from catalog.forms import AuthorsForm, UserRegistrationForm, CommentariesForm
from catalog.models import Author, Offer, Service


@login_required
def index(request: HttpRequest) -> HttpResponse:
    num_authors = Author.objects.count()
    num_offers = Offer.objects.count()
    num_services = Service.objects.count()

    context = {
        "num_authors": num_authors,
        "num_offers": num_offers,
        "num_services": num_services,
    }
    return render(request, "catalog/index.html", context=context)


class ServiceListView(LoginRequiredMixin, generic.ListView):
    model = Service
    template_name = "catalog/service_list.html"
    queryset = Service.objects.all()
    paginate_by = 2


class ServiceDetailView(generic.DetailView):
    model = Service
    template_name = "catalog/service_detail.html"
    queryset = Service.objects.all()


class ServiceOfferListView(generic.ListView):
    model = Service
    template_name = "catalog/service_offers_list.html"
    context_object_name = "offers"

    def get_queryset(self):
        service_id = self.kwargs["service_id"]
        service = get_object_or_404(Service, pk=service_id)
        return service.offers.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["service"] = get_object_or_404(Service, pk=self.kwargs["service_id"])
        return context


class AuthorListView(generic.ListView):
    model = Author
    template_name = "catalog/author_list.html"

    # context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Отримання списку авторів, які мають пропозиції
        context["authors_with_offers"] = Author.objects.filter(
            offers__isnull=False
        ).distinct()
        return context


class OfferListView(generic.ListView):
    model = Offer
    template_name = "catalog/offer_list.html"
    queryset = Offer.objects.all()
    paginate_by = 4


class OfferDetailView(generic.DetailView):
    model = Offer
    template_name = "catalog/offer_detail.html"
    context_object_name = "offer"


class ServiceCreateView(LoginRequiredMixin, generic.CreateView):
    model = Service
    fields = "__all__"
    success_url = reverse_lazy("catalog:service-list")


class OfferCreateList(LoginRequiredMixin, generic.CreateView):
    model = Offer
    fields = "__all__"
    success_url = reverse_lazy("catalog:offer-list")


class AuthorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Author
    form_class = AuthorsForm
    template_name = "catalog/author_form.html"
    success_url = reverse_lazy("catalog:author-list")

    def form_valid(self, form):
        return super().form_valid(form)


class AuthorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Author
    fields = (
        "username",
        "first_name",
        "last_name",
        "email",
    )
    success_url = reverse_lazy("catalog:author-list")


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = "catalog/author_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.object
        # Отримання пропозицій (offers) автора
        offers = Offer.objects.filter(posted_by=author)
        context["offers"] = offers
        return context


def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            author = form.save()
            login(request, author)
            return redirect("/")

        else:
            for error in list(form.errors.values()):
                print(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name="registration/register.html",
        context={"form": form},
    )


def search_offer(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        offers = Offer.objects.filter(name__icontains=searched)
        return render(
            request,
            "catalog/offer_search.html",
            {"searched": searched, "offers": offers},
        )
    else:
        return render(request, "catalog/offer_search.html", {})


def info(request):
    return render(
        request,
        "includes/info_general.html ",
    )


class AddCommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Offer
    template_name = "catalog/comment_create.html"
    form_class = CommentariesForm
    success_url = reverse_lazy("catalog:offer-detail", kwargs={"pk": 1})

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.offer = get_object_or_404(Offer, pk=self.kwargs["pk"])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        offers = self.get_object()
        context["user_offers"] = offers
        return context
