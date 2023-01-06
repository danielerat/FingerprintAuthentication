from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse
from .models import Patriarch
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
    # context = {'latest_question_list': latest_question_list}
     return HttpResponse('patients/test.html')
    

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
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    context={"name":"ilnuga gisa dnaiel","patients":lst}
    return render(request, 'patients/household_search.html',context)

def household(request,pk):
    try:
        household = Patriarch.objects.get(nationalId=pk)
        household_members=household.family_set.all()
    except:
        messages.error(request, "Unknown Household")
        return redirect('patients:household_search')

    context={"household":household,'members':household_members}
    return render(request,'patients/household.html',context)

def household_member(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    context={"name":"ilnuga gisa dnaiel","household":""}
    return render(request,'patients/household_member.html',context)

def processing(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    context={"name":"ilnuga gisa dnaiel","household":""}
    return render(request,'patients/processing_patients.html',context)

def authenticate(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    context={"name":"ilnuga gisa dnaiel","household":""}
    return render(request,'patients/authenticating_patients.html',context)
    