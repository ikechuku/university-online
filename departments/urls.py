from django.conf.urls import url
from . import views

app_name = 'departments'

urlpatterns = [
    url(r'^$', views.dept_list, name="dept_list"),

    # departments/department/add
    url(r'add/', views.DepartmentCreateView.as_view(), name='add-dept'),

    # departments/department/2
     url(r'update/(?P<pk>[0-9]+)/$', views.DepartmentUpdateView.as_view(), name='update-course'),

    # departments/department/2/delete
     url(r'delete/(?P<pk>[0-9]+)/$', views.DepartmentDeleteView.as_view(), name='delete-course'),
]
 