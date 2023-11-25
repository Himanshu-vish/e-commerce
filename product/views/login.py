from django.shortcuts import render,redirect
from product.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View


class Login(View):
    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_customer_by_email(email)
        error_massage=None
        if customer:
            f=check_password(password,customer.password)
            print(f)#True....that means password searched
            if f:
                request.session['customer']=customer.id #for cart
                #request.session['customer_email']=customer.email #for cart
                return redirect('homepage')
            else:
                error_massage='Email or password incorrect !!'
        else:
            error_massage='Email or password incorrect !!'
        print(customer)
        print(email,password)
        return render(request,'login.html',{'error':error_massage})
        
    def get(self,request):
          return render(request,'login.html')

def logout(request):
    request.session.clear()
    return redirect('login')