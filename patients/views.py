from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse
from .models import Patriarch,Family,Processing,Invoice
from .forms import InvoiceForm,BillForm
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
        messages.success(request, "Successfully deleted processing patient")
        return redirect('patients:processing')
    context={"patient":patient,"cancelLink":"patients:processing"}
    return render(request, "patients/delete_processing.html", context)


def delete_recorded_patient(request, pk):
    try:
        record = Invoice.objects.get(patient=pk)
        messages.info(request, "You are about to delete a patient")

    except:
        messages.error(request, "Unable to delete The recorded patient")
        return redirect('patients:records')
   
    if request.method == 'POST':
        record.delete()
        messages.success(request, "Successfully deleted the recorded patient")
        return redirect('patients:records')
    context={"patient":record,"cancelLink":"patients:records"}
    return render(request, "patients/delete_processing.html", context)

def create_invoice(request,pk):
    invoiceForm = InvoiceForm()
    billForm = BillForm()
    
    health_faculty=request.user.profile.health_faculty
    # Check Whether it is a legit patient from the processing table
    try: 
        patient = Processing.objects.get(patient=pk)    
    except:
        messages.error(request, "Unknown Patient make sure you choose a valid patient")
        return redirect('patients:processing')

    if request.method == 'POST':
        billForm = BillForm(request.POST)
        invoiceForm = InvoiceForm(request.POST)
        if billForm.is_valid() and invoiceForm.is_valid():
            bill=billForm.save()
            invoice=invoiceForm.save(commit=False)
            invoice.bill=bill
            invoice.patient=patient.patient
            invoice.health_faculty=health_faculty
            invoice.save()
            patient.delete()
            messages.success(request, "Invoice Successfully Recorded")
            return redirect('patients:records')
        else:
            messages.error(request, "Truing to add Medecine to the wrong patient, try again later")
            return redirect('patients:processing')

    context={"patient":patient,"invoiceForm":invoiceForm,"billForm":billForm}
    return render(request, "patients/create_invoice.html", context)

def records(request):
    health_faculty=request.user.profile.health_faculty
    invoice = Invoice.objects.filter(health_faculty=health_faculty)
    context={"invoice":invoice}
    return render(request,'patients/records.html',context)
