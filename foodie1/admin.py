from django.contrib import admin
from . import models
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(models.Category)
#admin.site.unregister(User)
admin.site.register(models.Customer)
admin.site.register(models.Vendor)


class FoodImageInline(admin.TabularInline):
    model = models.FoodImage


class MeatImageInline(admin.TabularInline):
    model = models.MeatImage


@admin.register(models.Food)
class FoodAdmin(admin.ModelAdmin):
    inlines = [
        FoodImageInline
    ]


@admin.register(models.Meat)
class MeatAdmin(admin.ModelAdmin):
    inlines = [
        MeatImageInline
    ]


admin.site.register(models.OrderItem)
admin.site.register(models.CartItem)
admin.site.register(models.OrderStatusCode)
admin.site.register(models.ShipmentItem)
admin.site.register(models.Order)
admin.site.register(models.Shipment)
