from django.db.models import fields
from django.utils import timezone
from opal import models
from opal.core import lookuplists
from opal.core.fields import ForeignKeyOrFreeText


class ProcedureType(lookuplists.LookupList): pass
class Indication(lookuplists.LookupList): pass
class SpinalOpiate(lookuplists.LookupList): pass
class EpiduralOpiate(lookuplists.LookupList): pass
class SpinalLocal(lookuplists.LookupList): pass
class EpiduralLocal(lookuplists.LookupList): pass


class EpiduralInsertion(models.EpisodeSubrecord):
    _is_singleton = True

    CERVIX_CHOICES = (
    ('<2 cm', '<2 cm',),
    ('3-5 cm', '3-5 cm',),
    ('> 6 cm', '> 6 cm',),
)

    insertion_date_time = fields.DateTimeField(
        null=True,
        # default=timezone.now,  (causes an Opal APIerror if uncommented)
        help_text="Date and time of the epidural insertion or epidural insertion attempt",
    )

    #needs to be the current user
    performed_by = fields.TextField(
        null=True,
        blank=True,

    )

    #pick from list of anaesthetist users
    supervised_by = fields.TextField(
        null=True,
        blank=True,

    )

    procedure = ForeignKeyOrFreeText(
        ProcedureType,
        help_text="Free text clinical record of the intervention"
    )


    # TODO should ideally be SNOMEDized
    indication = ForeignKeyOrFreeText(
        Indication,
        help_text="Description of the indication",
    )


    cervical_dilation  = fields.CharField(
        choices=CERVIX_CHOICES,
        blank=True, null=True,
        max_length=255,
    )


class Consent(models.EpisodeSubrecord):
    _is_singleton = True

    failure = fields.BooleanField(default=True)
    analgesia_expectations = fields.BooleanField(default=True)
    shivering = fields.BooleanField(default=True)
    pruritus = fields.BooleanField(default=True)
    blood_pressure_drop = fields.BooleanField(default=True)
    nausea_and_vomiting = fields.BooleanField(default=True)
    motor_block = fields.BooleanField(default=True)
    delayed_second_stage = fields.BooleanField(default=True)
    instrumental_delivery = fields.BooleanField(default=True)
    headache = fields.BooleanField(default=True)
    temporary_nerve_damage = fields.BooleanField(default=True)
    permanent_nerve_damage = fields.BooleanField(default=True)
    severe_complication = fields.BooleanField(default=True)
    other = fields.TextField(null=True)


class Asepsis(models.EpisodeSubrecord):
    _is_singleton = True

    gloves = fields.BooleanField(default=True)
    gown = fields.BooleanField(default=True)
    hat = fields.BooleanField(default=True)
    mask = fields.BooleanField(default=True)
    drape = fields.BooleanField(default=True)
    chlorhex = fields.BooleanField(default=True)


