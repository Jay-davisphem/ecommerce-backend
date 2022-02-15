from django.urls import path
from . import views

app_name = 'foodie'

urlpatterns = [
        path('api/', views.FoodListView.as_view(), name='food_home'),

        ]

