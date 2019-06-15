from django.contrib.auth import get_user_model
from django import forms

from .models import Professor

class UserSignUp(forms.Form):
    username = forms.CharField(max_length=303, required=True, widget=forms.TextInput(attrs={"class":"input100", "placeholder":"Name"}))
    password = forms.CharField(max_length=30, required=True,widget=forms.PasswordInput(attrs={"class":"input100", "placeholder":"Password"}))
    confirm_password = forms.CharField(max_length=30, required=True,widget=forms.PasswordInput(attrs={"class":"input100", "placeholder":"Confirm Password", "data-placeholder": "&#xf191"}))

    def save(self, commit=True):
        User = get_user_model()
        instance = User.objects.create(username =self.cleaned_data.get('username'))
        print(instance)


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['gender', 'profile_pic', 'education', 'mobile_no','address']

    



class LoginUser(forms.Form):
    username = forms.CharField(max_length=303, required=True, widget=forms.TextInput(attrs={"class":"input100", "placeholder":"Name"}))
    password = forms.CharField(max_length=30, required=True,widget=forms.PasswordInput(attrs={"class":"input100", "placeholder":"Password"}))