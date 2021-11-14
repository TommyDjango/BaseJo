from django.contrib import admin
from  .models import Product
# Register your models here.
admin.site.register(Product)

class Product(admin.ModelAdmin):
    list_display = ('name', 'price', 'instock', 'quantity')
