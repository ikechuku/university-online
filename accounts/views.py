from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import View
from . import forms
from .models import Professor
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# ClassBasedVies for Create, Update and Delete
class ProfessorCreate(LoginRequiredMixin, CreateView):
    model = Professor
    fields = ['user', 'bio', 'gender','address',"profile_pic", 'education']
    login_url = '/accounts/login'


class ProfessorUpdate(LoginRequiredMixin, UpdateView):
    model = Professor
    fields =['user.email', 'bio', 'gender','address',"profile_pic", 'education']
    login_url = '/accounts/login'

class ProfessorDelete(LoginRequiredMixin, DeleteView):
    model = Professor
    success_url = reverse_lazy('accounts:prof_list')
    login_url = '/accounts/login'

# Register new Professor
def signup_view(request):
    
    if request.method == 'POST':
        form = forms.UserSignUp(request.POST)
        p_form = forms.ProfessorForm(request.POST)
        # validate form data and log the user in
        if form.is_valid() and p_form.is_valid():
            form.save()
            p_form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #TODO log the user in
            USER = get_user_model()
            user = USER.objects.get(username = username)
            login(request, user)
            return redirect('courses:courses_list')

    else:
        form = forms.UserSignUp()
    return render(request, 'accounts/registration_form.html', {'form':form}) 

# Login as Professor
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('courses:courses_list')

    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html', {'form':form})

# Logout
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
# List all Professors
def professor_list(request):
    profs = Professor.objects.all()
    return render(request,'accounts/all_professors.html', {'profs':profs})

    

