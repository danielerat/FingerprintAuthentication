from django.contrib import admin
from .models import Patriarch,Family,Invoice,Bill,Address,Processing,HealthClass
# Register your models here.
admin.site.register(Patriarch)

admin.site.register(Bill)
admin.site.register(Address)
admin.site.register(Processing)
admin.site.register(HealthClass)




@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display=["id","chief","nationalId","firstName","lastName","dob","sex","email","phone"]
    search_fields = ['nationalId',"firstName","lastName","phone" ]

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['patient','health_faculty','bill','exams','medecines','procedures','others','date','id']
    list_per_page = 10
    search_fields = ['patient__firstName','health_faculty__name' ]