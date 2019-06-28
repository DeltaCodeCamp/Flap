from django import forms
from .models import special, events, organization, special_second, organization_second



class specialForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = special
        fields = ['username', 'password', 'phone']

class eventsForm(forms.ModelForm):
    info = forms.CharField(widget = forms.Textarea)
    class Meta:
        model = events
        exclude = ['activated', 'organization']

class organizationForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = organization
        exclude = ['activated', 'info']

class organization_secondForm(forms.ModelForm):
    class Meta:
        model = organization_second
        fields =  ['minimum_age', 'maximum_age', 'activities', 'disability', 'info']

class special_secondForm(forms.ModelForm):
    bio = forms.CharField(widget = forms.Textarea)
    class Meta:
        model = special_second
        fields =['age', 'bio', 'activities', 'disability']

class signinForm(forms.Form):
    username = forms.CharField(max_length = 200)
    password = forms.CharField(widget= forms.PasswordInput(), max_length = 100)

class activationForm(forms.Form):
    code = forms.CharField(max_length = 5)
