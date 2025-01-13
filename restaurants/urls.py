from django.urls import path
from restaurants.controllers.restaurant_controller import RestaurantSaveController, RestaurantListController
from .controllers.menu_category_controller import MenuCategorySaveController 

urlpatterns = [
    path('restaurants/', RestaurantSaveController.as_view(), name="save_restaurant"),
    path('restaurants/list', RestaurantListController.as_view(), name="restaurant_list"),
    path('menu/categories/', MenuCategorySaveController.as_view(), name="save_menu_category")
]