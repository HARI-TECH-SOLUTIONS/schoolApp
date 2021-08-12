from django.urls import path
from .views import *

urlpatterns = [

    #--------For Finance app----------------
    path('feecollection/',feeCollection),
    path('feeduesreport/',feeDuesReport),
    path('feecollectionreport/',feeCollectionReport),

]