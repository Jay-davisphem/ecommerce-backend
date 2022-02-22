from django.shortcuts import render
from rest_framework import generics
from .models import Food
from . import models
from .serializers import FoodSerializer


class FoodListView(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class Food(generics.RetrieveAPIView):
    lookup_field = 'slug'
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class CategoryItemView(generics.ListAPIView):
    serializer_class = FoodSerializer

    def get_queryset(self):
        return models.Food.objects.filter(category__slug=self.kwargs['slug'])


'''class FoodTypeView(generics.ListAPIView):
    serializer_class = FoodSerializer

    def get_queryset(self):
        return models.Food.objects.filter(food_type__slug=self.kwargs['slug'])'''
