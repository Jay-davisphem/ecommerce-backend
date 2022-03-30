from django.contrib.auth import authenticate  # , login
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, mixins
from django.contrib.auth.models import User
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from . import models, serializers, permissions
from rest_framework.permissions import IsAdminUser


class Permission1Class:
    permission_classes = (IsAdminUser | permissions.IsUserPermission, )


class FoodViewSet(Permission1Class, ModelViewSet):
    serializer_class = serializers.FoodSerializer
    queryset = models.Food.objects.all()


class MeatViewSet(Permission1Class, ModelViewSet):
    serializer_class = serializers.MeatSerializer
    queryset = models.Meat.objects.all()


class CategoryListView(generics.ListCreateAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()
    permission_classes = [IsAdminUser |
                          permissions.IsVendor or permissions.IsReadOnly]


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()
    permission_classes = [
        permissions.IsVendorAndOwner or permissions.IsReadOnly]


class Permission2Class:
    permission_classes = (permissions.IsAccountOwner, )
class CustomerViewSet(Permission2Class, ModelViewSet):
    serializer_class = serializers.CustomerSerializer
    queryset = models.Customer.objects.all()


class VendorViewSet(Permission2Class, ModelViewSet):
    serializer_class = serializers.VendorSerializer
    queryset = models.Vendor.objects.all()


class FoodImageViewSet(Permission1Class, ModelViewSet):
    serializer_class = serializers.FoodImageSerializer
    queryset = models.FoodImage.objects.all()
class MeatImageViewSet(Permission1Class, ModelViewSet):
    serializer_class = serializers.MeatImageSerializer
    queryset = models.MeatImage.objects.all()



class SignUpView(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()


class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        print(request.user)
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)



class OrderStatusCodeViewSet(ModelViewSet):
    permission_classes = (IsAdminUser, )
    serializer_class = serializers.OrderStatusCodeSerializer
    queryset = models.OrderStatusCode.objects.all()


class CartItemViewSet(ModelViewSet):
    serializer_class = serializers.CartItemSerializer
    queryset = models.CartItem.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        if not(self.request.user.is_superuser):
            qs = qs.filter(cart__user=self.request.user)
        return qs

    '''def create(self, request, **kwargs):
        data = self.request.data
        data._mutable = True
        val = models.Cart(user=models.Customer.objects.filter(
            id=self.request.user.id)[0])
        if val:
            data['cart'] = val
        else:
            data['cart'] = 2
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        '''


class CartViewSet(ModelViewSet):
    serializer_class = serializers.CartSerializer
    queryset = models.Cart.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        if not(self.request.user.is_superuser):
            qs = qs.filter(user=self.request.user)
        return qs

    def create(self, request, **kwargs):
        data = self.request.data
        data._mutable = True
        data['user'] = self.request.user.id
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)