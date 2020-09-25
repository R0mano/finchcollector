from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Character, Spaceship
from .forms import ForceForm


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def characters_index(request):
  characters = Character.objects.all().order_by('name')
  return render(request, 'characters/index.html', { 'characters': characters })

def character_detail(request, character_id):
  character = Character.objects.get(id=character_id)
  spaceships_character_doesnt_have = Spaceship.objects.exclude(id__in = character.spaceships.all().values_list('id'))
  force_form = ForceForm()
  return render(request, 'characters/detail.html', { 
    'character': character,
    'force_form': force_form,
    'spaceships': spaceships_character_doesnt_have
  })

class CharacterCreate(CreateView):
  model = Character
  fields = ['name', 'origin', 'light_saber_color', 'has_force', ]
  success_url = '/characters/'

class CharacterUpdate(UpdateView):
  model = Character
  fields = ['origin', 'light_saber_color', 'has_force']

class CharacterDelete(DeleteView):
  model = Character
  success_url = '/characters/'

def add_force(request, character_id):
  form = ForceForm(request.POST)
  #Validate the form
  if form.is_valid():
    new_force= form.save(commit=False)
    new_force.character_id= character_id
    new_force.save()
  return redirect('detail', character_id=character_id)

class SpaceshipList(ListView):
  model = Spaceship

class SpaceshipDetail(DetailView):
  model = Spaceship

class SpaceshipCreate(CreateView):
  model = Spaceship
  fields = '__all__'

class SpaceshipUpdate(UpdateView):
  model = Spaceship
  fields = '__all__'

class SpaceshipDelete(DeleteView):
  model = Spaceship
  success_url = '/spaceships/'

def assoc_spaceship(request, character_id, spaceship_id):
  character = Character.objects.get(id=character_id)
  # spaceship = spaceship.objects.get(id=spaceship_id)
  character.spaceships.add(spaceship_id)
  return redirect('detail', character_id=character_id)
