from django.db import models
from .supercategory import SuperCategory

class Category(models.Model):
    name = models.CharField(max_length=50)
    super_category = models.ForeignKey(SuperCategory, on_delete=models.CASCADE, default=1)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return f"(#{self.id}) {self.super_category.name} / {self.name}"
