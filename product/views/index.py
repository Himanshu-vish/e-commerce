from django.shortcuts import render,redirect
from product.models.product import Product
from product.models.category import Category
from django.views import View


class Index(View):
    def post(self,request):
        product=request.POST.get('product') # yaha se product ki id milegi
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        if cart:
           quantity=cart.get(product)
           if quantity:
              if remove:
                if quantity<=1:
                   cart.pop(product)
                else:   
                  cart[product]=quantity-1
              else:
                 cart[product]=quantity+1  
           else:
              cart[product]=1   
        else:
           cart={}
           cart[product]=1
        request.session['cart']=cart
        #print(product)
        print(request.session['cart'])
        return redirect('homepage')
    def get(self,request):
        cart=request.session.get('cart')
        if not cart:
           request.session['cart']={}
        categories = Category.get_category()
        categoryId=request.GET.get('category')
        #print(categoryId)
        if categoryId:
          products = Product.get_product_byid(categoryId)
        else:
          products = Product.get_product()
        data = {
          'products': products,
          'categories': categories,
         }
        #print('you are',request.session.get('customer_email'))
        return render(request, 'index.html', data)



    

