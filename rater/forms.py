from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import rater

class DateInput(forms.DateInput):
    input_type = 'date'

class SignupForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password', 'align': 'center', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Re-enter password'}),
    )

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')
        widgets={
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "first_name": forms.TextInput(attrs={'class': 'form-control'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

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
        widgets = {'birthday': DateInput(attrs={'class': 'form-control'}),
                   'gender': forms.Select(attrs={'class': 'form-control'}),
                   }
        model = rater
        fields =['birthday', 'gender']

class RaterLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Email', 'id': 'username'}))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Password',
            'id': 'password',
        }
    ))
