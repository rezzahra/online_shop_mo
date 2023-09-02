from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import User


class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password1', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password2', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'full_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('password does not match')
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            return user.save()
        return user


class CustomUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text='you can change password using <a href= \"../password/\"> this form </a>')

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'full_name', 'password', 'last_login')


class UserRegisterForm(forms.Form):
    email = forms.EmailField()
    full_name = forms.CharField(label='full name')
    phone = forms.CharField(max_length=11, min_length=11)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('this email is already exists')
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        user = User.objects.filter(phone_number=phone).exists()
        if user:
            raise ValidationError('this phone number is already exists')
        return phone


class UserVerifyCodeRegisterForm(forms.Form):
    code = forms.IntegerField()
