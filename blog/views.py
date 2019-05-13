from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse 

from . import forms 
# Create your views here.


def index(request):
    context = {
        'thang':'helloworld'
    }
    template = loader.get_template('blog/index.html')
    return HttpResponse(template.render(context, request))


def hello_forms(request):
    d = {
        'form':forms.SampleForm(),
    }
    # print(d['form']['gender_r'])
    return render(request, 'blog/forms.html', d)


def handle_forms(request):
    if request.method == 'POST':
        print('hello')
        print(request.POST.__dict__)
        print(request.POST['age'])
        print(request.POST['gender_s'])
        print(request.POST['send_message'])
        print(request.POST['birthday'])
        form = forms.SampleForm(data=request.POST)
        print(form.__dict__)
        if form.is_valid():
            print('Valid')
            pass 
        else:
            print('INvalid')
    return render(request, 'blog/index.html', {'name':form})