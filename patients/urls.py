from django.urls import path
from . import views
app_name = 'patients'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]