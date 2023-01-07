from django.contrib import admin
from .models import Patriarch,Family,Prescription,Bill,Address
# Register your models here.
admin.site.register(Patriarch)
admin.site.register(Family)
admin.site.register(Bill)
admin.site.register(Prescription)
admin.site.register(Address)