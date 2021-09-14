from djangowizardapp.forms import ContactForm, ContactForm2
from django.urls import path
from .views import ContactWizard, index

urlpatterns = [
    path('',index),
    path('contact/',ContactWizard.as_view([ContactForm,ContactForm2])),
]
