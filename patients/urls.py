from django.urls import path
from . import views
app_name = 'patients'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('patients/', views.patients, name='patients'),
    path('household/<str:pk>', views.household, name='household'),
    path('search/', views.household_serach, name='household_search'),
    

]