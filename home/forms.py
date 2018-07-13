from django import forms
from .models import Careers


class InternshipForm(forms.ModelForm):
    class Meta:
        model = Careers

        fields = ['full_name', 'email',
                  'facebook', 'twitter',
                  'linkedin', 'instagram',
                  'interests', 'extracurriculars',
                  'department']