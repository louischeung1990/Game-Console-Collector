from django.shortcuts import render

class Console:
    def __init__(self, name, brand, description, year):
        self.name = name
        self.brand = brand
        self.description = description
        self.year = year

consoles = [
    Console('N64', 'Nintendo', 'mint condition', 1996),
    Console('Dreamcast', 'Sega', 'scratched', 1998),
    Console('PlayStation 2', 'Sony', 'good condition', 2000),
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def consoles_index(request):
    return render(request, 'consoles/index.html', {'consoles' : consoles})