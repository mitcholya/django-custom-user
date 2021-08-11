from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser
from django.contrib.auth.models import User
from .models import Profile

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


"""Кастомный логин форм"""
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

"""Форма для регистрации"""
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                            widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ( 'email',)
        
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

"""Форма для редоктирования Юзера ЭЭЭ"""
class UserEditForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('email',)
        
"""Форма для редоктирования профиля"""
class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('first_name', 'surname', 'last_name','date_of_birth', 'photo')

class ProfileCreateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('first_name', 'surname', 'last_name','date_of_birth', 'photo')