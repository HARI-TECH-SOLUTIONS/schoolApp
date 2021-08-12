from django.urls import path
from .views import *


urlpatterns = [

    #--------For Admisson app---------------
    path('addadmission',addadmission),
    path('admissionreport',admissionreport),

]