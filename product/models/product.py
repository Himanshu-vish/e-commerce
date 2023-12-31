from django.db import models
from .category import Category
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=20)
    price=models.PositiveIntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=500,default='',null=True,blank=True)
    image=models.ImageField(upload_to='uploads/products')

    @staticmethod
    def get_products_for_cart(ids):
        return Product.objects.filter(id__in=ids)
    
    
    
    @staticmethod
    def get_product():
        return Product.objects.all()
        

    @staticmethod
    def get_product_byid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_product()
        