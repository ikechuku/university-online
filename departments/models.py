from django.db import models
from django.core.urlresolvers import reverse

class Department(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_head = models.CharField(max_length=100)
    dept_capacity = models.IntegerField(default=250)
    dept_details = models.TextField(max_length=100, null=True)
    phone = models.CharField(max_length=50, default="+123 4567890")
    email = models.EmailField(max_length=254, default="dept@smart-school.com")
    start_date = models.CharField(max_length=100, default="1998")
        
    def get_absolute_url(self):
        return reverse('departments:dept_list')

    def __str__(self):
        return self.dept_name