from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from catalog.models import Offer, Service


class AddCommentCreateViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user", password="test_password"
        )
        self.service = Service.objects.create(name="test_service")
        self.offer = Offer.objects.create(
            name="Test Offer", posted_by=self.user, service_type=self.service
        )
        self.url = reverse("catalog:offer-comment-create", kwargs={"pk": self.offer.pk})
        self.client.login(username="test_user", password="test_password")

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "catalog/comment_create.html")


class CommentaryUpdateViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username="test_user", password="test_password"
        )
        self.service = Service.objects.create(name="test_service1")
        self.offer = Offer.objects.create(
            name="Test Offer", posted_by=self.user, service_type=self.service
        )
        self.url = reverse("catalog:offer-comment-create", kwargs={"pk": self.offer.pk})
        self.client.login(username="test_user", password="test_password")
        self.client.force_login(self.user)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
