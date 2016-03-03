# -​*- coding: utf-8 -*​-
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import SignUpModelForm, ContactForm


def home(request):
    title = 'Welcome'
    form = SignUpModelForm(request.POST or None)
    # request と formの意味は？？

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

        # ↑の意味は？？

    if request.user.is_authenticated():
        title = 'Hello %s' % (request.user)
# .is_authenticated(): 管理者
    context = {
        'title': title,
        'form': form,
    }

    return render(request, 'home.html', context)


def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form_email = form.cleaned_data.get("email1")
        form_message = form.cleaned_data.get("message")
        form_name = form.cleaned_data.get("full_name")
        subject = 'コンタクトページからメッセージが届いたよ'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email]
        contact_message = "%s: %s via %s" % (
            form_name,
            form_message,
            form_email,
        )
        send_mail(subject, contact_message, from_email, to_email, fail_silently=True)

        # ％の意味は？

    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)
