from django.contrib import admin
from .models import Offers


class OfferAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'discount')


admin.site.register(Offers, OfferAdmin)
