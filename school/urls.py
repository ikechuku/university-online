from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


app_name = 'school'

urlpatterns = [
    # admin
    url(r'^admin/', admin.site.urls),
   
    # signup
    url(r'^signup/', views.sign_up, name='sign_up'),

    # signin
    url(r'^signin/', views.sign_in, name='sign_in'),

    # professor_profile
    url(r'^profile/', views.prof, name='prof'),

    
    # departments
    url(r'^departments/', include('departments.urls')),

    # courses
    url(r'^courses/', include('courses.urls')),

    # single pages
    url(r'^$', views.home, name='home'),
    url(r'^events$', views.events, name='events'),
    url(r'^grade$', views.grade, name='grade'),
    url(r'^classroom$', views.classroom, name='classroom'),
    url(r'^student$', views.student_signup, name='student_signup'),
    url(r'^students$', views.student_login, name='student_login'),
    url(r'^studenthome$', views.student_page, name='student_page'),
    url(r'^register-course$', views.register_course, name='register_course'),
]



urlpatterns += staticfiles_urlpatterns()


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)