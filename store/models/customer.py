from django.db import models
from .color import Color
from .gender import Gender

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=8)
    email=models.EmailField()
    password = models.CharField(max_length=100)
    
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    bmi = models.FloatField(blank=True, null=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, default=1, blank=True, null=True)
       
    
    def __str__(self):
        return f"(#{self.id}) {self.first_name} {self.last_name} || {self.email}"

    #to save the data
    def register(self):
        self.save()


    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email= email)
        except:
            return False


    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False