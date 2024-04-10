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
    CommentaryDeleteView,
    CommentaryUpdateView,
    CommentaryDetailView,
)

urlpatterns = [
    path("", index, name="index"),
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
    path("commentary/<int:pk>/delete/", CommentaryDeleteView.as_view(), name="commentary-delete"),
    path("commentary/<int:pk>/", CommentaryDetailView.as_view(), name="comment-detail"),
    path("commentary/<int:pk>/update/", CommentaryUpdateView.as_view(), name="commentary-update"),
    path("accounts/register/", views.register, name="register"),
    path("offer/search/", views.search_offer, name="search-offer"),
    path("info/", views.info, name="info"),
    path("car/", views.cars, name="cars"),
    path("insurance/", views.insurance, name="insurance"),
    path("hospital/", views.hospital, name="hospital"),
    path("custom/", views.custom, name="custom"),
    path("canyons/", views.canyons, name="canyons"),
    path("springs/", views.springs, name="springs"),
    path("beaches/", views.beaches, name="beaches"),
    path("hammam/", views.hamam, name="hammam"),
]

app_name = "catalog"
