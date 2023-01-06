from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile, Message
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm, MessageForm
# from .utils import search_profiles
# from projects.utils import custom_paginator


def login_user(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('patients:patients')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Unknown Username or Password")
            return render(request, 'registration/login_register.html')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'patients:household_search')
        else:
            messages.error(request, "Unknown Username Or Password")
    return render(request, 'registration/login_register.html')


def logout_user(request):
    logout(request)
    messages.info(request, "You were Logged Out Successfully")
    return redirect('users:login')


# Create your views here.
# def profiles(request):
#     profiles, search_query = search_profiles(request)

#     custom_range, profiles = custom_paginator(request, profiles, 6)

#     context = {'profiles': profiles, 'search_query': search_query, 'custom_range': custom_range}
#     return render(request, 'users/profiles.html', context)


# def user_profile(request, pk):
#     profile = get_object_or_404(Profile, pk=pk)

#     # All skills with description
#     top_skills = profile.skill_set.exclude(description__exact='')

#     # All Skills with no Description
#     other_skills = profile.skill_set.filter(description__exact='')

#     context = {'profile': profile, 'topSkills': top_skills, 'otherSkills': top_skills}
#     return render(request, 'users/user-profile.html', context)


# def register_user(request):
#     page = 'register'
#     form = CustomUserCreationForm()
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.username = user.username.lower()
#             user.save()
#             messages.success(request, "Account Successfully Created")
#             login(request, user)
#             return redirect('users:account')
#         else:
#             messages.error(request, "Error has Occurred during registration")

#     context = {'page': page, 'form': form}
#     return render(request, 'registration/login_register.html', context)


# @login_required(login_url='users:login')
# def user_account(request):
#     profile = request.user.profile

#     context = {'profile': profile}
#     return render(request, 'users/account.html', context)


# @login_required(login_url='users:login')
# def edit_account(request):
#     user = request.user.profile
#     form = ProfileForm(instance=user)
#     if request.method == "POST":
#         form = ProfileForm(request.POST, request.FILES, instance=user)
#         if form.is_valid():
#             updated = form.save()
#             messages.info(request, "%s Your Account Data Updated Successfully" % updated.username)
#             return redirect('users:account')
#     context = {'form': form}
#     return render(request, 'users/profile_form.html', context)


# @login_required(login_url='users:login')
# def add_skill(request):
#     form = SkillForm()
#     profile = request.user.profile

#     if request.method == 'POST':
#         form = SkillForm(request.POST)
#         if form.is_valid():
#             add = form.save(commit=False)
#             add.owner = profile
#             add.save()
#             messages.info(request, "Hey %s Your Skill was added successfully ! " % profile.first_name)
#             return redirect('users:add_skill')
#     context = {'form': form}
#     return render(request, 'users/skill_form.html', context)


# @login_required(login_url='users:login')
# def edit_skill(request, pk):
#     profile = request.user.profile
#     skill = profile.skill_set.get(id=pk)
#     form = SkillForm(instance=skill)
#     if request.method == 'POST':
#         form = SkillForm(request.POST, instance=skill)
#         if form.is_valid():
#             save = form.save()
#             messages.info(request, "Your Skill was added successfully ! ")
#             return redirect('users:account')
#     context = {'form': form}
#     return render(request, 'users/skill_form.html', context)


# @login_required(login_url='users:login')
# def delete_skill(request, pk):
#     profile = request.user.profile
#     skill = profile.skill_set.get(id=pk)
#     if request.method == 'POST':
#         skill.delete()
#         messages.success(request, "Hey %s, Your Skill was Deleted Successfully" % request.user.profile.first_name)
#         return redirect("users:account")
#     context = {'object': skill}
#     return render(request, "projects/delete_template.html", context)


# @login_required(login_url='users:login')
# def inbox(request):
#     profile = request.user.profile
#     msgs = profile.messages.all()
#     unread_count = msgs.filter(is_read=False).count()
#     context = {'msgs': msgs, 'unread_count': unread_count}
#     return render(request, 'users/inbox.html', context)


# @login_required(login_url='users:login')
# def message(request, pk):
#     profile = request.user.profile
#     msg = profile.messages.get(pk=pk)
#     if not msg.is_read:
#         msg.is_read = True
#         msg.save()
#     context = {'msg': msg}
#     return render(request, 'users/message.html', context)


# def send_message(request, pk):
#     form = MessageForm()
#     try:
#         sender = request.user.profile
#     except:
#         sender = None
#     receiver = get_object_or_404(Profile, id=pk)
#     if request.method == 'POST':
#         form = MessageForm(request.POST)
#         if form.is_valid():
#             msg = form.save(commit=False)
#             msg.sender = sender
#             msg.receiver = receiver
#             if sender:
#                 msg.first_name = sender.first_name
#                 msg.last_name = sender.last_name
#             msg.save()
#             messages.success(request, 'Your message was sent Successfully')
#             return redirect('users:user_profile', pk=receiver.id)
#     context = {'form': form, 'receiver': receiver}
#     return render(request, 'users/message_form.html', context)
