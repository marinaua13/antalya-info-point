from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from catalog.models import Offer, Company, Service


class PublicOfferViewTest(TestCase):
    def test_login_not_required(self):
        url = reverse("catalog:offer-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/offer_list.html")

    def test_login_required(self):
        url = reverse("catalog:offer-create")
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)

    def test_retrieve_offer_detail_view(self):
        author = get_user_model().objects.create(username="test name")
        service = Service.objects.create(name="test service")
        company = Company.objects.create(name="test company")
        offer = Offer.objects.create(
            name="test offer",
            posted_by=author,
            description="test_description",
            price=200,
            company=company,
            service_type=service,
        )
        url = reverse("catalog:offer-detail", kwargs={"pk": offer.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/offer_detail.html")
        self.assertContains(response, offer.name)
        self.assertContains(response, offer.description)
        self.assertContains(response, offer.price)
        self.assertContains(response, offer.company)
        self.assertContains(response, offer.posted_by)


class PrivateOfferViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username="test")
        self.service = Service.objects.create(name="test service")
        self.client.force_login(self.user)

    def test_create_offer(self):
        response = self.client.post(
            reverse("catalog:offer-create"),
            {
                "name": "test new offer",
                "posted_by": self.user.id,
                "service_type": self.service.id,
            },
        )

        self.assertTrue(Offer.objects.filter(name="test new offer").exists())
        self.assertRedirects(response, reverse("catalog:offer-list"))
