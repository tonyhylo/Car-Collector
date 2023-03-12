from django.shortcuts import render, redirect

# Create your views here.
# Add the following import
from django.http import HttpResponse
from . models import Car
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import WashingForm

# cars = [
#   Car('Tesla', 'Model 3', 2020, 'Black'),
#   Car('Honda', 'SK2000', 2001, 'Yellow'),
#   Car('Mazda', 'MX-5', 1990, 'Sky Blue')
# ]

class CarCreate(CreateView):
  model = Car
  fields = '__all__'
  success_url = '/cars/'

class CarUpdate(UpdateView):
  model = Car
  fields = '__all__'

class CarDelete(DeleteView):
  model = Car
  success_url = '/cars/'

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')


def cars_index(request):
  cars = Car.objects.all()
  return render(request, 'cars/index.html', { 'cars': cars })


def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  washing_form = WashingForm()
  return render(request, 'cars/detail.html', { 'car': car, 'washing_form': washing_form })


def add_washes(request, car_id):
  # create a ModelForm instance using the data in request.POST
  form = WashingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_wash = form.save(commit=False)
    new_wash.car_id = car_id
    new_wash.save()
  return redirect('detail', car_id=car_id)