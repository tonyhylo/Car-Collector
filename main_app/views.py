from django.shortcuts import render

# Create your views here.
# Add the following import
from django.http import HttpResponse

class Car:  # Note that parens are optional if not inheriting from another class
  def __init__(self, make, model, year, colour):
    self.make = make
    self.model = model
    self.year = year
    self.colour = colour

cars = [
  Car('Tesla', 'Model 3', 2020, 'Black'),
  Car('Honda', 'SK2000', 2001, 'Yellow'),
  Car('Mazda', 'MX-5', 1990, 'Sky Blue')
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Welcome to my car collection</h1>')

def about(request):
  return render(request, 'about.html')


def cars_index(request):
  return render(request, 'cars/index.html', { 'cars': cars })