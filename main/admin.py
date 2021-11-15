from django.contrib import admin
from  .models import Product, Catergory
# Register your models here.
@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ("name", "price", 'instock', 'quantity')
