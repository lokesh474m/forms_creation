from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from app.forms import *

def forms(request):
    ENFO=NameForm()
    d={'ENFO':ENFO}

    if request.method=='POST':
        NFDO=NameForm(request.POST)
        if NFDO.is_valid():
            return HttpResponse(str(NFDO.cleaned_data))
            #return HttpResponse(NFDO.cleaned_data['Sname'])

        else:
            return HttpResponse('Data is not Valid')

    return render(request,'forms.html',d)