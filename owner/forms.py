from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import business

class DateInput(forms.DateInput):
    input_type = 'date'

class BSignForm(UserCreationForm):
    email = forms.EmailField(label='Company Email', max_length=300, help_text='Required')

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "email": forms.EmailInput(attrs={
                'class': ''
            })}
        fields = ('email', 'password1', 'password2')

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

class BusinessForm(forms.ModelForm):
    class Meta:
        labels={
            'company_name': 'Company Name',
            'company_website': 'Company Website'
        }
        model = business
        fields =['company_name', 'company_website']
        widgets = {
            "company_website": forms.URLInput(attrs={
                'class': ''
            })}

class adCreate(forms.ModelForm):
    pass

