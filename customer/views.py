from django.shortcuts import render,redirect
from . models import *
from agency. models import *
# Create your views here.
def Index(request):
    return render(request,'customer/index.html')
def Signup(request):
    if request.method=='POST':
        Name=request.POST['name']
        Email=request.POST['email']
        Password=request.POST['password1']
        customer=Customer(name=Name,email=Email,password=Password)
        customer.save()
        return redirect('customer:login')
    return render(request,'customer/signup.html')
def Login(request):
    if request.method=='POST':
        Email=request.POST['email']
        Password=request.POST['password']
        try:
            cust=Customer.objects.get(email=Email,password=Password)
            request.session['customer']=cust.id
            return redirect('customer:tours')
        except Customer.DoesNotExist:
            return render(request,'customer/login.html',{'msg':'invalid email or password'})
       
        # if Customer.objects.filter(email=Email,password=Password).exists():
        #     return redirect('customer:tours')
        # else:
        #     return render(request,'customer/login.html',{'msg':'invalid email or password'})
    return render(request,'customer/login.html')
def Tours(request):
    if 'customer' in request.session:
        alltours=Addtours.objects.all()
        return render(request,'customer/tours.html',{'alltours':alltours})
    else:
        return render(request,'customer/index.html')
def About(request): 
    return render(request,'customer/about.html')
def Contact(request):
    return render(request,'customer/contact.html')
def Booktours(request,tour_id):
    if 'customer' in request.session:
      tour=Addtours.objects.get(id=tour_id)
      agency_id=tour.Agency.id
      agency=AgencyRegistration.objects.get(id=agency_id)
      if request.method=='POST':
          Username=request.POST['username']
          Mobile=request.POST['phone']
          Address=request.POST['address']
          Pincode=request.POST['pin']
          application=Applications(tour=tour,agency=agency,name=Username,mobile=Mobile,address=Address,pincode=Pincode)
          application.save()

          return redirect('customer:payment')
      return render(request,'customer/booktours.html')
    else:
        return render(request,'customer/index.html')
def Logout(request):
    if 'customer' in request.session:
        del request.session['customer']
        return render(request,'customer/index.html')
    else:
        return render(request,'customer/index.html')
def Payment(request):
    return render(request,'customer/payment.html')

          

