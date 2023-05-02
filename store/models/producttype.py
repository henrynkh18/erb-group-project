from django.db import models
from .category import Category
from .sport import Sport
from .color import Color

class ProductType(models.Model):
    name = models.CharField(max_length=60)
    price= models.DecimalField(max_digits=6, decimal_places=2, default=99.00)
    description= models.TextField(blank=True, null=True)
    image= models.ImageField(upload_to='uploads/products/', default='image/noimage.jpeg')
    category= models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    sport= models.ForeignKey(Sport, on_delete=models.CASCADE, default=1)
    color= models.ForeignKey(Color, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.name

    @staticmethod
    def get_producttypes_by_id(ids):
        return ProductType.objects.filter(id__in=ids)
    
    @staticmethod
    def get_all_products():
        return ProductType.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return ProductType.objects.filter(category=category_id)
        elif category_id == 0:
            return ProductType.get_all_products()
        else:
            return ProductType.get_all_products()
        
    @staticmethod
    def get_all_products_by_colorid(color_id):
        if color_id:
            return ProductType.objects.filter(color=color_id)
        else:
            return ProductType.get_all_products()
    
    @staticmethod
    def get_all_products_by_sportid(sport_id):
        if sport_id:
            return ProductType.objects.filter(sport=sport_id)
        else:
            return ProductType.get_all_products()