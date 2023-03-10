from queue import Queue
from django.shortcuts import render, get_object_or_404, redirect
import pyrebase
from django.utils import timezone

from django.contrib.auth.decorators import login_required


from datetime import datetime
import pytz
from django.http import HttpResponse
from .models import Patriarch,Family,Processing,Invoice
from .forms import InvoiceForm,BillForm
from django.contrib import messages
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Firebase Configurations
config = {
  "apiKey": "AIzaSyBVmS09_NOHFAreKDL4Nou6ZEtBA9_zGEo",
  "authDomain": "fingerprintesp-3a43c.firebaseapp.com",
  "databaseURL": "https://fingerprintesp-3a43c-default-rtdb.firebaseio.com",
  "projectId": "fingerprintesp-3a43c",
  "storageBucket": "fingerprintesp-3a43c.appspot.com",
  "messagingSenderId": "1086377241362",
  "appId": "1:1086377241362:web:69f85cfadbe417cdb3a1cb"
}
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

def update_firebase(request):
    fam=Family.objects.all()
    my_tz = pytz.timezone("Africa/Kigali")
    now = datetime.now(my_tz)
    timestamp=int(datetime.timestamp(now))
    
    for f in fam:
        day = database.child('Fingerprints').child(f.id).set(
            {
            'id': str(f.id),
            'last_authentication': timestamp,
        }
    )
    return HttpResponse("Ok")

def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'sick':'inkorora'}
    return render(request,'patients/test.html',context )



def patients(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    context={"name":"ilunga gisa dnaiel"}
    return HttpResponse('patients/patients.html')
def patient(request,pk):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    
    return HttpResponse('patients/patients.html')


@login_required(login_url='users:login')
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

@login_required(login_url='users:login')
def household(request,pk):
    try:
        household = Patriarch.objects.get(id=pk)
        household_members=household.family_set.all()
    except:
        messages.error(request, "Unknown Household")
        return redirect('patients:household_search')

    context={"household":household,'members':household_members}
    return render(request,'patients/household.html',context)




@login_required(login_url='users:login')
def household_member(request,pk):
    try:
        member = Family.objects.get(id=pk)
    except:
        messages.error(request, "Invalid Family Member, Make sure you select the correct Family Member")
        return redirect('patients:household_search')

    context={"member":member}
    return render(request,'patients/household_member.html',context)

@login_required(login_url='users:login')
def processing(request):
    healthFaculty=request.user.profile.health_faculty
    processing = Processing.objects.filter(healthFaculty=healthFaculty)
    print(processing)
    context={"processing":processing}
    return render(request,'patients/processing_patients.html',context)


# async def make_request(pk):
#     start_time = time.time()
#     data_found = False
#     while time.time() - start_time < 60:
#         data = await database.child("Fingerprints").child(pk).get("last_authentication")
#         print(data.val())
#         await asyncio.sleep(1)



@csrf_exempt
def authenticate(request,pk):
    member = Family.objects.get(pk=pk)
    context = {"member": member,"time":int(datetime.timestamp(datetime.now()))}
    matchOcured = False
    
    print("POST Not")
    if request.body:
        print("POST Made")
        match=json.loads(request.body.decode('utf-8'))
        print(match.get("match_found"))
        if match.get('match_found')=="true" and not matchOcured:
            matchOcured=True
            try:
                messages.success(request, "User Was Authenticated Successfully.")
                Processing.objects.create(patient=member,healthFaculty=request.user.profile.health_faculty)
            except:
                messages.success(request, "User Was Authenticated Successfully.")
        elif match.get('match_found')=="false" and not matchOcured:
            print("Failed Authentication")
            messages.error(request, "Unable To authenticate the user")
            return 
        else:
            print("Match problem")
    return render(request, 'patients/authenticating_patients.html',context)

def successfullAuthentication(request):
    messages.success(request, "User Was Authenticated Successfully.")
    return redirect('patients:processing')
def failedAuthentication(request,pk):
    messages.error(request, "Unable To authenticate the user")
    return redirect('patients:household_member',pk=pk)
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
        record = Invoice.objects.get(id=pk)
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
        patient = Processing.objects.get(patient=pk,healthFaculty=health_faculty)    
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
            messages.error(request, "Trying to add Medecine to the wrong patient, try again later")
            return redirect('patients:processing')

    context={"patient":patient,"invoiceForm":invoiceForm,"billForm":billForm}
    return render(request, "patients/create_invoice.html", context)

def records(request):
    health_faculty=request.user.profile.health_faculty
    invoice = Invoice.objects.filter(health_faculty=health_faculty)
    context={"invoice":invoice}
    return render(request,'patients/records.html',context)
