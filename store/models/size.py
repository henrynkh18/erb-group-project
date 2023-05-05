from django.db import models
from .category import Category

class Size(models.Model):
    name= models.CharField(max_length=25)
    category= models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return f"{self.name} ({self.category})"

    @staticmethod
    def get_all_sizes():
        return Size.objects.all()

    @staticmethod
    def get_all_sizes_by_categoryid(category_id):
        if category_id:
            return Size.objects.filter(category=category_id)
        else:
            return Size.get_all_sizes()
        
    