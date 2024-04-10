from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from catalog.models import Author, Offer, Service


class AuthorViewTest(TestCase):
    def setUp(self):
        self.author1 = Author.objects.create(username="author1")
        self.author2 = Author.objects.create(username="author2")
        self.service = Service.objects.create(name="test_service")
        Offer.objects.create(
            name="Offer 1", posted_by=self.author1, service_type=self.service
        )
        Offer.objects.create(
            name="Offer 2", posted_by=self.author2, service_type=self.service
        )

    def test_author_list_view(self):
        response = self.client.get(reverse("catalog:author-list"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context["authors_with_offers"],
            [self.author1, self.author2],
            ordered=False,
        )
        self.assertTemplateUsed(response, "catalog/author_list.html")


class PrivateAuthorViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            first_name="testuser", last_name="testuserlast"
        )
        self.client.force_login(self.user)

    def test_author_update_view(self):
        author = self.user
        url = reverse("catalog:author-update", kwargs={"pk": author.pk})
        new_data = {"first_name": "New First Name", "last_name": "New Last Name"}
        response = self.client.post(url, new_data)
        self.assertRedirects(response, reverse("catalog:author-list"))

        updated_author = Author.objects.get(pk=author.pk)
        updated_author.first_name = new_data["first_name"]
        updated_author.last_name = new_data["last_name"]
        updated_author.save()

        self.assertEqual(updated_author.first_name, new_data["first_name"])
        self.assertEqual(updated_author.last_name, new_data["last_name"])


class AuthorDetailViewTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(first_name="John", last_name="Doe")
        self.service = Service.objects.create(name="Service 1")
        self.offer1 = Offer.objects.create(
            name="Offer 1", posted_by=self.author, service_type=self.service
        )
        self.offer2 = Offer.objects.create(
            name="Offer 2", posted_by=self.author, service_type=self.service
        )

    def test_author_detail_view(self):
        url = reverse("catalog:author-detail", kwargs={"pk": self.author.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.author.first_name)
        self.assertContains(response, self.author.last_name)

        self.assertContains(response, self.offer1.name)
        self.assertContains(response, self.service.name)
        self.assertContains(response, self.offer2.name)
        self.assertContains(response, self.service.name)
