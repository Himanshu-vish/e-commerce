from django.shortcuts import render,redirect
from product.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View


class Signup(View):
    def post(self,request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'mobile': mobile,
            'email': email,
            'password': password
        }
        error_massage =self.user_validation(Customer(first_name=first_name, last_name=last_name, mobile=mobile, email=email, password=password))
        if not error_massage:
            hashed_password = make_password(password)
            customerData = Customer.objects.create(
                first_name=first_name,
                last_name=last_name,
                mobile=mobile,
                email=email,
                password=hashed_password
            )
            customerData.save()
            return redirect('homepage')
        else:
            data = {
                'error': error_massage,
                'values': value
            }
            return render(request, 'signup.html', data)
    def user_validation(self,customerData):
            error_massage = None
            if not customerData.first_name:
              error_massage = 'first name is required'
            elif len(customerData.first_name) < 4:
              error_massage = 'first name must be 4 char or more'
            elif not customerData.last_name:
              error_massage = 'last name is required'
            elif len(customerData.last_name) < 4:
              error_massage = 'last name must be 4 char or more'
            elif len(customerData.password) < 6:
              error_massage = 'password must be 6 char or more'
            elif Customer.objects.filter(email=customerData.email).exists():
              error_massage = 'Email address is already registered'
            return error_massage

    def get(self,request):
        return render(request, 'signup.html')

