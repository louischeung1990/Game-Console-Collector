from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

ACCESSORIES = (
    ('C', 'Controller'),
    ('M', 'Memory Card'),
    ('E', 'External Hard Drive')
)

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    release_year = models.IntegerField('Release Year')

    def __str__(self):
        return f"{self.name} is a {self.genre} type of game released in {self.release_year}"

    def get_absolute_url(self):
        return reverse('game_detail', kwargs={'pk':self.id})

class Console(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    games = models.ManyToManyField(Game)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"A {self.brand} {self.name} from {self.year}, {self.description}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'console_id': self.id})

class Accessory(models.Model):
    name = models.CharField(
        max_length=1,
        choices=ACCESSORIES,
        default=ACCESSORIES[0][0]
        )
    number = models.IntegerField()
    date_purchased = models.DateField('Date purchased')
    console = models.ForeignKey(Console, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.number} {self.get_name_display()} purchased on {self.date_purchased}"

    class Meta:
        ordering = ['-date_purchased']
