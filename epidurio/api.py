import requests
from django.conf import settings
from django.utils.dateparse import parse_date
from opal.core.api import OPALRouter
from opal.core.api import LoginRequiredViewset
from opal.core.views import json_response
from opal.core import exceptions


class FhirServerSearchViewSet(LoginRequiredViewset):
    base_name = r'search'

    PATIENT_FOUND_IN_FHIR = "patient_found_in_fhir"
    PATIENT_NOT_FOUND = "patient_not_found"

    def list(self, request): return json_response('hi')

    def retrieve(self, request, *args, **kwargs):
        patient = self.get_data_from_fhir_server(kwargs['pk'])

        #if patient is found on FHIR server and response contains 1 patient
        if patient['total'] == 1:
            demographics = patient['entry'][0]['resource']
            opal_demographics = {
                'hospital_number': demographics['identifier'][0]['value'],
                'nhs_number': 'NHS number not available',
                'first_name': " ".join(demographics['name'][0]['given']),  # sorry but syntax like "str".join(list) is why Python sucks
                'surname': " ".join(demographics['name'][0]['family']),    # list.join("str") is much less weird for normal people
                'date_of_birth': parse_date(demographics['birthDate']),
                'ethnicity': 'Ethnicity placeholder',
                'birth_place': 'Birth Place placeholder',
                'sex': demographics['gender'],
            }
            return json_response(dict(
                patient=dict(demographics=[opal_demographics]),
                status=self.PATIENT_FOUND_IN_FHIR),
            )

        # if patient is not found on FHIR server
        elif patient['total'] == 0:
            return json_response(dict(
                status=self.PATIENT_NOT_FOUND
            ))

        # if patient is found but there is more than one patient with that MRN (should not happen)
        elif patient['total'] > 1:
            return json_response("More than one patient with MRN %s was found on the FHIR server. This is unusual. And concerning." % kwargs['pk'])



    def get_data_from_fhir_server(self, cerner_mrn):
        query_type = "Patient"
        url = settings.FHIR_API_DETAILS['cerner_open']['api_base_url'] + query_type
        token_prefix = settings.FHIR_API_DETAILS['cerner_open']['ident_token_prefix']
        identifier_string = token_prefix + "|" + cerner_mrn
        querystring = {"identifier": identifier_string}
        headers = {'accept': "application/json",}
        response = requests.request("GET", url, headers=headers, params=querystring)
        if response.status_code == 200:
            return response.json()
        else:
            msg = "Error contacting external FHIR demographic API from Epidur.io"
            raise exceptions.APIError(msg)


epidurio_router = OPALRouter()
epidurio_router.register(FhirServerSearchViewSet.base_name, FhirServerSearchViewSet)
