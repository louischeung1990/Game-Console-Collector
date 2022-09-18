from django.db import models
from django.urls import reverse

ACCESSORIES = (
    ('C', 'Controller'),
    ('M', 'Memory Card'),
    ('E', 'External Hard Drive')
)

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
