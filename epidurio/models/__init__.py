from .epidural_insertion import (
    EpiduralInsertion,
    Asepsis,
    Consent,
    Technique,
    NeuraxialDrugs,
    ProcedureNotes
    )
from .epidural_request import EpiduralRequest
from .epidural_follow_up import EpiduralFollowUp, SatisfactionRating

from opal import models

# Core Opal models - these inherit from the abstract data models in
# opal.models but can be customised here with extra / altered fields.

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


__all__ = [
    'EpiduralInsertion',
    'EpiduralRequest',
    'EpiduralFollowUp',
    'SatisfactionRating',
    'Asepsis',
    'Consent',
    'Technique',
    'NeuraxialDrugs',
    'ProcedureNotes',
]
