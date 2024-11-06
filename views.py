
# sms/views.py

from django.shortcuts import render, redirect
from django.conf import settings
from twilio.rest import Client
from .forms import SMSForm
from twilio.rest import Client

def send_sms(request):
    if request.method == 'POST':
        form = SMSForm(request.POST)
        if form.is_valid():
            to = form.cleaned_data['to']
            message = form.cleaned_data['message']

            # Twilio configuration
            TWILIO_ACCOUNT_SID = 'AC91448179326dddb98425989558ec4ad0'
            TWILIO_AUTH_TOKEN = '818e371c819c820ada42fedb1f2acc43'
            TWILIO_PHONE_NUMBER = '+19788481114'

            # Initialize Twilio client
            client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
            client.messages.create(
                body=message,
                from_='+19788481114',
                to='+919964711248'
            )
            

            return redirect('sms:success')
    else:
        form = SMSForm()

    return render(request, 'sms/send_sms.html', {'form': form})

def success(request):
    return render(request, 'sms/success.html')

# Create your views here.
