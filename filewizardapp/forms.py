from django import forms

class ImageForm(forms.Form):
    image1 = forms.ImageField()


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)