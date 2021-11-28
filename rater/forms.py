from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import rater

class DateInput(forms.DateInput):
    input_type = 'date'

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=300, help_text='Required')
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name')

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email is already in use.')

class RaterForm(forms.ModelForm):
    class Meta:
        widgets = {'birthday': DateInput(attrs={'class': ''})}
        model = rater
        fields =['birthday', 'gender']

class RaterLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': '', 'placeholder': 'Enter Email', 'id': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': '',
            'placeholder': 'Enter Password',
            'id': 'password',
        }
    ))
