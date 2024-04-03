from catalog import views
from django.urls import path

from catalog.views import (
    index,
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

)

urlpatterns = [
    path("", index, name="index"),
    path("service/", ServiceListView.as_view(), name="service-list"),
    path("service/create/", ServiceCreateView.as_view(), name="service-create"),
    path("service/<int:pk>/", ServiceDetailView.as_view(), name="service-detail"),
    path("service/<int:service_id>/offer/", ServiceOfferListView.as_view(), name="service-offer-list"),
    path("author/", AuthorListView.as_view(), name="author-list"),
    path("author/create/", AuthorCreateView.as_view(), name="author_create"),
    path("author/<int:pk>/update", AuthorUpdateView.as_view(), name="author-update"),
    path("author/<int:pk>/", AuthorDetailView.as_view(), name="author_detail"),
    path("offer/", OfferListView.as_view(), name="offer-list"),
    path("offer/<int:pk>/", OfferDetailView.as_view(), name="offer-detail"),
    path("offer/create/", OfferCreateList.as_view(), name="offer-create"),
    path("offer/<int:pk>/commentary", AddCommentCreateView.as_view(), name="offer-comment-create"),
    path("accounts/register/", views.register, name="register"),
    path("offer/search/", views.search_offer, name="search-offer"),
    path("info/", views.info, name="info")


]

app_name = "catalog"
