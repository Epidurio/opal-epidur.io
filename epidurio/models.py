"""
epidurio models.
"""
from django.db.models import fields
from django.utils import timezone
from opal import models

"""
Core Opal models - these inherit from the abstract data models in
opal.models but can be customised here with extra / altered fields.
"""
class Demographics(models.Demographics): pass
class Location(models.Location): pass
class Allergies(models.Allergies): pass
class Diagnosis(models.Diagnosis): pass
class PastMedicalHistory(models.PastMedicalHistory): pass
class Treatment(models.Treatment): pass
class Investigation(models.Investigation): pass
class SymptomComplex(models.SymptomComplex): pass
class PatientConsultation(models.PatientConsultation): pass

# we commonly need a referral route, ie how the patient
# came to the service, but not always.
# class ReferralRoute(models.ReferralRoute): pass

"""
End Opal core models
"""


class EpiduralRequest(models.EpisodeSubrecord):

    # this may change if we decide to handle the State of EpiduralRequest differently
    # in the Ruby version this was an Enum
    # Could this be handled as a SNOMED-CT lookuplist?
    epidural_status = fields.IntegerField(
        null=True,
        help_text="Internal field for managing the state of the epidural request - ordered, in progress, completed, attempted-failed, etc)",
    )

    history = fields.TextField(
        null=True,
        help_text="Focused summary of the relevant history. Use this area to let the amaesthetist know about any relevant hazards ar special circumstances",
    )

    cannula_in_situ = fields.BooleanField(
        help_text="Does the patient have a peripheral venous cannula in situ?",
    )

    anticoagulants = fields.BooleanField(
        help_text="Is the patient currently taking anticolagulants, antiplatelet agents, or any other medication that 'thins' blood or affects coagulation?",
    )

    pyrexia = fields.BooleanField(
        help_text="Does the patient have a recent history of pyrexia?",
        # TODO definition of pyrexia should be explicitly stated (temp, duration, what is 'recent' etc)
    )

    hypertension = fields.BooleanField(
        help_text="Does the patient have pregnancy-induced hypertension (PIH)?",
    )

    # TODO this field could be autopopulated from the lab, also needs a timestamp to give meaning to 'latest'
    platelet_count = fields.CharField(
        null=True,
        max_length=20,
        help_text="Patient's latest Platelet count",
    )

    request_date_time = fields.DateTimeField(
        null=True,
        default=timezone.now,
        help_text="Date and time of the epidural request",)

    # NOTE: FK patient_id is handled because of EpisodeSubrecord inheritance
    # NOTE: FK user_id is handled because of TrackedModel inheritance
