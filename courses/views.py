from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Course
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def courses_list(request):
    courses = Course.objects.all().order_by('course_code')
    return render(request,'courses/all_courses.html', {'courses':courses})


class CourseCreate(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login'
    model = Course
    fields = ['course_name', 'course_code', 'course_details','course_duration',"profile_pic", "course_max_students",'professor']



class CourseUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login'
    model = Course
    fields = ['course_name', 'course_code', 'course_details','course_duration',"profile_pic", "course_max_students",'professor']


class CourseDelete(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login'
    model = Course
    success_url = reverse_lazy('courses:courses_list')
    

