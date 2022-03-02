from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser
from .models import Food, Category, FoodType
from . import models
from .serializers import FoodSerializer, CategorySerializer
from .permissions import IsCook, IsCustomer


class FoodListView(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


'''class Food(viewsets.ModelViewSet):
    lookup_field = 'slug'
    queryset = Food.objects.all()
    erializer_class = FoodSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsCustomer | True]
        else:
            permission_classes = [IsCook | IsAdminUser]
'''


class Food(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsCook | IsAdminUser]
    lookup_field = 'slug'
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class CategoryItemView(generics.ListAPIView):
    serializer_class = FoodSerializer

    def get_queryset(self):
        return models.Food.objects.filter(category__slug=self.kwargs['slug'])


class FoodTypeView(generics.ListAPIView):
    serializer_class = FoodSerializer

    def get_queryset(self):
        return models.Food.objects.filter(food_type__name__iexact=self.kwargs['slug'])


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.filter(level=1)
    serializer_class = CategorySerializer


"""class FoodTypeListView(generics.ListAPIView):
    queryset = FoodType.objects.all()
    serializer_class = FoodSerializer"""
