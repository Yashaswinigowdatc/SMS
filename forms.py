# sms/forms.py

from django import forms

class SMSForm(forms.Form):
    to = forms.CharField(max_length=15, label='To')
    message = forms.CharField(widget=forms.Textarea, label='Message')
