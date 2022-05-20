from django.shortcuts import render
from .models import Wish
from django.views.generic.edit import CreateView, DeleteView
# Create your views here.

def home(request):
    wishes = Wish.objects.all()
    return render(request, 'home.html', {'wishes': wishes})

class CreateWish(CreateView):
    model = Wish
    fields = '__all__'
    success_url = '/'

class DeleteWish(DeleteView):
    model = Wish
    success_url = '/'