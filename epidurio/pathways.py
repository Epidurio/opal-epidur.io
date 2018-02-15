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
