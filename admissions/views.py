from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(reequest):

    return HttpResponse("Please search the URL  you want")


def addadmission(request):


    # form = StudentModelForm
    # studentform = {'form': form}
    #     if request.method == 'POST':

    #         form = StudentModel(request)
    #         return HttpResponse("New Admission Added Successfully")  

    #     else:
    return render(request,'admissions/addadmission.html')          
          

    # return HttpResponse("Add new Admission Here")
    

def admissionreport(request):

    return render(request, 'admissions/admissionreport.html')

    # return HttpResponse("See Admissions Report Here")


