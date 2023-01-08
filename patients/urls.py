from django.urls import path
from . import views
app_name = 'patients'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('fire/', views.update_firebase, name='fire'),
    path('patients/', views.patients, name='patients'),
    path('household/<str:pk>', views.household, name='household'),
    path('household/member/<str:pk>', views.household_member, name='household_member'),
    path('search/', views.household_serach, name='household_search'),
    path('records/', views.records, name='records'),
    path('processing/', views.processing, name='processing'),
    path('deleteProcessing/<str:pk>', views.deleteProcessingPatient, name='delete_processing_patient'),
    path('delete_recorded_patient/<str:pk>', views.delete_recorded_patient, name='delete_recorded_patient'),
    path('authentication/<str:pk>', views.authenticate, name='hausehold_authentication'),
    path('create_invoice/<str:pk>', views.create_invoice, name='create_invoice'),

]