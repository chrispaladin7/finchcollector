from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
    species=models.CharField(max_length=50)
    color=models.CharField(max_length=25)
    size=models.CharField(max_length=10)
    description=models.TextField(max_length=250)

    def __str__(self):
        return  (f'({self.id}) {self.species} Color: {self.color} ')
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id':self.id})
     