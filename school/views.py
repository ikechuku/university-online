from django.shortcuts import render

def prof(request):
    return render(request, 'professor_profile.html')

def sign_up(request):
    return render(request,'sign_up.html')


def sign_in(request):
    return render(request,'sign_in.html')

def home(request):
    return render(request, 'index.html')

def events(request):
    return render(request, 'events.html')

def classroom(request):
    return render(request, 'classroom.html')

def grade(request):
    return render(request, 'grade.html')

def student_signup(request):
    return render(request, 'student_signup.html')
    
def student_login(request):
    return render(request, 'student_login.html')

def student_page(request):
    return render(request, 'student_page.html')

def register_course(request):
    return render(request, 'register_course.html')


