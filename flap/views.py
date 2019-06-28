from django.shortcuts import render, redirect
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext


from django.template.context_processors import csrf

from .forms import signinForm, specialForm, eventsForm, organizationForm, special_secondForm, organization_secondForm, activationForm
from .models import special, organization, events, special_second, organization_second, activation_tbl

from twilio.rest import Client
import string
import random

def home(request):
    if request.method == "POST":
        pass
    else:
        return HttpResponse("The home is loaded.")

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

def special_(request):
    if request.method == "POST":
        form = specialForm(request.POST)
        if form.is_valid():
            all_special = special.objects.all()
            for data in all_special:
                if request.POST['username'] == data.username:
                    return HttpResponse("The username is already reserved.")
                if request.POST['phone'] == str(data.phone):
                    return HttpResponse("The phone is already reserved.")
            key = ''
            session_key = ''
            all_digits = string.digits
            all_char = string.ascii_letters
            for a in range(5):
                key = key + all_digits[random.randrange(10)]
                session_key = session_key + all_char[random.randrange(52)]
            send_sms(key)
            form.save()
            request.session['activation_key'] = session_key
            spcl = special.objects.get(username = request.POST['username'])
            a = activation_tbl(special_id = spcl.id , session_key = session_key, mobile_key = key)
            a.save()
            request.session['usr_identity'] = 'usr' + request.POST['username']
            print(request.session['usr_identity'])
        return redirect("/activation/special")
    else:
        form = specialForm()
        dict = {'form': form}
        dict.update(csrf(request))
        return render_to_response('signupForm.html', dict, RequestContext(request))

def events_(request):
    if request.method == "POST":
        print(request.session['organization_name'])
        name = request.session['organization_name']
        form = eventsForm(request.POST)
        if form.is_valid():
            obj = organization.objects.get(organization = name)
            instance = form.save(commit = False)
            instance.organization = obj
            instance.save()
        return HttpResponse("The event was added.")
    else:
        form = eventsForm()
        dict = {'form': form}
        dict.update(csrf(request))
        return render_to_response('signupForm.html', dict, RequestContext(request))

def organization_(request):
    if request.method == "POST":
        form = organizationForm(request.POST)
        if form.is_valid():
            request.session['org_identity'] = request.POST['organization']
            all_org = organization.objects.all()
            for data in all_org:
                if request.POST['organization'] == data.organization:
                    return HttpResponse("The username is already reserved.")
                if request.POST['phone'] == str(data.phone):
                    return HttpResponse("The phone is already reserved.")
            form.save()
            key = ''
            session_key = ''
            all_digits = string.digits
            all_char = string.ascii_letters
            for a in range(5):
                key = key + all_digits[random.randrange(10)]
                session_key = session_key + all_char[random.randrange(52)]
            send_sms(key)
            request.session['activation_key'] = session_key
            org = organization.objects.get(organization = request.POST['organization'])
            a = activation_tbl(organization = org , session_key = session_key, mobile_key = key)
            a.save()
        return redirect("/activation/organization")
    else:
        form = organizationForm()
        dict = {'form': form}
        dict.update(csrf(request))
        return render_to_response('signupForm.html', dict, RequestContext(request))

def organization_second(request):
    if request.method == "POST":
        form = organization_secondForm(request.POST)
        if form.is_valid():
            print(request.POST['user'])
            print(request.session['org_identity'])
            if request.POST['user'][3:] == request.session['org_identity']:
                del request.session['org_identity']
                print(request.POST['user'])
                a = request.POST['user']
                ft = organization.objects.get(organization = a[3:])
                obj = form.save(commit = False)
                obj.organization = ft
                request.session['organization_name'] = a[3:]
                print(request.session['organization_name'])
                obj.save()
                return redirect('/home')
            else:
                return HttpResponse("Cross Site Request Frogery Detected.")
        else:
            print(form.errors)
            return HttpResponse("Form validation failed. Check loga for more detail.")
    else:
        user = 'org'+request.session['org_identity']
        form = organization_secondForm()
        dict = {'form': form, 'user': user}
        dict.update(csrf(request))
        return render_to_response('signupForm_second.html', dict, RequestContext(request))

def special_second(request):
    if request.method == "POST":
        form = special_secondForm(request.POST)
        if form.is_valid():
            if request.POST['user'] == request.session['usr_identity']:
                del request.session['usr_identity']
                ft = special.objects.get(username = request.POST['user'][3:])
                obj = form.save(commit = False)
                obj.special = ft
                obj.save()
                return redirect('/home')
            else:
                return HttpResponse("Cross Site Request Frogery Detected.")
        else:
            print(form.errors)
            return HttpResponse("Form validation failed. Check loga for more detail.")
    else:
        form = special_secondForm()
        user = request.session['usr_identity']
        dict = {'form': form,'user': user}
        dict.update(csrf(request))
        return render_to_response('signupForm_second.html', dict, RequestContext(request))

def activation(request, redirection_code):
    if request.method == "POST":
        form = activationForm(request.POST)
        if form.is_valid():
            code = request.POST['code']
            session_key = request.session['activation_key']
            obj = activation_tbl.objects.get(session_key = session_key)
            if obj.mobile_key == code:
                if redirection_code == 'special':
                    obj.special.activated = True
                    obj.special.save()
                    return redirect('special_second')
                elif redirection_code == 'organization':
                    obj.organization.activated = True
                    obj.organization.save()
                    return redirect('organization_second')
            else:
                return HttpResponse("Wrong key inserted.")
        else:
            print(form.errors)
            return HttpResponse("Activation code failed. Check logs for more details")
    else:
        form = activationForm()
        dict = {'form': form}
        dict.update(csrf(request))
        return render_to_response("activation_form.html", dict,RequestContext(request))


def send_sms(message):
    account_sid = 'ACcf401c612d39d28e0d1e374ef541df27'
    auth_token = '7eb29117c4053bedddac350df49aafec'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body= message,
                         from_='+12055649922',
                         to='+9779819604815'
                     )

    print(message.sid)
