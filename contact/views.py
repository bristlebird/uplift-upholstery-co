"""
Views for the contact app
"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# from .models import Enquiry
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import EnquiryForm


def contact(request):
    """ Display the contact form and process enquiry. """

    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            # send enquiry to store owner by email
            subject = render_to_string(
                'contact/enquiry_emails/enquiry_subject.txt',
                {'form': form})
            body = render_to_string(
                'contact/enquiry_emails/enquiry_body.txt',
                {'form': form})

            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL]
            )
            messages.success(request, 'Message sent successfully')
            return redirect(reverse('contact_success'))

        else:
            messages.error(request, 'Message delivery failed. \
                           Please ensure the form is valid.')
    else:
        form = EnquiryForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def contact_success(request):
    """
    Render thank you / success page after successful contact enquiry
    form submission
    """
    return render(request, 'contact/contact_success.html')
