from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import ContactForm, ContactForm2
from .models import FormData
from formtools.wizard.views import SessionWizardView
# Create your views here.

def index(request):
    return HttpResponse("Index page")\


def saveDB(fname,lname,email):
    data = FormData(fname=fname,lname=lname,email=email)
    data.save()


class ContactWizard(SessionWizardView):
    template_name = "wizardtemp.html"
    form_list = [ContactForm,ContactForm2]

    def done(self,form_list,**kwargs):
        formdata = []
        for data in form_list:
            formdata.append(data)

        datas = [form.cleaned_data for form in form_list]
     
        fname = datas[0]['fname']
        lname = datas[0]['lname']
        email = datas[1]['email']

        saveDB(fname,lname,email)

        return render(self.request,'done.html',{
            'form_data': datas
        })

