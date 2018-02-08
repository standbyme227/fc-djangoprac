from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    toppings = models.ManyToManyField('Topping')

    def __str__(self):
        return '{topping}가 올라간 {pizza}'.format(
            pizza = self.name,
            topping = ', '.join(self.toppings.values_list('name', flat=True)),
        )


class Topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name