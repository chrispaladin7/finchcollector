from django.db import models

# Create your models here.
class Finch(models.Model):
        species=models.CharField(max_length=50)
        color=models.CharField(max_length=25)
        size=models.CharField(max_length=10)
        description=models.TextField(max_length=250)
        weight=models.DecimalField(...,max_digits=3, decimal_places=2)

        def __str__(self):
            return  (f'({self.id}) {self.species} Color: {self.color} ')
     