# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models import Value
from django.db.models.functions import Concat 

class Employee(models.Model):
    user_name = models.CharField(primary_key=True, max_length=10)
    password = models.CharField(max_length=20, blank=True, null=True)
    lead_by = models.ForeignKey('self', models.DO_NOTHING, db_column='lead_by', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'

class ItemManager(models.Manager):
    """Add the full name"""
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.annotate(full_name=Concat("state", Value(" "),
                                                  "category"))


class Item(models.Model):
    state = models.CharField(max_length=15, blank=True, null=True)
    category = models.CharField(max_length=25, blank=True, null=True)
    warehouse = models.ForeignKey('Warehouse', models.DO_NOTHING, blank=True, null=True)
    date_of_stock = models.DateTimeField(blank=True, null=True)
    objects = ItemManager()

    def __str__(self):
        return f"{self.state} {self.category}"

    class Meta:
        managed = True
        db_table = 'item'


class Warehouse(models.Model):

    class Meta:
        # managed = False
        db_table = 'warehouse'
