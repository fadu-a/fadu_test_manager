from django import forms
from .models import TestCases


class PostForm(forms.ModelForm):

    class Meta:
        model = TestCases()
        fields = ('Title', 'Description', 'Configs', )