from django.db import models
from .category import Category
from .sport import Sport
from .color import Color

from .producttype import ProductType
from .size import Size

class Product(models.Model):
    name= models.ForeignKey(ProductType, on_delete=models.CASCADE, default=1)
    size= models.ForeignKey(Size, on_delete=models.CASCADE, default=1)
    stock_on_hand= models.IntegerField(default=50)
    
    def __str__(self):
        return f"{self.name}, {self.size}, SOH: {self.stock_on_hand}"
    
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter (id__in=ids)
    
    @staticmethod
    def get_producttypes_by_id(ids):
        producttypes = {}
        if ids:
            products = Product.objects.filter (id__in=ids)
            for product in products:
                producttype = ProductType.objects.get(id = product.name.id)
                producttypes[product.name.id] = producttype          
        return producttypes
            