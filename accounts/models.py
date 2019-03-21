from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=300, blank=True, default="Instructor")
    # Department = models.OneToOneField("departments.Department", on_delete=models.CASCADE )
    gender = models.CharField(max_length=10, default="Male")
    profile_pic = models.FileField(upload_to="Professors")
    mobile_no = models.CharField(max_length=30, blank=True)
    address = models.TextField(max_length=100, blank=True)
    education = models.TextField(max_length=130, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.user.email}'
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Professor.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.professor.save()


# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     Department = models.ForeignKey("departments.Department", on_delete=models.CASCADE)
#     gender = models.CharField(max_length=10)
#     profile_pic = models.FileField(upload_to="Students")
#     matric_no = models.CharField(max_length=50)
#     parents_name = models.CharField(max_length=50)
#     parents_contact = models.CharField(max_length=50)
#     address = models.TextField(max_length=130, blank=True)

#     def __str__(self):
#         return self.matric_no
    