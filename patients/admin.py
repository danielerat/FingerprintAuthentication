from django.contrib import admin
from .models import Patriarch,Family,Prescription,Bill,Address,Processing,HealthClass
# Register your models here.
admin.site.register(Patriarch)
admin.site.register(Family)
admin.site.register(Bill)
admin.site.register(Prescription)
admin.site.register(Address)
admin.site.register(Processing)
admin.site.register(HealthClass)