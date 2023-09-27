from django.db import models
from django.urls import reverse
from datetime import date

LOCATIONS=(
    ('N','North'),
    ('S','South'),
    ('E','East'),
    ('W','West'),
)

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner'),
)

# Create your models here.
class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})

class Finch(models.Model):
    species=models.CharField(max_length=50)
    color=models.CharField(max_length=25)
    size=models.CharField(max_length=10)
    description=models.TextField(max_length=250)
    # Foreign key referrencing Toy table
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return  (f'({self.id}) {self.species} Color: {self.color} ')
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id':self.id})
    
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
    

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

class Feeding(models.Model):
  date = models.DateField('Feeding date')
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
  )
  # Create a finch_id FK((Finch)one-to-many(Feeding))
  finch = models.ForeignKey(
    Finch,
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"
  
class Meta:
   ordering = ['-date']
     
