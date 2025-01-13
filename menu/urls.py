from django.urls import path
from menu.controllers.menu_item_controller import MenuItemSaveController

urlpatterns = [
    path('menuitems/', MenuItemSaveController.as_view(), name="save_menuitem")
]