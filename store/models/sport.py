from django.db import models

class Sport(models.Model):
    name= models.CharField(max_length=50)

    @staticmethod
    def get_all_sports():
        return Sport.objects.all()

    def __str__(self):
        return f'(#{self.id}) {self.name}'