from django.urls import path
from restaurants.controllers.restaurant_controller import RestaurantSaveController
from .controllers.menu_category_controller import MenuCategorySaveController 

urlpatterns = [
    path('restaurants/', RestaurantSaveController.as_view(), name="save_restaurant"),
    path('menu/categories/', MenuCategorySaveController.as_view(), name="save_menu_category")
]