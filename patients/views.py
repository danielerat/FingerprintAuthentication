from django.shortcuts import render
from django.http import HttpResponse
# from .models import Question

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
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    context={"name":"ilnuga gisa dnaiel","household":pk}
    return render(request, 'patients/household.html',context)