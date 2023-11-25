from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=500)

      # this code is email validation in signup
    def isExists(self):
        return Customer.objects.filter(email=self.email).exists()
    
     # this code is get customer by email in login page
    @staticmethod
    def  get_customer_by_email(email):
          try:
            return Customer.objects.get(email=email)
          except:
              False