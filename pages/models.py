from django.db import models

# Create your models here.

class Category (models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book (models.Model):

    x = [
        ('avilable', 'avilable'),
        ('sold', 'sold'),
        ('rentel', 'rentel')
    ]


    title = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    book_photo = models.ImageField(upload_to= 'photos/%y/%m%d', null=True, blank=True)
    author_photo = models.ImageField(upload_to= 'photos/%y/%m%d', null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    relta_price = models.DecimalField(max_digits=5,decimal_places= 2, null=True, blank=True)
    retal_period = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=100, choices=x)

    category = models.ForeignKey(Category, on_delete=models.PROTECT ,null=True, blank=True)


    def __str__(self):
        return self.title