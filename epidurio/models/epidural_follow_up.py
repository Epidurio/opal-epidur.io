from django.db.models import fields
from django.utils import timezone
from opal import models


class EpiduralFollowUp(models.EpisodeSubrecord):
    _is_singleton = True
    time_of_follow_up = fields.DateTimeField(
        blank=True, null=True
    )
    headache = fields.BooleanField(default=False)
    has_not_mobilised = fields.BooleanField(default=False)
    weakness = fields.BooleanField(default=False)
    sensory_disturbance = fields.BooleanField(default=False)
    back_pain = fields.BooleanField(default=False)
    has_not_passed_urine = fields.BooleanField(default=False)


<<<<<<< HEAD
=======

>>>>>>> 85f2f3ec15414ffe20d648048c24fe0d75b0ad12
class SatisfactionRating(models.EpisodeSubrecord):
    _is_singleton = True
    SATISFACTION_CHOICES = (
        ('Dissatisfied', 'Dissatisfied',),
        ('Satisfied', 'Satisfied',),
        ('Very Satisfied', 'Very Satisfied',),
    )

<<<<<<< HEAD
    labor_analgesia = fields.CharField(
=======

    labor_analgesia  = fields.CharField(
>>>>>>> 85f2f3ec15414ffe20d648048c24fe0d75b0ad12
        choices=SATISFACTION_CHOICES,
        blank=True, null=True,
        max_length=255,
    )

    delivery_analgesia = fields.CharField(
        choices=SATISFACTION_CHOICES,
        blank=True, null=True,
        max_length=255,
    )

    post_natal_analgesia = fields.CharField(
        choices=SATISFACTION_CHOICES,
        blank=True, null=True,
        max_length=255,
    )
