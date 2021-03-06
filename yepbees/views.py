import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.conf import settings

#email
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import EmailMessage
from .forms import ContactForm
from django.contrib import messages
from django.conf import settings
# reCAPTCHA
import urllib
import json
import urllib.request

def home_page(request):
    return render(request, 'home_page.html')

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():

            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''

            if result['success']:
                name = form.cleaned_data['subject']
                from_email = form.cleaned_data['from_email']
                message_text = form.cleaned_data['message']
                number = form.cleaned_data['contact_phone']
                subject = "Customer enquiry - Yep Bees: " + name

                message = (
                    "From: " + name +
                    "<br>Email: " + from_email +
                    "<br>Phone: " + number +
                    "<br><br> Message: " + message_text
                    )
                msg = EmailMessage(subject, message, from_email, ['yepbees@gmail.com'],)
                msg.content_subtype = "html"

                try:
                    msg.send()
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                messages.success(request, 'Success! Thank you for your message.')
                return redirect('contact')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                return redirect('contact')
    return render(request, "contact.html", {'form': form})
