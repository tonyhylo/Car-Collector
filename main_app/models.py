from django.db import models
from django.urls import reverse

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    colour = models.TextField(max_length=250)
    year = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})
    

washed = (
    ('I', 'Interior'),
    ('E', 'Exterior')
)

class Washes(models.Model):
    date = models.DateField('washed date')
    whereWashed = models.CharField(max_length=1, choices=washed, default=washed[0][0])
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_whereWashed_display()} on {self.date}"

    class Meta:
        ordering = ['-date']