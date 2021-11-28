import random
import string
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, RaterForm, RaterLoginForm
from .models import rater
from django.core.mail import EmailMessage
from adData import settings
from django.contrib.auth.decorators import login_required


code = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))

def signUp(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        rform = RaterForm(request.POST)
        if form.is_valid() and rform.is_valid():
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            birthday = rform.cleaned_data.get('birthday')
            gender = rform.cleaned_data.get('gender')
            user = User.objects.create_user(username=email, password=raw_password, email=email, first_name=first_name, last_name=last_name)
            user.save()
            p = rater(user=user, birthday=birthday, gender=gender, is_email_verified=False, credits=0)
            p.save()
            login(request, user)
            return redirect('emailVer')
    else:
        form = SignupForm()
        rform = RaterForm()
    return render(request, 'rater/signup.html', {'form': form, 'rform': rform})

@login_required
def emailVer(request):
    subject="Verification"
    message = f"{code}"
    email_from = settings.EMAIL_HOST_USER
    email_to = [request.user.email, ]
    print(request.user.email)
    msg = EmailMessage(
        subject,
        message,
        from_email=email_from,
        to=email_to,
    )
    msg.send(fail_silently=False)

    if request.method == 'GET':
        return render(request, 'rater/codeCheck.html')
    else:
        if request.POST['code'] == code:
            pro = rater.objects.get(user=request.user)
            pro.is_email_verified = True
            pro.save()
            return redirect('home')
        else:
            return render(request, 'rater/codeCheck.html', {'error': 'Code did not work, sent another code please check your email again!'})

def loginRater(request):
    if request.method == 'GET':
        return render(request, 'rater/loginuser.html', {'form': RaterLoginForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'rater/loginuser.html',
                          {'form': RaterLoginForm(), 'error': 'This User Does Not Exist, Please Try Again'})
        else:
            login(request, user)
            return redirect('home')

@login_required
def logoutRater(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
