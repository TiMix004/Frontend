from django.contrib import admin
from django.urls import path
from .views import get_items, create_item

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/', get_items),
    path('items_create/', create_item),
]