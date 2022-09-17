from django.db import models
from django.urls import reverse

# Create your models here.
class Console(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()

    def __str__(self):
        return f"A {self.brand} {self.name} from {self.year}, {self.description}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'console_id': self.id})