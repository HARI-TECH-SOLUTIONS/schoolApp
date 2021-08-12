from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def feeCollection(request):

    return render(request, 'finance/feecollection.html')

    # return HttpResponse("I will Get Fee from this view")



def feeDuesReport(request):

    return render(request, 'finance/feeduesreport.html')

    # return HttpResponse("I will Show the Fee Dues Report from this View")



def feeCollectionReport(request):

    return render(request, 'finance/feecollectionreport.html')

    # return HttpResponse("I will show the Fee Collection Report from this View")