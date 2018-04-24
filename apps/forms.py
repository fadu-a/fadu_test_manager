from django import forms
from .models import TestCases


class NewForm(forms.ModelForm):
    class Meta:
        model = TestCases
        fields = ('title', 'description', 'configs')
