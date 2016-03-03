# -​*- coding: utf-8 -*​-
from django import forms
from .models import SignUp


class SignUpModelForm(forms.ModelForm):

    class Meta:
        model = SignUp
        fields = ['full_name', 'email']


class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email1 = forms.EmailField()
    email2 = forms.EmailField()
    message = forms.CharField()

    def clean_email2(self):
        email1 = self.cleaned_data.get("email1")
        email2 = self.cleaned_data.get("email2")

        if not email1 == email2:
            raise forms.ValidationError(
             "確認用メールと一致しないよ"
            )
        return email2
