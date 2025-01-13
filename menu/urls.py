from django.urls import path
from menu.controllers.menu_item_controller import MenuItemSaveController, MenuItemGetController

urlpatterns = [
    path('menuitems/', MenuItemSaveController.as_view(), name="save_menuitem"),
    path('menuitems/find/<int:pk>', MenuItemGetController.as_view(), name="menu_item_find")
]