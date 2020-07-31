from django.forms import ModelForm
from ksm_app.models import Debatants, Judges, DebatantsBattle, PasswordJudges
from django import forms
from django.contrib.auth.models import User
from django import forms
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='Hasło')

    class Meta():
        model = User
        fields = ('username', 'password')
        labels = {
            'username': 'Nazwa użytkownika',
        }


class DebatantsProfileInfo(forms.ModelForm):
    organizacja = forms.CharField(required=False)
    opis = forms.CharField(required=False)
    terminy = forms.CharField(required=False,
                              label='Terminy sparingów (Preferowane)')
    accept = forms.BooleanField(required=True, label='Akceptuje Regulamin')
    accept2 = forms.BooleanField(required=True, label='')

    class Meta():
        model = Debatants
        fields = ['imię', 'nazwisko', 'email', 'miasto', 'szkoła', 'organizacja',
                  'facebook', 'opis', 'terminy', 'accept', 'accept2']
        labels = {
            'facebook': 'Profil Facebook',
        }


class JudgesProfileInfo(forms.ModelForm):
    organizacja = forms.CharField(required=False)
    dyspozycyjnosc = forms.CharField(required=False)
    opis = forms.CharField(required=False)
    accept = forms.BooleanField(required=True, label='Akceptuje Regulamin')
    accept2 = forms.BooleanField(required=True, label='')

    class Meta():
        model = Judges
        fields = ['imię', 'nazwisko', 'email', 'miasto', 'szkoła', 'organizacja',
                  'dyspozycyjnosc', 'opis', 'facebook', 'accept', 'accept2']
        labels = {
            'facebook': 'Profil Facebook',
            'dyspozycyjnosc': 'Dyspozycyjność'
        }


class JudgesForm(forms.ModelForm):
    dyspozycyjnosc = forms.CharField(required=False)
    opis = forms.CharField(required=False)
    organizacja = forms.CharField(required=False)

    class Meta:
        model = Judges
        fields = ['imię', 'nazwisko', 'email', 'miasto', 'szkoła', 'organizacja',
                  'dyspozycyjnosc', 'opis', 'facebook']


class DebatantsBattleForm(forms.ModelForm):
    data = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'RRRR-MM-DD'}))
    transmisja = forms.URLField(required=False)
    godzina = forms.TimeField(widget=forms.TextInput(attrs={'placeholder': 'gg:mm'}))

    class Meta:
        model = DebatantsBattle
        fields = ['user1', 'user2', 'judge', 'data', 'godzina', 'transmisja']


class TransmisionBattle(forms.ModelForm):
    class Meta:
        model = DebatantsBattle
        fields = ['transmisja']


class JudgesPassword(forms.ModelForm):
    haslo = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = PasswordJudges
        fields = ['haslo']


class DebatantsForm(forms.ModelForm):
    organizacja = forms.CharField(required=False)
    opis = forms.CharField(required=False)
    terminy = forms.CharField(required=False)

    class Meta:
        model = Debatants
        fields = ['imię', 'nazwisko', 'email', 'miasto', 'szkoła', 'organizacja',
                  'facebook', 'opis', 'terminy']
