from django.contrib import admin

from vehicle.models import *


# Register your models here.
@admin.register(Car)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(Moto)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(Milage)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["year"]
