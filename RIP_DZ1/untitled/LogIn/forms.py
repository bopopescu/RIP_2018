from django import forms
from .models import Profile as pModel
from django.forms import ModelForm


class Profile(ModelForm):
    class Meta:
        model = pModel
        fields = ('about','avatar')
        widgets = {
            'about': forms.TextInput(attrs={'class': 'about'})
            # 'avatar': forms.TextInput(attrs={'class': 'avatar'})
        }
