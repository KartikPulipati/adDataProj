from django.shortcuts import render, redirect, get_object_or_404
from owner.forms import responseForm
from django.contrib.auth.decorators import login_required
from owner.models import advertisement, answer
from django.contrib.auth.models import User

def home(request):
    return render(request, 'display/home.html')

@login_required
def viewAd(request, advertisement_pk):
    notThere = True
    ad = get_object_or_404(advertisement, pk=advertisement_pk)
    ans = answer.objects.filter(ad=ad)
    try:
        for i in ans:
            if i.user == request.user.rater:
                notThere = False
    except:
        pass
    if notThere:
        if request.method == 'POST':
            form = responseForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user.rater
                instance.ad = ad
                ad.num_views = ad.num_views + 1
                ad.save()
                request.user.rater.credits = request.user.rater.credits + ad.reward
                request.user.rater.save()
                instance.save()
                return redirect('discover')
        else:
            form = responseForm()
        return render(request, 'display/viewAd.html', {'form': form, 'ad': ad, 'ans': ans})
    return render(request, 'display/viewAd.html', {'ad': ad, 'ans': ans})
