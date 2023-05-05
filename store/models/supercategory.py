from django.db import models

class SuperCategory(models.Model):
    name= models.CharField(max_length=50)

    @staticmethod
    def get_all_genders():
        return SuperCategory.objects.all()

    def __str__(self):
        return self.name