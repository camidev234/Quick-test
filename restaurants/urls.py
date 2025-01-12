from django.urls import path
from restaurants.controllers.restaurant_controller import RestaurantSaveController

urlpatterns = [
    path('restaurants/', RestaurantSaveController.as_view(), name="save_restaurant"),
]