from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(
        verbose_name='Name',
        max_length=20
   )
    price = models.IntegerField(
        default=0
    )

    def __str__(self):
        return self.name