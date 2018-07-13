from django import forms
from .models import Request


class MessageForm(forms.ModelForm):
    class Meta:
        model = Request

        fields = [
            'name',
            'phoneNo',
            'email',
            'message'
        ]
