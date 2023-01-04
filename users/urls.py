from django.urls import path
from . import views

app_name = 'users'


urlpatterns = [
    path('', views.login_user, name='login'),
    # path('logout/', views.logout_user, name='logout'),
    # path('register/', views.register_user, name='register'),
    # path('account/', views.user_account, name='account'),
    # path('edit_account/', views.edit_account, name='edit_account'),

    # path('add_skill/', views.add_skill, name='add_skill'),
    # path('edit_skill/<str:pk>', views.edit_skill, name='edit_skill'),
    # path('delete_skill/<str:pk>', views.delete_skill, name='delete_skill'),

    # path('inbox/', views.inbox, name='inbox'),
    # path('read_message/<str:pk>', views.message, name='message'),
    # path('send_message/<str:pk>', views.send_message, name='send_message'),
   
    # path('profile/<str:pk>', views.user_profile, name='user_profile'),

]
