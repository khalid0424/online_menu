from django.shortcuts import HttpResponse, render , get_object_or_404
from .models import Category, MenuItem

def category_list(request):
    categories = Category.objects.all() 
    return HttpResponse(request, 'category.html', {'categories': categories})

def menu_items_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)  
    menu_items = MenuItem.objects.filter(category=category)  
    return HttpResponse(request, 'menu.html', {'category': category, 'menu_items': menu_items})

