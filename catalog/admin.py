from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from catalog.models import Author, Service, Offer, Commentary, Company


@admin.register(Author)
class AuthorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience", "mobile_phone", "picture",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("years_of_experience", "mobile_phone", "picture")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional Info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "years_of_experience",
                    "mobile_phone",
                    "picture"
                )
            },
        ),
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "price",
        "service_type",
        "posted_by",
        "posted_date",
        "company",
    )
    search_fields = ("service_type",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "offer",
        "created_time",
        "content",
    )
    search_fields = ("offer",)


admin.site.register(Company)
