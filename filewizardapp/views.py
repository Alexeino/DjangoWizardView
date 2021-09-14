from filewizardapp.models import ImageModel
from django.http.response import HttpResponse
from django.shortcuts import render
from formtools.wizard.views import SessionWizardView
from .forms import ImageForm, ContactForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os


# Create your views here.

def imageView(request):
    return HttpResponse("Image View")

def saveData(name,image):
    data = ImageModel(name=name,image=image)
    data.save()

class FileWizard(SessionWizardView):
    template_name = "imagewizard.html"
    form_list = [ContactForm,ImageForm]

    file_storage= FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT,'photos'))

    def done(self,form_list,**kwargs):
        
        datas = [form.cleaned_data for form in form_list]
        name = datas[0]['name']
        image = datas[1]['image1']

        saveData(name,image)

        
        return render(self.request,'done.html',{
            'form_data': [form.cleaned_data for form in form_list]
        })

def home(request):
    data = ImageModel.objects.all()

    context={
        'data':data
    }
    return render(request,'home.html',context)