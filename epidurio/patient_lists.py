"""
Defining Opal PatientLists
"""
from opal import core
from opal.models import Episode
from epidurio import models


class AllPatientsList(core.patient_lists.PatientList):
    display_name = 'All Patients'

    schema = [
        models.Demographics,
        models.Diagnosis,
        models.Treatment
    ]

    def get_queryset(self, **kwargs):
        return Episode.objects.all()


class EpiduralRequestsList(core.patient_lists.TaggedPatientList):
    display_name = "Epidural Requests"
    tag = "epidural_requested"

    schema = [
        models.Allergies,
        models.Demographics,
        models.EpiduralRequest,
    ]


class EpiduralFollowUpsList(core.patient_lists.TaggedPatientList):
    display_name = "Epidural Followups"
    tag = "epidural_completed"
    direct_add = False
    # patients cannot be direct added; they must have had an epidural to be added

    schema = [
        models.Demographics,
        models.EpiduralRequest,
        models.EpiduralInsertion,
    ]
