from django.forms import ModelForm
from .models import Inbox

class InboxForm(ModelForm):
    class Meta:
        model = Inbox
        fields = ['email','subject','message']
