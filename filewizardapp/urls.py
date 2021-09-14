from filewizardapp.forms import ContactForm, ImageForm
from django.urls import path
from .views import imageView, FileWizard, home
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',FileWizard.as_view([ContactForm,ImageForm])),
    path('home/',home)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
