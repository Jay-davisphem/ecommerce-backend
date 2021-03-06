from rest_framework import serializers
from . import models
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class FoodImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FoodImage
        fields = "__all__"


class MeatImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MeatImage
        fields = ("food_images", "is_feature")


class FoodSerializer(serializers.ModelSerializer):
    food_images = FoodImageSerializer(many=True, read_only=True)
    print(food_images, "lovi lovi")

    class Meta:
        model = models.Food
        fields = [
            "id",
            "name",
            "description",
            "regular_price",
            "discount_price",
            "vendor",
            "category",
            "meats",
            "food_images",
        ]


class MeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Meat
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        exclude = [
            "is_staff",
            "is_active",
            "is_superuser",
            "last_login",
            "date_joined",
            "user_permissions",
            "groups",
        ]


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        exclude = [
            "password",
            "is_staff",
            "is_active",
            "is_superuser",
            "last_login",
            "date_joined",
            "groups",
        ]


class CustomerLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomerLogin
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(email=validated_data["email"], username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        Token.objects.create(user=user)
        return user


class VendorLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VendorLogin
        fields = "__all__"


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartItem
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        exclude = ["user"]


class OrderStatusCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderStatusCode
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = "__all__"


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shipment
        fields = "__all__"


class ShipmentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ShipmentItem
        fields = "__all__"
