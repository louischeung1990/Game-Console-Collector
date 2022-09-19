from django.shortcuts import render, redirect
from .models import Console, Game
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import AccessoryForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def consoles_index(request):
    consoles = Console.objects.filter(user=request.user)
    return render(request, 'consoles/index.html', {'consoles' : consoles})

@login_required
def console_detail(request, console_id):
    console = Console.objects.get(id=console_id)
    games_console_doesnt_have = Game.objects.exclude(id__in = console.games.all().values_list('id'))
    accessory_form = AccessoryForm()
    return render(request, 'consoles/detail.html', { 
        'console' : console,
        'accessory_form': accessory_form,
        'games': games_console_doesnt_have
        })

class ConsoleCreate(LoginRequiredMixin, CreateView):
    model = Console
    fields = ['name', 'brand', 'description', 'year']

    def form_valid(self, form):
        # Assign the loggin the user (self.request.user)
        form.instance.user = self.request.user
        # Let CreateView continue to do its job
        return super().form_valid(form)

class ConsoleUpdate(LoginRequiredMixin, UpdateView):
    model = Console
    fields = ['description']

class ConsoleDelete(LoginRequiredMixin, DeleteView):
    model = Console
    success_url = '/consoles/'

@login_required
def add_accessory(request, console_id):
    form = AccessoryForm(request.POST)
    if form.is_valid():
        new_accessory = form.save(commit=False)
        new_accessory.console_id = console_id
        new_accessory.save()
    return redirect('detail', console_id=console_id)

class GameList(LoginRequiredMixin, ListView):
  model = Game

class GameDetail(LoginRequiredMixin, DetailView):
  model = Game

class GameCreate(LoginRequiredMixin, CreateView):
  model = Game
  fields = '__all__'

class GameUpdate(LoginRequiredMixin, UpdateView):
  model = Game
  fields = ['name', 'genre']

class GameDelete(LoginRequiredMixin, DeleteView):
  model = Game
  success_url = '/games/'

@login_required
def assoc_game(request, console_id, game_id):
    console = Console.objects.get(id = console_id)
    console.games.add(game_id)
    return redirect('detail', console_id = console_id)

@login_required
def unassoc_game(request, console_id, game_id):
    console = Console.objects.get(id = console_id)
    console.games.remove(game_id)
    return redirect('detail', console_id = console_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('games_index')
        else:
            error_message = 'Invalid sign up - try again'
    # otherwise, this is a GET request or bad POST
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
