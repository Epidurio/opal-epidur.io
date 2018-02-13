from django.db.models import fields
from django.utils import timezone
from opal import models
from opal.core import lookuplists
from opal.core.fields import ForeignKeyOrFreeText

class ProcedureType(lookuplists.LookupList): pass


class EpiduralInsertion(models.EpisodeSubrecord):

    insertion_date_time = fields.DateTimeField(
        null=True,
        # default=timezone.now,  (causes an Opal APIerror if uncommented)
        help_text="Date and time of the epidural insertion or epidural insertion attempt",
    )

    # TODO should ideally allow SNOMED codes to be embedded in the text
    insertion_record = ForeignKeyOrFreeText(
        ProcedureType,
        help_text="Free text clinical record of the intervention"
    )


    # TODO should ideally be SNOMEDized
    indication = fields.CharField(
        null=True,
        max_length=255,
        help_text="Description of the intervention",
    )

    number_of_attempts = fields.PositiveIntegerField(
        default=1,
        help_text="The number of discrete epidural insertion attempts",
    )

    # TODO should ideally be SNOMEDized
    # TODO consider a default value? "no immediate complications"
    complications = fields.CharField(
        blank=True, null=True,
        max_length=255,
        help_text="Complications caused by the epidural insertion",
    )

    # TODO should ideally be SNOMEDized
    # TODO any other options @TimCKnowles?
    OUTCOME_CHOICES=(
        ("SUCCESS", "Successful epidural insertion and effective analgesia"),
        ("INEFFECTIVE", "Successful insertion of epidural catheter"),
        ("DURAL PUNCTURE", "Epidural insertion caused dural puncture"),
        ("FAILURE", "Failed epidural insertion"),
    )
    outcome = fields.CharField(
        choices = OUTCOME_CHOICES,
        blank=True, null=True,
        help_text="Outcome of the epidural insertion attempt",
        max_length=255,
    )

    # NOTE: patient_id is handled because of EpisodeSubrecord inheritance
    # NOTE: created_at, updated_at and user_id are handled because of TrackedModel inheritance
