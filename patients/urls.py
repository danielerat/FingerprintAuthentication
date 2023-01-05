from django.urls import path
from . import views
app_name = 'patients'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('patients/', views.patients, name='patients'),
    path('household/', views.household, name='household'),
    path('household/member/', views.household_member, name='household_member'),
    path('search/', views.household_serach, name='household_search'),
    

]