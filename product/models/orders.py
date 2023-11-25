from django.db import models
from .product import Product
from .customer import Customer
import datetime


class Order(models.Model):
   product=models.ForeignKey(Product,on_delete=models.CASCADE)
   customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
   quantity=models.IntegerField(default=1)
   price=models.IntegerField()
   address=models.CharField(max_length=100,blank=True,default='')
   phone=models.CharField(max_length=20,blank=True,default='')
   date=models.DateField(default=datetime.datetime.today)
   status=models.BooleanField(default=False)
  
   def get_orders_by_customer(customer_id):
      return Order.objects.filter(customer=customer_id).order_by('-date')