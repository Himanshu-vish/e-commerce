from django.shortcuts import render
from django.views import View
from product.models.product import Product

class Cart(View):
    def get(self,request):
        ids=(list(request.session.get('cart').keys()))
        products=Product.get_products_for_cart(ids)
        print(products)
        return render(request,'cart.html',{'products':products})