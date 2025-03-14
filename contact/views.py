"""
Views for the contact app
"""
from django.shortcuts import render, redirect, reverse
# from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings
from .forms import EnquiryForm


def contact(request):
    """ Display the contact form and process enquiry. """

    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            # send enquiry to store owner by email
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            subject = render_to_string(
                'contact/enquiry_emails/enquiry_subject.txt',
                {'name': name})
            body = render_to_string(
                'contact/enquiry_emails/enquiry_body.txt',
                {
                    'name': name,
                    'email': email,
                    'phone_number': phone_number,
                    'message': message
                    }
                )
            EmailMessage(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.STORE_OWNER_EMAIL],
                [], reply_to=[email]
                ).send()
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
