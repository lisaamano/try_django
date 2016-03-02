# -​*- coding: utf-8 -*​-
from django.shortcuts import render
from .forms import SignUpModelForm


def home(request):
    title = 'Welcome'
    form = SignUpModelForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    if request.user.is_authenticated():
        title = 'Hello %s' % (request.user)
# .is_authenticated(): 管理者
    context = {
        'title': title,
        'form': form,
    }

    return render(request, 'home.html', context)
