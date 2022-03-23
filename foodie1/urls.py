from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'foodie'

router = routers.DefaultRouter()
router.register(r'foods', views.FoodViewSet)
router.register(r'meats', views.MeatViewSet)
#router.register(r'categories', views.CategoryViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'vendors', views.VendorViewSet)
router.register(r'food-images', views.FoodImageViewSet)
router.register(r'meat-images', views.MeatImageViewSet)

urlpatterns = [
        path('apis/categories/', views.CategoryListView.as_view(), name='category-lists'),
        path('apis/categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'), 
        path('apis/', include(router.urls)),
        path('login/', views.LoginView.as_view(), name='login'),
        path('users/', views.CreateUser.as_view(), name='user_create'),
]