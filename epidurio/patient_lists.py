"""
Defining Opal PatientLists
"""
from opal import core
from epidurio import models


class LabourWardList(core.patient_lists.TaggedPatientList):
    display_name = "Labour Ward"
    tag = "labour"
    template_name = "patient_lists/layouts/labour_ward.html"

    schema = [
        models.Allergies,
        models.EpiduralRequest,
    ]


class EpiduralRequestsList(core.patient_lists.TaggedPatientList):
    display_name = "Epidural Requests"
    tag = "epidural_requested"
    template_name = "patient_lists/layouts/epidural_request.html"

    schema = [
        models.Allergies,
        models.EpiduralRequest,
    ]


class EpiduralFollowupList(core.patient_lists.TaggedPatientList):
    display_name = "Epidural Followups"
    tag = "epidural_completed"
    template_name = "patient_lists/layouts/card_list.html"
    direct_add = False
    # patients cannot be direct added; they must have had an epidural to be added

    schema = [
        models.EpiduralRequest,
        models.EpiduralInsertion,
    ]
