from opal.core import pathway
from epidurio import models
from epidurio import patient_lists


class AddPatientPathway(pathway.PagePathway):
    display_name = "Add a Patient"
    slug = "add_patient"
    steps = (
        pathway.Step(
            display_name='Add a Patient to Epidur.io',
            icon = "fa fa-female",
            step_controller="AddPatientCtrl",
            template = 'pathway/add-patient.html',
        ),
        models.Location,
    )


class RequestEpiduralPathway(pathway.PagePathway):
    display_name = "Request Epidural"
    slug = "request_epidural"

    steps = (
        pathway.Step(
            model=models.EpiduralRequest,
            step_controller="EpiduralRequestCtrl"
        ),

        models.Pregnancy,
        models.Progress,
        models.Preparation,
    )

    def save(self, data, user=None, episode=None, patient=None):
        super(RequestEpiduralPathway, self).save(
            data, user=user, episode=episode, patient=patient
        )
        episode.set_tag_names(
            [patient_lists.EpiduralRequestsList.tag, patient_lists.LabourWardList.tag], user
        )

        return patient, episode


class RecordEpiduralPathway(pathway.PagePathway):
    display_name = "Record Epidural"
    slug = "record_epidural"

    steps = (
        pathway.Step(
            model=models.EpiduralInsertion,
            step_controller="EpiduralInsertionCtrl"
        ),
        models.Consent,
        models.Asepsis,
        models.Technique,
        models.NeuraxialDrugs,
        models.ProcedureNotes,
    )

    def save(self, data, user=None, episode=None, patient=None):
        super(RecordEpiduralPathway, self).save(
            data, user=user, episode=episode, patient=patient
        )
        episode.set_tag_names(
            [patient_lists.EpiduralFollowupList.tag, patient_lists.LabourWardList.tag], user
        )
        return patient, episode


class RecordFollowUPPathway(pathway.PagePathway):
    display_name = "Record Follow Up"
    slug = "record_follow_up"

    steps = (
        pathway.Step(
            model=models.EpiduralFollowUp,
            step_controller="FollowUpCtrl"
        ),
        models.SatisfactionRating,
    )

    def save(self, data, user=None, episode=None, patient=None):
        super(RecordFollowUPPathway, self).save(
            data, user=user, episode=episode, patient=patient
        )
        episode.set_tag_names(
            [patient_lists.LabourWardList.tag], user
        )
        return patient, episode
