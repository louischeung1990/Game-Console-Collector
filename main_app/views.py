from django.shortcuts import render
from .models import Console
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def consoles_index(request):
    consoles = Console.objects.all()
    return render(request, 'consoles/index.html', {'consoles' : consoles})

def console_detail(request, console_id):
    console = Console.objects.get(id=console_id)
    return render(request, 'consoles/detail.html', { 'console' : console })

class ConsoleCreate(CreateView):
    model = Console
    fields = '__all__'
    
class ConsoleUpdate(UpdateView):
    model = Console
    fields = ['description']

class ConsoleDelete(DeleteView):
    model = Console
    success_url = '/consoles/'
