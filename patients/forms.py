from django.forms import ModelForm
from django import forms
from .models import Invoice,Bill


class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = ['exams','medecines','procedures','others']
        
class BillForm(ModelForm):
    class Meta:
        model = Bill
        fields = ["consultation_fee","exams_fee","procedures_fee","medecines_fee","others_fee"]
        
    