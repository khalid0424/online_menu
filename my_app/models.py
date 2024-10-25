from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class MenuItem(models.Model):
    item_name = models.CharField(max_length=100)
    item_description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)  

    def __str__(self):
        return self.item_name

