from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('categories/', views.menu_items_by_category, name='menu_items_by_category'),
]
