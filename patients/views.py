from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse
from .models import Patriarch,Family,Processing
from django.contrib import messages
# Create your views here.
lst=[
    {
        'id':1,
        'name':"Ilulnga gisa daniel",
        "age":11
    },
    {
        'id':2,
        'name':"Jacko james",
        "age":22
    },
    {
        'id':3,
        'name':"John wick",
        "age":33
    },
   
]
    

def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'sick':'inkorora'}
    return render(request,'patients/test.html',context )
    

def patients(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    context={"name":"ilnuga gisa dnaiel","patients":lst}
    return render(request, 'patients/patients.html',context)
def patient(request,pk):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    pol=1
    for i in lst:
        if i.get('id')==pk:
            pol=i
            break

    return render(request, 'patients/patient.html',{"patient":pol})


def household_serach(request):
    
    if request.method == 'POST':
        id = request.POST['householdId']
        try:
            householdId = Patriarch.objects.get(nationalId=id)
            print(householdId.id)
            return redirect('patients:household', pk=householdId.id)
        except:
            messages.error(request, "Unknown Id Card, Make sure you write well the ID")
            return render(request, 'patients/household_search.html')
    return render(request, 'patients/household_search.html')
   
def household(request,pk):
    try:
        household = Patriarch.objects.get(id=pk)
        household_members=household.family_set.all()
    except:
        messages.error(request, "Unknown Household")
        return redirect('patients:household_search')

    context={"household":household,'members':household_members}
    return render(request,'patients/household.html',context)




def household_member(request,pk):
    try:
        member = Family.objects.get(id=pk)
    except:
        messages.error(request, "Invalid Family Member, Make sure you select the correct Family Member")
        return redirect('patients:household_search')

    context={"member":member}
    return render(request,'patients/household_member.html',context)

def processing(request):
    healthFaculty=request.user.profile.health_faculty
    processing = Processing.objects.filter(healthFaculty=healthFaculty)
    context={"processing":processing}
    return render(request,'patients/processing_patients.html',context)

def authenticate(request,pk):
    try:
        member = Family.objects.get(id=pk)
    except:
        messages.error(request, "Invalid Family Member, Make sure you select the correct Family Member")
        return redirect('patients:household_search')
    context={"member":member}
    return render(request,'patients/authenticating_patients.html',context)


def deleteProcessingPatient(request, pk):
    try:
        patient = Processing.objects.get(patient=pk)
    except:
        messages.error(request, "Unable to delete processing patient")
        return redirect('patients:processing')
   
    if request.method == 'POST':
        patient.delete()
        messages.success(request, " Successfully deleted processing patient")
        return redirect('patients:processing')
    context={"patient":patient}
    return render(request, "patients/delete_processing.html", context)