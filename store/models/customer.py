from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=8)
    email=models.EmailField()
    password = models.CharField(max_length=100)
    # gender = models.CharField(max_length=10, default='-')
    # height = models.FloatField(blank=True, null=True)
    # weight = models.FloatField(blank=True, null=True)
       
    
    def __str__(self):
        return f"ID#{self.id} | {self.first_name} {self.last_name} | E-Mail: {self.email}"

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