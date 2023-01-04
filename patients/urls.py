from django.urls import path
from . import views
app_name = 'patients'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('patients/', views.patients, name='patients'),
    path('patient/<int:pk>/', views.patient, name='patient'),
    

]