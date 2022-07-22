from django.forms import ModelForm
from .models import ProgressUpdate

class ProgressUpdateForm(ModelForm):
  class Meta:
    model = ProgressUpdate
    fields = ['date', 'name', 'description']