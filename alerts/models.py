import string
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _
from nominatim import NominatimReverse


class Alert(models.Model):
    UNKNOWN = 'U'
    UNKNOWN_CHOICE = (UNKNOWN, _('Unknown'))
    TYPE_DOG = 'D'
    TYPE_CAT = 'C'
    TYPE_OTHER = 'O'
    TYPE_CHOICES = (
        (TYPE_DOG, _('Dog')),
        (TYPE_CAT, _('Cat')),
        (TYPE_OTHER, _('Other')))
    GENRE_FEMALE = 'F'
    GENRE_MALE = 'M'
    GENRE_CHOICES = (
        UNKNOWN_CHOICE,
        (GENRE_FEMALE, _('Female')),
        (GENRE_MALE, _('Male'))
    )
    AGE_CUB = 'Y'
    AGE_ADULT = 'A'
    AGE_CHOICES = (
        (AGE_CUB, _('Cub/Young')),
        (AGE_ADULT, _('Adult')))

    species = models.CharField(choices=TYPE_CHOICES, max_length=1)
    genre = models.CharField(choices=GENRE_CHOICES, max_length=1, default=UNKNOWN)
    age = models.CharField(choices=AGE_CHOICES, max_length=1, default=AGE_ADULT)
    immediate_danger = models.BooleanField(default=False, verbose_name=_('In immediate danger'))
    picture = models.ImageField()
    date = models.DateTimeField(auto_now_add=True)
    lat = models.FloatField()
    lng = models.FloatField()
    details = models.CharField(max_length=500, verbose_name=_('Other details'), null=True, blank=True)

    def __unicode__(self):
        return string.join([self.get_age_display(), self.get_species_display()])

    def get_address(self):
        nomrev = NominatimReverse()
        result = nomrev.query(lat=self.lat, lon=self.lng)
        return result.get('display_name')

    def get_absolute_url(self):
        return reverse('alerts:detail', args=[str(self.id)])
