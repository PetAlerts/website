from django.db import models
from django.utils.translation import ugettext as _


class Animal(models.Model):
    TYPE_DOG = 'D'
    TYPE_CAT = 'C'
    TYPE_OTHER = 'O'
    TYPE_CHOICES = (
        (TYPE_DOG, _('Dog')),
        (TYPE_CAT, _('Cat')),
        (TYPE_OTHER, _('Other')))
    AGE_CUB = 'CU'
    AGE_ADULT = 'AD'
    AGE_CHOICES = (
        (AGE_CUB, _('Cub')),
        (AGE_ADULT, _('Adult')))
    HEALTH_GOOD = 'G'
    HEALTH_BAD = 'B'
    HEALTH_CHOICES = (
        (HEALTH_GOOD, _('Good')),
        (HEALTH_BAD, _('Bad')))

    type = models.CharField(choices=TYPE_CHOICES, max_length=1)
    age = models.CharField(choices=AGE_CHOICES, max_length=2, null=True, blank=True)
    health = models.CharField(choices=HEALTH_CHOICES, max_length=1, null=True, blank=True)
    picture = models.ImageField()

    def __unicode__(self):
        return '{} {}'.format(self.pk, self.get_type_display())


class Alert(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    lat = models.FloatField()
    lng = models.FloatField()
    animal = models.ForeignKey(Animal)
