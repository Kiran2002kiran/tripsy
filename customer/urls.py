from django.urls import path
from.import views
app_name='customer'
urlpatterns=[
    path('',views.Index,name='index'),
    path('signup/',views.Signup,name='signup'),
    path('login/',views.Login,name='login'),
    path('tours/',views.Tours,name='tours'),
    path('about/',views.About,name='about'),
    path('contact/',views.Contact,name='contact'),
    path('booktours/<int:tour_id>',views.Booktours,name='booktours'),
    path('customer_logout/',views.Logout,name='customerlogout'),
    path('payment/',views.Payment,name='payment')
]