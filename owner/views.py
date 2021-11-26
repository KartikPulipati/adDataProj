from django.shortcuts import render

# Create your views here.
def register_business(request):
    return render(request, 'rater/register_business.html')
