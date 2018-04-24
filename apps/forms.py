from django import forms
from .models import Test_cases

class NewForm(forms.ModelForm):
    class Meta:
        model = Test_cases
        fields = ('title', 'description', 'configs')
