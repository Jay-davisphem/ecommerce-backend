from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser
from .models import Food, Category, FoodType, CartItem
from . import models
from .serializers import FoodSerializer, CategorySerializer, CartSerializer
from .permissions import IsCook, IsCustomer
from django.shortcuts import get_object_or_404


'''class MultFM:
    def get_object(self):
        queryset = self.queryset()
        queryset = self.filter_queryset(queryset)
        filter = {}
        for field in self.looku_fields:
            if self.kwargs[field]:
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj
'''


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
            permissi n_classes = [IsCook | IsAdminUser
'''


class Food(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [IsCook | IsAdminUser]
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


class CartListView(viewsets.ViewSet):
    def list(self, request):
        queryset = CartItem.objects.all()
        serializer = CartSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = CartItem.objects.all()
        cart = get_object_or_404(queryset, pk=pk)
        serializer = CartSerializer(cart)
        return Response(serializer.data)