class Technique(models.EpisodeSubrecord):
    _is_singleton = True

    POSITION_CHOICES = (
        ('Sitting', 'Sitting',),
        ('Lateral', 'Lateral',),
    )
    LEVEL_CHOICES = (
        ('L2/3', 'L2/3',),
        ('L3/4', 'L3/4',),
        ('L4/5', 'L4/5',),
        ('Other', 'Other',),
    )

    APPROACH_CHOICES = (
        ('Midline', 'Midline',),
        ('Paramedian', 'Paramedian',),
    )

    TUOHY_NEEDLE_CHOICES = (
        ('16G', '16G',),
        ('18G', '18G',),
    )

    SPINAL_NEEDLE_CHOICES = (
        ('26G', '26G',),
        ('27G', '27G',),
    )

    LOR_CHOICES = (
        ('Saline', 'Saline',),
        ('Air', 'Air',),
    )

    CATHETER_IN_EPIDURAL_SPACE_CHOICES = (
        ('2 cm', '2 cm',),
        ('3 cm', '3 cm',),
        ('4 cm', '4 cm',),
        ('5 cm', '5 cm',),
        ('6 cm', '6 cm',),
    )

    LIDOCAINE_CHOICES = (
        ('1 %', '1 %',),
        ('2 %', '2 %',),
    )

    patient_position  = fields.CharField(
        choices=POSITION_CHOICES,
        blank=True, null=True,
        max_length=255,
    )

    level  = fields.CharField(
        choices=LEVEL_CHOICES,
        blank=True, null=True,
        max_length=255,
    )

    approach  = fields.CharField(
        choices=APPROACH_CHOICES,
        blank=True, null=True,
        max_length=255,
    )

    lidocaine  = fields.CharField(
        choices=LIDOCAINE_CHOICES,
        blank=True, null=True,
        max_length=255,
    )

    lidocaine_volume = fields.PositiveIntegerField(
        default=3,
    )

    tuohy_needle_choices = fields.CharField(
        choices=TUOHY_NEEDLE_CHOICES,
        blank=True, null=True,
        max_length=255,
    )

    spinal_needle_choices = fields.CharField(
        choices=SPINAL_NEEDLE_CHOICES,
        blank=True, null=True,
        max_length=255,
    )

    loss_of_resistance = fields.CharField(
        choices=LOR_CHOICES,
        blank=True, null=True,
        max_length=255,
    )

    depth_of_epidural_space = fields.PositiveIntegerField(
        default=3,

    )

    catheter_length_in_epidural_space = fields.CharField(
        choices=CATHETER_IN_EPIDURAL_SPACE_CHOICES,
        blank=True, null=True,
        max_length=255,
        default=3,
    )


class NeuraxialDrugs(models.EpisodeSubrecord):
    _is_singleton = True

    spinal_opiate = ForeignKeyOrFreeText(
        SpinalOpiate,
    )

    spinal_opiate_dose = fields.PositiveIntegerField(
        null=True,
        blank=True,
    )

    local_anaesthetic_spinal = ForeignKeyOrFreeText(
        SpinalLocal,
    )

    spinal_local_anaesthetic_volume = fields.PositiveIntegerField(
        null=True,
        blank=True,
    )

    epidural_opiate = ForeignKeyOrFreeText(
        EpiduralOpiate,
    )

    epidural_opiate_dose = fields.PositiveIntegerField(
        null=True,
        blank=True,
    )

    local_anaesthetic_epidural = ForeignKeyOrFreeText(
        EpiduralLocal,
    )

    epidural_local_anaesthetic_volume = fields.PositiveIntegerField(
        null=True,
        blank=True,
    )


class ProcedureNotes(models.EpisodeSubrecord):
    _is_singleton = True

    DIFFICULTY_CHOICES = (
        ('Straightforward', 'Straightforward',),
        ('Moderately Difficult', 'Moderately Difficult',),
        ('Difficult', 'Difficult',),
    )

    PARAESTHESIA_CHOICES = (
        ('None', 'None',),
        ('Spinal Needle', 'Spinal Needle',),
        ('Tuohy Needle', 'Tuohy Needle',),
        ('Epidural Catheter', 'Epidural Catheter'),
    )

    difficulty = fields.CharField(
        choices=DIFFICULTY_CHOICES,
        blank=True, null=True,
        max_length=255,
    )

    paraesthesia = fields.CharField(
        choices=PARAESTHESIA_CHOICES,
        blank=True, null=True,
        max_length=255,
    )

    complication_blood_in_catheter = fields.BooleanField(default=False)
    complication_dural_puncture = fields.BooleanField(default=False)
    complication_csf_aspirated = fields.BooleanField(default=False)
    complication_bony_obstruction = fields.BooleanField(default=False)
    complication_morethanone_interspace = fields.BooleanField(default=False)

    notes = fields.TextField(
        null=True,
        blank=True,
    )

    # NOTE: patient_id is handled because of EpisodeSubrecord inheritance
    # NOTE: created_at, updated_at and user_id are handled because of TrackedModel inheritance
