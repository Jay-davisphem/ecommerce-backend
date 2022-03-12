from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'foodie'
router = DefaultRouter()
router.register('cart', views.CartListView, basename='cart')
urlpatterns = [
    path('api/', views.FoodListView.as_view(), name='food_home'),
    path('api/category/', views.CategoryListView.as_view(), name='categories'),
    path('api/', include(router.urls)),
    path('api/<slug:slug>/', views.Food.as_view(), name='food'),
    path('api/category/<slug:slug>/',
         views.CategoryItemView.as_view(), name='category_item'),
    path('api/foodtype/<slug:slug>',
         views.FoodTypeView.as_view(), name='food_type'),

]
