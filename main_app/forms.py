from django.forms import ModelForm
from .models import Force

class ForceForm(ModelForm):
  class Meta:
    model = Force
    fields = ['force_side']