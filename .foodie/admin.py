'''from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category, FoodType, Food, FoodImage, MeatType, CartItem


admin.site.register(Category, MPTTModelAdmin)

admin.site.register(FoodType)


# class MeatTypeInline(admin.TabularInline):
#    model = MeatType

admin.site.register(MeatType)


class FoodImageInline(admin.TabularInline):
    model = FoodImage


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    inlines = [
        FoodImageInline,  # MeatTypeInline
    ]


admin.site.register(CartItem)
'''
