from django.urls import path
from . import views

#vIEWS  HANDLER
urlpatterns = [
    path('', views.kyc_form, name='kyc_form'),
    path('kyc_form',views.kyc_form, name='kyc_form'),
    path('kyc_details',views.kyc_details, name='kyc_details'),
    
    
]