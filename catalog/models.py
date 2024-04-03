from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import forms


class Author(AbstractUser):
    years_of_experience = models.IntegerField(default=0, blank=True, null=True)
    mobile_phone = models.CharField(max_length=20, blank=True, null=True)
    picture = models.ImageField(upload_to="authors_pictures", null=True, blank=True)

    # class Meta:
    #     model = Author
    #     fields = ['mobile_phone', 'picture']


class Service(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.name


class Offer(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    service_type = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="offers"
    )
    posted_date = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="offers"
    )
    company = models.ForeignKey(
        "Company",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="offers",
    )

    class Meta:
        verbose_name = "Offer"
        verbose_name_plural = "Offers"

    def __str__(self):
        return f"{self.name} - {self.posted_by}"


class Company(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(blank=True, null=True)
    opening_year = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return f"{self.name} - {self.opening_year}"


class Commentary(models.Model):
    user = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="commentaries"
    )
    offer = models.ForeignKey(
        Offer, on_delete=models.CASCADE, related_name="commentaries"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ["-created_time"]
        verbose_name = "Commentary"
        verbose_name_plural = "Commentaries"
