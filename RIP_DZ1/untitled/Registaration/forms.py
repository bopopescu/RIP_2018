from django import forms
from django.contrib.auth.models import User
from LogIn.models import Profile
from django.contrib.auth.forms import  UserCreationForm
# from django.core.exceptions import ObjectDoesNotExist
# from django.utils.translation import ugettext_lazy as _
# from django.forms import ModelForm


class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="Repeat password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        strip=False
    )
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input', 'type': 'file'}),
                              required=False)
    about = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']
        if not avatar:
            return 'uploads/avatars/default.jpg'
        else:
            return avatar

    def clean_about(self):
        about = self.cleaned_data['about']
        if not about:
            return 'empty data'
        else:
            return about

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username']
        )
        user.set_password(self.cleaned_data['password1'])
        user.save()

        user_profile = Profile.objects.create(
            about=self.cleaned_data['about'],
            avatar=self.cleaned_data['avatar'],
            user=user
        )
        user_profile.save()
        return user_profile

    def get_user(self):
        return self.save().user


