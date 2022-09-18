from this import d
from django.shortcuts import render, redirect
from .models import Console, Game
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import AccessoryForm

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
    games_console_doesnt_have = Game.objects.exclude(id__in = console.games.all().values_list('id'))
    accessory_form = AccessoryForm()
    return render(request, 'consoles/detail.html', { 
        'console' : console,
        'accessory_form': accessory_form,
        'games': games_console_doesnt_have
        })

class ConsoleCreate(CreateView):
    model = Console
    fields = '__all__'
    
class ConsoleUpdate(UpdateView):
    model = Console
    fields = ['description']

class ConsoleDelete(DeleteView):
    model = Console
    success_url = '/consoles/'

def add_accessory(request, console_id):
    form = AccessoryForm(request.POST)
    if form.is_valid():
        new_accessory = form.save(commit=False)
        new_accessory.console_id = console_id
        new_accessory.save()
    return redirect('detail', console_id=console_id)

class GameList(ListView):
  model = Game

class GameDetail(DetailView):
  model = Game

class GameCreate(CreateView):
  model = Game
  fields = '__all__'

class GameUpdate(UpdateView):
  model = Game
  fields = ['name', 'genre']

class GameDelete(DeleteView):
  model = Game
  success_url = '/games/'

def assoc_game(request, console_id, game_id):
    console = Console.objects.get(id = console_id)
    console.games.add(game_id)
    return redirect('detail', console_id = console_id)

def unassoc_game(request, console_id, game_id):
    console = Console.objects.get(id = console_id)
    console.games.remove(game_id)
    return redirect('detail', console_id = console_id)