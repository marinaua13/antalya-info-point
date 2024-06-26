from catalog import views
from django.urls import path

from catalog.views import (
    IndexView,
    ServiceListView,
    AuthorListView,
    OfferListView,
    OfferDetailView,
    ServiceCreateView,
    OfferCreateList,
    AuthorCreateView,
    AuthorDetailView,
    ServiceDetailView,
    ServiceOfferListView,
    AddCommentCreateView,
    AuthorUpdateView,
    CommentaryDeleteView,
    CommentaryUpdateView,
    CommentaryDetailView,
    InfoView,
    CarsView,
    InsuranceView,
    HospitalView,
    CustomView,
    CanyonsView,
    SpringsView,
    BeachesView,
    HammamView,
    SearchOfferView,
    RegisterView,

)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("service/", ServiceListView.as_view(), name="service-list"),
    path("service/create/", ServiceCreateView.as_view(), name="service-create"),
    path("service/<int:pk>/", ServiceDetailView.as_view(), name="service-detail"),
    path(
        "service/<int:service_id>/offer/",
        ServiceOfferListView.as_view(),
        name="service-offer-list",
    ),
    path("author/", AuthorListView.as_view(), name="author-list"),
    path("author/create/", AuthorCreateView.as_view(), name="author_create"),
    path("author/<int:pk>/update", AuthorUpdateView.as_view(), name="author-update"),
    path("author/<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),
    path("offer/", OfferListView.as_view(), name="offer-list"),
    path("offer/<int:pk>/", OfferDetailView.as_view(), name="offer-detail"),
    path("offer/create/", OfferCreateList.as_view(), name="offer-create"),
    path(
        "offer/<int:pk>/commentary/",
        AddCommentCreateView.as_view(),
        name="offer-comment-create",
    ),
    path(
        "commentary/<int:pk>/delete/",
        CommentaryDeleteView.as_view(),
        name="commentary-delete",
    ),
    path("commentary/<int:pk>/", CommentaryDetailView.as_view(), name="comment-detail"),
    path(
        "commentary/<int:pk>/update/",
        CommentaryUpdateView.as_view(),
        name="commentary-update",
    ),
    path("accounts/register/", RegisterView.as_view(), name="register"),
    path("offer/search/", SearchOfferView.as_view(), name="search-offer"),
    path("info/", InfoView.as_view(), name="info"),
    path("car/", CarsView.as_view(), name="cars"),
    path("insurance/", InsuranceView.as_view(), name="insurance"),
    path("hospital/", HospitalView.as_view(), name="hospital"),
    path("custom/", CustomView.as_view(), name="custom"),
    path("canyons/", CanyonsView.as_view(), name="canyons"),
    path("springs/", SpringsView.as_view(), name="springs"),
    path("beaches/", BeachesView.as_view(), name="beaches"),
    path("hammam/", HammamView.as_view(), name="hammam"),
]

app_name = "catalog"
