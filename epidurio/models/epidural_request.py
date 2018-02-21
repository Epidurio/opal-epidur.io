from django.db.models import fields
from django.utils import timezone
from opal import models


class EpiduralRequest(models.EpisodeSubrecord):
    _is_singleton = True

    # this may change if we decide to handle the State of EpiduralRequest differently
    # in the Ruby version this was an Enum
    # Could this be handled as a SNOMED-CT lookuplist?
    epidural_status = fields.PositiveIntegerField(
        null=True,
        help_text="Internal field for managing the state of the epidural request - ordered, in progress, completed, attempted-failed, etc)",
    )

    history = fields.TextField(
        null=True,
        help_text="Focused summary of the relevant history. Use this area to let the amaesthetist know about any relevant hazards ar special circumstances",
    )

    cannula_in_situ = fields.BooleanField(
        help_text="Does the patient have a peripheral venous cannula in situ?",
        default=False
    )

    anticoagulants = fields.BooleanField(
        help_text="Is the patient currently taking anticolagulants, antiplatelet agents, or any other medication that 'thins' blood or affects coagulation?",
        default=False
    )

    pyrexia = fields.BooleanField(
        help_text="Does the patient have a recent history of pyrexia?",
        default=False
        # TODO definition of pyrexia should be explicitly stated (temp, duration, what is 'recent' etc)
    )

    hypertension = fields.BooleanField(
        help_text="Does the patient have pregnancy-induced hypertension (PIH)?",
        default=False
    )

    # TODO this field could be autopopulated from the lab, also needs a timestamp to give meaning to 'latest'
    platelet_count = fields.CharField(
        null=True,
        max_length=20,
        help_text="Patient's latest Platelet count",
    )

    request_date_time = fields.DateTimeField(
        null=True,
        # default=timezone.now, (causes an Opal APIerror if uncommented)
        help_text="Date and time of the epidural request",)

    # NOTE: patient_id is handled because of EpisodeSubrecord inheritance
    # NOTE: created_at, updated_at and user_id are handled because of TrackedModel inheritance
