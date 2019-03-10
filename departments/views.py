from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Department

def dept_list(request):
    depts = Department.objects.all().order_by('dept_name')
    return render(request,'departments/all_depts.html', {'depts':depts})

class DepartmentCreateView(CreateView):
    model = Department
    fields = ['dept_name', 'dept_head', 'dept_capacity', 'phone', 'email', 'start_date','dept_details']   

class DepartmentUpdateView(UpdateView):
    model = Department
    fields = ['dept_name', 'dept_head', 'dept_capacity','dept_details']   


class DepartmentDeleteView(DeleteView):
    model = Department
    success_url = reverse_lazy('departments:dept_list')

