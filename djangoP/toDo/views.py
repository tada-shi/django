from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import toDOItem

# Create your views here.
def home(request):
    items = toDOItem.objects.all()
    return render(request, "toDo.htm", {'items' : items})

def addToDo(request):
    text = toDOItem(text = request.POST['text'])
    text.save()
    return HttpResponseRedirect('/')

def delToDo(request, toDo_id):
    item = toDOItem.objects.get(id=toDo_id)
    item.delete()
    return HttpResponseRedirect('/')
