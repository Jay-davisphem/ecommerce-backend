from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category, FoodType, Food, FoodImage, MeatType


admin.site.register(Category, MPTTModelAdmin)

admin.site.register(FoodType)


# class MeatTypeInline(admin.TabularInline):
#    model = MeatType


class MeatModelAdmin(admin.ModelAdmin):
    model = MeatType


admin.site.register(MeatType, MeatModelAdmin)


class FoodImageInline(admin.TabularInline):
    model = FoodImage


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    inlines = [
        FoodImageInline,  # MeatTypeInline
    ]
