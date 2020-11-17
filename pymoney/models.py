from django.db import models
from django.utils.text import slugify


class Budget(models.Model):
    """
    docstring
    """
    name = models.CharField(max_length=100)
    budget = models.IntegerField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Budget, self).save(*args, **kwargs)


class Category(models.Model):
    """
    docstring
    """
    Budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class Expense(models.Model):
    """
    docstring
    """
    Budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Income(models.Model):
    """
    docstring
    """
    Budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Saving(models.Model):
    """
    docstring
    """
    Budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)