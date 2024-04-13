from django.urls import path
from.import views
app_name='agency'
urlpatterns=[
    path('agency_login/',views.Agency_login,name='agency_login'),
    path('agency_signup/',views.Agency_signup,name='agency_signup'),
    path('addtours/',views.Agency_addtours,name='addtours'),
    path('viewtours/',views.Agency_viewtours,name='viewtours'),
    path('viewdetails/<int:tour_id>',views.Agency_viewdetails,name='viewdetails'),
    path('delete_tours/<int:tour_id>',views.Agency_deletetours,name='delete_tours'),
    path('update_tours/<int:tour_id>',views.Agency_updatetours,name='update_tours'),
    path('agency_logout/',views.Agency_logout,name='agencylogout'),
    path('viewapplicants/',views.Agency_viewapplicants,name='viewapplicants')
]