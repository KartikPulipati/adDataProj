from django.forms import forms
from owner.models import Video

class UploadVideoForm(forms.ModelForm):
    class Meta:
        model = Video 
        fields = ['file', 'title', 'uploader', 'upload_date', 'num_views']