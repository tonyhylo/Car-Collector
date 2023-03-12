from django.forms import ModelForm
from . models import Washes

class WashingForm(ModelForm):
  class Meta:
    model = Washes
    fields = ['date', 'whereWashed']
