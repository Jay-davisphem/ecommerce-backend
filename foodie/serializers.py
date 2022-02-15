from rest_framework import serializers

from .models import Food


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['title', 'meats', 'food_type', 'category',
                  'description', 'regular_price', 'discount_price', 'food_image']
