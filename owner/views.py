import random
import string
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import BSignForm, BusinessForm
from .models import business
from django.core.mail import EmailMessage
from adData import settings
from django.contrib.auth.decorators import login_required


code = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))

def signupB(request):
    if request.method == 'POST':
        form = BSignForm(request.POST)
        rform = BusinessForm(request.POST)
        if form.is_valid() and rform.is_valid():
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            company_name = rform.cleaned_data.get('company_name')
            company_website = rform.cleaned_data.get('company_website')
            user = User.objects.create_user(username=email, password=raw_password, email=email)
            user.save()
            p = business(user=user, company_name=company_name, company_website=company_website, is_email_verified=False, credits=0)
            p.save()
            login(request, user)
            return redirect('emailVer')
    else:
        form = BSignForm()
        rform = BusinessForm()
    return render(request, 'owner/signupB.html', {'form': form, 'rform': rform})

@login_required(redirect_field_name='loginRater')
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
        return render(request, 'owner/codeCheckB.html')
    else:
        if request.POST['code'] == code:
            pro = business.objects.get(user=request.user)
            pro.is_email_verified = True
            pro.save()
            return redirect('home')
        else:
            return render(request, 'owner/codeCheckB.html', {'error': 'Code did not work, sent another code please check your email again!'})





