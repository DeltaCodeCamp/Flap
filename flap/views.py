from django.shortcuts import render, redirect
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext


from django.template.context_processors import csrf

from .forms import signinForm, specialForm, eventsForm, organizationForm, special_secondForm, organization_secondForm
def signin(request):
    if request.method == "POST":
        form = signinForm(request.POST)
        if form.is_valid():
            print(request.POST)
        return HttpResponse("You have got to do some work dude.")
    else:
        form = signinForm()
        dict = {'form': form}
        dict.update(csrf(request))
        return render_to_response('signinForm.html', dict, RequestContext(request))

def special(request):
    if request.method == "POST":
        form = specialForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/special_second")
    else:
        form = specialForm()
        dict = {'form': form}
        dict.update(csrf(request))
        return render_to_response('signupForm.html', dict, RequestContext(request))

def events(request):
    if request.method == "POST":
        form = eventsForm(request.POST)
        if form.is_valid():
            form.save()
        return
    else:
        form = eventsForm()
        dict = {'form': form}
        dict.update(csrf(request))
        return render_to_response('signupForm.html', dict, RequestContext(request))

def organization(request):
    if request.method == "POST":
        form = organizationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/organization_second")
    else:
        form = organizationForm()
        dict = {'form': form}
        dict.update(csrf(request))
        return render_to_response('signupForm.html', dict, RequestContext(request))

def organization_second(request):
    if request.method == "POST":
        form = organization_secondForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
            return HttpResponse("Form validation failed. Check loga for more detail.")
    else:
        form = organization_secondForm()
        dict = {'form': form}
        dict.update(csrf(request))
        return render_to_response('signupForm.html', dict, RequestContext(request))

def special_second(request):
    if request.method == "POST":
        form = special_secondForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
            return HttpResponse("Form validation failed. Check loga for more detail.")
    else:
        form = special_secondForm()
        dict = {'form': form}
        dict.update(csrf(request))
        return render_to_response('signupForm.html', dict, RequestContext(request))
