from django.conf.urls import url
from . import views

app_name = 'courses'

urlpatterns = [
    url(r'^$', views.courses_list, name="courses_list"),

    # courses/course/add
    url(r'add/', views.CourseCreate.as_view(), name='add-course'),

    # courses/course/2
     url(r'update-course/(?P<pk>[0-9]+)/$', views.CourseUpdate.as_view(), name='update-course'),

    # courses/course/2/delete
     url(r'delete-course/(?P<pk>[0-9]+)/delete', views.CourseDelete.as_view(), name='delete-course'),

]
