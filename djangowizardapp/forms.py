from django import forms

class ContactForm(forms.Form):
    fname = forms.CharField(max_length=100)
    lname = forms.CharField(max_length=100)


class ContactForm2(forms.Form):
    email = forms.EmailField()

