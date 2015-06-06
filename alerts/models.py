import string
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _
from nominatim import NominatimReverse
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


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
    GENDER_FEMALE = 'F'
    GENDER_MALE = 'M'
    GENDER_CHOICES = (
        UNKNOWN_CHOICE,
        (GENDER_FEMALE, _('Female')),
        (GENDER_MALE, _('Male'))
    )
    AGE_CUB = 'Y'
    AGE_ADULT = 'A'
    AGE_CHOICES = (
        (AGE_CUB, _('Cub/Young')),
        (AGE_ADULT, _('Adult')))

    species = models.CharField(choices=TYPE_CHOICES, max_length=1, default=TYPE_DOG)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, default=UNKNOWN)
    age = models.CharField(choices=AGE_CHOICES, max_length=1, default=AGE_ADULT)
    immediate_danger = models.BooleanField(default=False, verbose_name=_('In immediate danger'))
    picture = ProcessedImageField(upload_to='.',
                                 blank=True, null=True,
                                 processors=[ResizeToFit(265, 320)],
                                 format='JPEG',
                                 options={'quality': 90},
                                 verbose_name=_('Pet'))
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
