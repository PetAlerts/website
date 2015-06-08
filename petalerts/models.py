from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class ModelWithLocation(models.Model):
    lat = models.FloatField(
        validators=[
            MaxValueValidator(90),
            MinValueValidator(-90)
        ]
    )
    lng = models.FloatField(
        validators=[
            MaxValueValidator(180),
            MinValueValidator(-180)
        ]
    )

    class Meta:
        abstract = True