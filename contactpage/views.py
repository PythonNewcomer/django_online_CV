from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from contactpage.forms import ContactForm
from django.contrib import messages

def contactform(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['sender']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            recepients = ['omelinska@gmail.com']
            try:
                send_mail(subject, message, 'omelinska@gmail.com', recepients)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponseRedirect('success/')
        else:
            messages.warning(request, 'Invalid email address! Please, try again!')
            return render(request, 'contactme.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'contactme.html', {'form': form})


def success(request):
    messages.success(request, 'Thank you for email!')
    return render(request, 'contactme.html')
