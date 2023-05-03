from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from app.forms import *

def register(request):
    tfo=TopicForm()
    wfo=WebpageForm()
    afo=AccessRecordForm()
    d={'tfo':tfo,'wfo':wfo,'afo':afo}

    if request.method=='POST':
        tfd=TopicForm(request.POST)
        wfd=WebpageForm(request.POST)
        afd=AccessRecordForm(request.POST)

        if tfd.is_valid() and wfd.is_valid() and afd.is_valid():
            NSTO=tfd.save(commit=False)
            NSTO.save()
            NSWO=wfd.save(commit=False)
            NSWO.topic_name=NSTO
            NSWO.save()
            NSAO=afd.save(commit=False)
            NSAO.name=NSWO
            NSAO.save()
            return HttpResponse('Registration is Successfully')

        else:
            return HttpResponse('In Valid')
    return render(request,'register.html',d)