from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from catalog.models import Service, Offer

SERVICE_URL = reverse("catalog:service-list")


class TestServiceView(TestCase):

    def test_login_not_required(self):
        response = self.client.get(SERVICE_URL)
        self.assertEqual(response.status_code, 200)

    def test_login_required(self):
        response = self.client.get(SERVICE_URL)
        self.assertEqual(response.status_code, 200)

    def test_retrieve_service_view(self):
        response = self.client.get(SERVICE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/service_list.html")

    def test_retrieve_service_detail_view(self):
        service = Service.objects.create(name="Test Service")
        url = reverse("catalog:service-detail", kwargs={"pk": service.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/service_detail.html")

    def test_retrieve_service_offer_list_view(self):
        service = Service.objects.create(name="Test Service")

        url = reverse("catalog:service-offer-list", kwargs={"service_id": service.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/service_offers_list.html")


class TestServiceOfferView(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="test")
        self.service = Service.objects.create(name="Test Service")
        self.offer1 = Offer.objects.create(
            name="Test Offer1", posted_by=self.user, service_type=self.service
        )
        self.offer2 = Offer.objects.create(
            name="Test Offer2", posted_by=self.user, service_type=self.service
        )

    def test_correct_display_list_offers(self):
        url = reverse(
            "catalog:service-offer-list", kwargs={"service_id": self.service.pk}
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("offers", response.context)
        self.assertContains(response, self.service.name)
        for offer in Offer.objects.filter(service_type=self.service):
            self.assertContains(response, offer.name)

    def test_display_error_for_invalid_service_id(self):
        invalid_service_id = 9999
        url = reverse(
            "catalog:service-offer-list", kwargs={"service_id": invalid_service_id}
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)
