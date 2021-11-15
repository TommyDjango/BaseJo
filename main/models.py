from django.db import models

class Catergory(models.Model):
    name = models.CharField(
        max_length=20,default='Other'
    )
    sub = models.CharField(
        max_length=20,default=''
    )

# Create your models here.
class Product(models.Model):
    name = models.CharField(
        verbose_name='Name',
        max_length=20
   )
    price = models.IntegerField(
        default=0
    )
    instock = models.BooleanField(
        default = True
    )
    quantity = models.IntegerField(
        default=1
    )
    men = "Mens"
    woman = 'Woman'
    kid = 'Kids'

    cat_of_products = (
        (men, 'Men'),
        (woman, 'Woman'),
        (kid, 'Kids'),
    )
    catergory = models.CharField(
        choices=cat_of_products, default='', max_length=10
    )

    def __str__(self):
        return f'{self.name},{self.price},{self.instock},{self.quantity}'