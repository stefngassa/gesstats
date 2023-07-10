from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class UpdatePasswordForm(forms.Form):
    password = forms.CharField()
    confirm_password = forms.CharField()


class CountryForm(forms.ModelForm):
    class Meta:
        model = Pays
        exclude = ['date_updated']


class BrevetsForm(forms.ModelForm):
    class Meta:
        model = Brevets
        exclude = ['date_updated']


class DmiForm(forms.ModelForm):
    class Meta:
        model = DMI
        exclude = ['date_update']


class MarqueForm(forms.ModelForm):
    class Meta:
        model = Marques
        exclude = ['date_updated']


class DeleteDMIForm(forms.ModelForm):
    class Meta:
        model = DMI
        fields = ['type_dmi', 'annee_dmi']


class DeleteBrevetsForm(forms.ModelForm):
    class Meta:
        model = Brevets
        fields = ['type_brevets', 'annee_brevets']


class DeleteMarquesForm(forms.ModelForm):
    class Meta:
        model = Marques
        fields = ['type_marques', 'annee_marques']


class UploadPaysFileForm(forms.Form):
    file = forms.FileField()


class UploadPIFileForm(forms.Form):
    annee = forms.IntegerField()
    type_pi = forms.CharField()
    file = forms.FileField()


class ExportIFileForm(forms.Form):
    annee = forms.IntegerField()
    type_pi = forms.CharField()
    pi = forms.CharField()


class ExportEFileForm(forms.Form):
    annee = forms.IntegerField()
    type_pi = forms.CharField()
    pi = forms.CharField()
    file = forms.FileField()


class DashFilterForm(forms.Form):
    pi = forms.CharField()
    annee = forms.IntegerField()

