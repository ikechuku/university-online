from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Department
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def dept_list(request):
    depts = Department.objects.all().order_by('id')
    return render(request,'departments/all_depts.html', {'depts':depts})

class DepartmentCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login'
    model = Department
    fields = ['dept_name', 'dept_head', 'dept_capacity', 'phone', 'email', 'start_date','dept_details']   

class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login'
    model = Department
    fields = ['dept_name', 'dept_head', 'dept_capacity', 'phone', 'email', 'start_date','dept_details'] 


class DepartmentDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login'
    model = Department
    success_url = reverse_lazy('departments:dept_list')

