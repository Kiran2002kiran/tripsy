from django.shortcuts import render,redirect
from . models import *
from customer.models import Applications
# Create your views here.
def Agency_login(request):
    if request.method=='POST':
        Userid=request.POST['userid']
        Password=request.POST['password1']
        try:
            agency=AgencyRegistration.objects.get(userid=Userid,password=Password)
            request.session['agency']=agency.id
            return redirect('agency:viewtours')
        except AgencyRegistration.DoesNotExist:
            return render(request,'agency/agency_login.html',{'msg':'Invalid userid or password'})
    return render(request,'agency/agency_login.html')
def Agency_signup(request):
    if request.method=='POST':
        agencyname=request.POST['agencyname']
        branches=request.POST['branches']
        ownername=request.POST['ownername']
        license=request.POST['license']
        userid=request.POST['userid']
        password=request.POST['password1']
        agency=AgencyRegistration(agencyname=agencyname,branches=branches,ownername=ownername,license=license,userid=userid,password=password)
        agency.save()
        return redirect('agency:agency_login')
    return render(request,'agency/agency_signup.html')
def Agency_addtours(request):
 if 'agency' in request.session:
    agency_id=request.session.get('agency')
    agency=AgencyRegistration.objects.get(id=agency_id)
    if request.method=='POST':
        agency_id=request.POST.get('agency')
        destination=request.POST.get('destination')
        description=request.POST.get('description')
        dest_img=request.FILES['dest_img']
        charge=request.POST.get('charge')
        addtours=Addtours(Agency=agency,Destination=destination,Description=description,Image=dest_img,Charge=charge)
        addtours.save()
        return redirect('agency:viewtours')
    return render(request,'agency/add_tours.html',{'agency':agency})
 else:
    return render('customer/index')
def Agency_viewtours(request):
 if 'agency' in request.session:
    agency_id=request.session.get('agency')
    agency=AgencyRegistration.objects.get(id=agency_id)
    tours=Addtours.objects.filter(Agency=agency)
    return render(request,'agency/view_tours.html',{'tours':tours,'agency':agency})
 else:
    return redirect('customer/index')
def Agency_viewdetails(request,tour_id):
 if 'agency' in request.session:
    tour=Addtours.objects.get(id=tour_id)
    return render(request,'agency/viewdetails.html',{'tour':tour})
 else:
    return redirect('customer/index')
def Agency_deletetours(request,tour_id):
    Addtours.objects.get(id=tour_id).delete()
    return redirect('agency:viewtours')
def Agency_updatetours(request,tour_id):
 if 'agency' in request.session:
    agency_id=request.session.get('agency')
    agency_obj=AgencyRegistration.objects.get(id=agency_id)
    agency=AgencyRegistration.objects.all()
    tour=Addtours.objects.get(id=tour_id)
    if request.method=='POST':
        
        destination=request.POST.get('destination')
        description=request.POST.get('description')
        dest_img=request.FILES['dest_img']
        charge=request.POST.get('charge')
        tour.Agency=agency_obj
        tour.Destination=destination
        tour.Description=description
        tour.Charge=charge
        tour.Image=dest_img
        tour.save()
        return redirect('agency:viewtours')
    

    return render(request,'agency/update_tours.html',{'tour':tour,'agency':agency})
 else:
    return redirect('customer/index')
def Agency_logout(request):
   if 'agency' in request.session:
      del request.session['agency']
      return render(request,'agency/agency_login.html')
   else:
      return render(request,'agency/agency_login.html')
def Agency_viewapplicants(request):
    if 'agency' in request.session:
        agency_id=request.session.get('agency')
        agency=AgencyRegistration.objects.get(id=agency_id)
        applications=Applications.objects.filter(agency=agency)
        return render(request,'agency/viewapplicants.html',{'applications':applications})
    else:
      return render(request,'agency/agency_login.html')