from django.contrib.auth.models import User
from opal.models import Patient
from intrahospital_api.apis import get_api
from epidurio.patient_lists import LabourWardList
from django.db import transaction
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    @transaction.atomic()
    def handle(self, *args, **options):
        api = get_api()
        demographics = api.generate_random_demographics()
        user = User.objects.first()
        for i in range(10):
            patient = Patient.objects.create()
            episode = patient.create_episode()
            demographics = patient.demographics_set.first()
            demographics_dict = api.generate_random_demographics()
            demographics.update_from_dict(demographics_dict, user)
            episode.set_tag_names([LabourWardList.tag], user)
            location = episode.location_set.get()
            location.bed = str(i+1)
            location.save()
