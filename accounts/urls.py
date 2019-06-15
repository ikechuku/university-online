from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    # signup
    url(r'^signup/', views.signup_view, name='sign_up'),

    # signin
    url(r'^login/', views.login_view, name='sign_in'),

     # logout
    url(r'^logout/', views.logout_view, name='logout'),

    # professor list
    url(r'^prof/', views.professor_list, name="prof_list"),

     # accounts/prof/add
    url(r'^prof/add/', views.ProfessorCreate.as_view(), name='add-prof'),

    # courses/course/2
     url(r'^prof/(?P<pk>[0-9]+)/$', views.ProfessorUpdate.as_view(), name='update-prof'),

    # courses/course/2/delete
     url(r'^prof/(?P<pk>[0-9]+)/delete', views.ProfessorDelete.as_view(), name='delete-prof'),

]