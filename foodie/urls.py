from django.urls import path
from . import views

app_name = 'foodie'

urlpatterns = [
    path('api/', views.FoodListView.as_view(), name='food_home'),
    path('api/<slug:slug>/', views.Food.as_view(), name='food'),
    path('api/category/<slug:slug>/',
         views.CategoryItemView.as_view(), name='category_item'),
    #path('api/foodtype/<slug:slug>',
    #     views.FoodTypeView.as_view(), name='food_type'),
]
