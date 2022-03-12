from rest_framework import serializers

from .models import Food, FoodImage, Category, FoodType, MeatType, CartItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodImage
        fields = ['image', 'alt_text']


class MeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeatType
        fields = ['name', 'price']


class FoodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodType
        fields = ['name']


class FoodSerializer(serializers.ModelSerializer):
    food_image = ImageSerializer(many=True, read_only=True)
    meats = MeatSerializer(many=True, read_only=True)
    food_type = FoodTypeSerializer(many=False, read_only=True)

    class Meta:
        model = Food
        fields = ['title', 'meats', 'food_type', 'category',
                  'description', 'slug', 'regular_price', 'discount_price', 'food_image']


class CartSerializer(serializers.ModelSerializer):
    food = FoodSerializer(many=False, read_only=True)

    class Meta:
        model = CartItem
        fields = ['food']
