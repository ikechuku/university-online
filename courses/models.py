from django.db import models
from django.core.urlresolvers import reverse

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=40)
    course_details = models.TextField()
    course_start_date = models.CharField(max_length=50)
    course_duration = models.CharField(max_length=30, default="3 months")
    course_max_students = models.IntegerField(default=200)
    # course_contact_no = models.IntegerField()
    profile_pic = models.ImageField(upload_to="courses")
    professor = models.CharField(max_length=50, default="Prof Jane Doe")

    def get_absolute_url(self):
        return reverse('courses:courses_list')

    def __str__(self):
        return self.course_name


