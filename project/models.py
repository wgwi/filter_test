from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    release_date = models.DateField()
    manufacturer = models.ForeignKey(Manufacturer)

    def __unicode__(self):
        return self.name

import django_filters

class ProductFilter(django_filters.FilterSet):
     price = django_filters.NumberFilter(lookup_type='lt')
     class Meta:
         model = Product
         fields = ['price', 'release_date']


import django_tables2 as tables
from django.utils.safestring import mark_safe

class IdColumn(tables.Column):
    def render(self, value):
        return mark_safe('<input type="checkbox" value="%d"/>' % value)

class ProductTable(tables.Table):
    id = tables.CheckBoxColumn()
    name = tables.Column()
    price = tables.Column(orderable=True)
    description =tables.Column()
    release_date = tables.Column(orderable=True)
    manufacturer = tables.Column()

    class Meta:
        #model = Product
        attrs = {'class': 'paleblue'}
        orderable = False
        sequence = ('id', 'name', 'price', 'description', 'release_date', 'manufacturer')

