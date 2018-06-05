from django.utils.safestring import mark_safe
from django import forms

from django.forms.widgets import RadioSelect

RADIO_CHOICES = [['1','Radio 1'],['2','Radio 2']]


class TestForm(forms.Form):
    radio = forms.ChoiceField( widget=RadioSelect(), choices=RADIO_CHOICES)


class _TestForm(forms.Form):
    CHOICES= [('select1','select 1'), ('select2','select 2')]
    like = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
