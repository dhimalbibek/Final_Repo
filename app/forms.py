from django import forms
from app.models import Infoss


class createForm(forms.ModelForm):
    class Meta:
        model =  Infoss
        fields =  '__all__'