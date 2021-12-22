import random
import string
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import BSignForm, BusinessForm, adCreateForm
from .models import business
from rater.models import rater
from django.core.mail import EmailMessage
from adData import settings
from django.contrib.auth.decorators import login_required
from .models import advertisement
from django.contrib.auth.decorators import permission_required
from django.http import Http404


code = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))

def signupB(request):
    if request.user.is_authenticated:
        return redirect('home')

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
            p = business(user=user, company_name=company_name, company_website=company_website, is_email_verified=False)
            p.save()
            login(request, user)
            return redirect('emailVerB')
    else:
        form = BSignForm()
        rform = BusinessForm()
    return render(request, 'owner/signupB.html', {'form': form, 'rform': rform})


@login_required
def emailVerB(request):
    subject = "Verification"
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
            return render(request, 'owner/codeCheckB.html',
                          {'error': 'Code did not work, sent another code please check your email again!'})

@login_required
def adCreate(request):
    try:
        request.user.business
        if request.method == 'POST':
            form = adCreateForm(request.POST, request.FILES)
            if form.is_valid():
                name = form.cleaned_data.get('title')
                reward = form.cleaned_data.get('reward')
                media = form.cleaned_data.get('media_file')
                user = request.user.business
                ad = advertisement.objects.create(title=name, reward=reward, media_file=media, uploader=user)
                ad.save()
                return redirect('home')
        else:
            form = adCreateForm()
        return render(request, 'owner/adCreate.html', {'form': form})
    except:
        raise Http404

@login_required
def dashboard(request):
    try:
        items = advertisement.objects.filter(uploader=request.user.business)
        return render(request, 'owner/dashboard.html', {'items': items})
    except:
        raise Http404


