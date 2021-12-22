from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import business, advertisement, answer


class DateInput(forms.DateInput):
    input_type = 'date'


class BSignForm(UserCreationForm):
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
        fields = ["email"]
        widgets = {
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
        }
        labels = {
            "email": "Company Email",
        }

    def __init__(self, *args, **kwargs):
        super(BSignForm, self).__init__(*args, **kwargs)
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


class BusinessForm(forms.ModelForm):
    class Meta:
        labels = {
            'company_name': 'Company Name',
            'company_website': 'Company Website'
        }
        model = business
        fields = ['company_name', 'company_website']
        widgets = {
            "company_website": forms.URLInput(attrs={'class': 'form-control'}),
            "company_name": forms.TextInput(attrs={'class': 'form-control'}),
        }


class adCreateForm(forms.ModelForm):
    class Meta:
        model = advertisement
        fields = ['title', 'media_file', 'reward']
        labels = {
            'reward': 'Reward'
        }
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            'media_file': forms.FileInput(attrs={'class': 'form-control'}),
            'reward': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class responseForm(forms.ModelForm):
    class Meta:
        model = answer
        fields = ['opinion', 'rating']
        widgets = {
            "opinion": forms.Textarea(attrs={
                'class': 'form-control'
            }),
            "rating": forms.NumberInput(attrs={
                'class': 'form-control'
            }),
        }
