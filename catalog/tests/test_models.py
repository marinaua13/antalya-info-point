from django.contrib.auth import get_user_model
from django.test import TestCase

from catalog.models import Service, Offer, Company


class TestModels(TestCase):

    def test_author_str(self):
        author = get_user_model().objects.create(
            username="test",
            password="test1234",
            first_name="test_first",
            last_name="test_last",
        )
        self.assertEqual(str(author), author.username)

    def test_service_str(self):
        service = Service.objects.create(name="test_service")
        self.assertEqual(str(service), service.name)

    def test_offer_str(self):
        author = get_user_model().objects.create(username="test")
        service = Service.objects.create(name="test_service")
        offer = Offer.objects.create(
            name="test_offer", posted_by=author, service_type=service
        )
        self.assertEqual(str(offer), f"{offer.name} - {offer.posted_by}")

    def test_company_str(self):
        company = Company.objects.create(name="test_company", opening_year=2009)
        self.assertEqual(str(company), f"{company.name} from {company.opening_year}")
