from django import forms
from .models import SignUp


class SignUpModelForm(forms.ModelForm):

    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

        
