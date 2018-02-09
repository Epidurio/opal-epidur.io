from opal.core import pathway
from epidurio import models


class RequestEpiduralPathway(pathway.PagePathway):
    display_name = "Request Epidural"
    slug = "request_epidural"

    steps = (
        pathway.Step(model=models.EpiduralRequest),
    )
