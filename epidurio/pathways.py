from opal.core import pathway
from epidurio import models
from epidurio import patient_lists


class RequestEpiduralPathway(pathway.PagePathway):
    display_name = "Request Epidural"
    slug = "request_epidural"

    steps = (
        models.EpiduralRequest,
    )

    def save(self, data, user=None, episode=None, patient=None):
        super(RequestEpiduralPathway, self).save(
            data, user=user, episode=episode, patient=patient
        )
        episode.set_tag_names(
            [patient_lists.EpiduralRequestsList.tag], user
        )
        return patient, episode


class RecordEpiduralPathway(pathway.PagePathway):
    display_name = "Record Epidural"
    slug = "record_epidural"

    steps = (
        models.EpiduralInsertion,
    )

    def save(self, data, user=None, episode=None, patient=None):
        super(RecordEpiduralPathway, self).save(
            data, user=user, episode=episode, patient=patient
        )
        episode.set_tag_names(
            [patient_lists.EpiduralFollowupList.tag], user
        )
        return patient, episode


class RecordFollowUPPathway(pathway.PagePathway):
    display_name = "Record Follow Up"
    slug = "record_follow_up"

    steps = (
        models.EpiduralFollowUp,
        models.SatisfactionRating,
    )

    def save(self, data, user=None, episode=None, patient=None):
        super(RecordEpiduralPathway, self).save(
            data, user=user, episode=episode, patient=patient
        )
        episode.set_tag_names(
            [], user
        )
        return patient, episode
