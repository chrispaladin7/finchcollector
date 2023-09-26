from django.db import models
from django.urls import reverse

LOCATIONS=(
    {'N','North'},
    {'S','South'},
    {'E','East'},
    {'W','West'},
)

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
    

class Distribution(models.Model):
    region = models.CharField(max_length=100)
    habitat = models.TextField()
    migration = models.TextField(blank=True, null=True)
    date = models.DateField()
    location = models.CharField(
        max_length=1,
        choices=LOCATIONS,
        default=LOCATIONS[0][0]
    ) 
    # Create a finch_id FK
    Finch = models.ForeignKey(
        Finch,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Distribution of {self.get_distribution_display()} in {self.date}'
     