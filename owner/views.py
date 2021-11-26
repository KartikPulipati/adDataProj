from django.shortcuts import render
from django.shortcuts import HttpResponse
from owner.forms import UploadVideoForm

# Create your views here.
def register_business(request):
    return render(request, 'rater/register_business.html')

def upload_video(request):
    if request.method == 'POST':
        form = UploadVideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('The file is saved')
    else:
        form = UploadVideoForm()
        context = {
            'form': form
        }
    return render(request, 'UploadVideo.html', context)

