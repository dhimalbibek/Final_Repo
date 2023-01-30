from django.shortcuts import render
from app.models import Infoss
from app.forms import createForm
from django.http import HttpResponseRedirect

# Create your views here.
def homePage(request):
    home = Infoss.objects.all()
    return render(request, 'home.html', {'home': home})

def read(request, id):
    r = Infoss.objects.get(id=id)
    return render(request, 'read.html', {'Infoss': r}  )

def form_page(request):
    context = {}
    form = createForm(data=request.POST or None, files=request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    context = {
            'form' : form
        }
    return render (request, 'create.html', context)

def update_form(request, id):
    content = {

    }
    up = Infoss.objects.get(id=id)
    form = createForm(request.POST or None, instance=up)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    content ={
        'form': form
    }
    return render(request, 'create.html', content)

def delete_page(request,id):
    if request.method =="POST":
        dd = Infoss.objects.get(id=id)
        dd.delete()
        return HttpResponseRedirect('/')
    return render(request, 'delete.html', {'id':id})
