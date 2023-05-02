from django.db import models

class Color(models.Model):
    name= models.CharField(max_length=50)

    @staticmethod
    def get_all_colors():
        return Color.objects.all()

    def __str__(self):
        return self.name
