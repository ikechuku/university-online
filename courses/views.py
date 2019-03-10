from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Course

def courses_list(request):
    courses = Course.objects.all().order_by('course_code')
    return render(request,'courses/all_courses.html', {'courses':courses})


class CourseCreate(CreateView):
    model = Course
    fields = ['course_name', 'course_code', 'course_details','course_duration']


class CourseUpdate(UpdateView):
    model = Course
    fields = ['course_name', 'course_code', 'course_details','course_duration']

class CourseDelete(DeleteView):
    model = Course
    success_url = reverse_lazy('courses:courses_list')
    

