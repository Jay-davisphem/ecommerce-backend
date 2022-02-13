from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category, FoodType, Food, FoodImage, MeatType


admin.site.register(Category, MPTTModelAdmin)


class FoodTypeModelAdmin(admin.ModelAdmin):
    model = FoodType


admin.site.register(FoodType, FoodTypeModelAdmin)


class MeatTypeModelAdmin(admin.ModelAdmin):
    model = MeatType


admin.site.register(MeatType, MeatTypeModelAdmin)


class FoodImageInline(admin.TabularInline):
    model = FoodImage


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    inlines = [
        FoodImageInline,
    ]
