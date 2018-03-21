from opal.core.api import OPALRouter
from opal.core.api import LoginRequiredViewset
from opal.core.views import json_response
from opal.core import exceptions
import requests


class FhirServerSearchViewSet(LoginRequiredViewset):
    base_name = r'search'

    API_DETAILS = {
        'cerner_open': {
            'api_base_url':        'https://fhir-open.sandboxcerner.com/dstu2/0b8a0111-e8e6-4c26-a91c-5069cbc6b1ca/',
            'ident_token_prefix':  'urn:oid:2.2.2.2.2.2'
        },
        'smart_open': {
            'api_base_url':        'https://sb-fhir-dstu2.smarthealthit.org/api/smartdstu2/open/',
            'ident_token_prefix':  ''
        }
    }

    def list(self, request): return json_response('hi')

    def retrieve(self, request, *args, **kwargs):
        patient = self.get_data_from_fhir_server(kwargs['pk'])
        if patient['total'] == 1:
            demographics = patient['entry'][0]['resource']
            opal_demographics = {
                'hospital_number': demographics['identifier'][0]['value'],
                'nhs_number': 'NHS number not available',
                'first_name': " ".join(demographics['name'][0]['given']),  # sorry but syntax like "str".join(list) is why Python sucks
                'surname': " ".join(demographics['name'][0]['family']),    # list.join("str") is much less weird for normal people
                'date_of_birth': demographics['gender'],
                'ethnicity': 'Ethnicity placeholder',
                'birth_place': 'Birth Place placeholder',
            }
            return json_response(opal_demographics)

        elif patient['total'] == 0:
            return json_response("No patient with MRN %s was found on the FHIR server" % kwargs['pk'])

        elif patient['total'] > 1:
            return json_response("More than one patient with MRN %s was found on the FHIR server. This is unusual. And concerning." % kwargs['pk'])



    def get_data_from_fhir_server(self, cerner_mrn):
        query_type = "Patient"
        url = self.API_DETAILS['cerner_open']['api_base_url'] + query_type
        identifier_string = self.API_DETAILS['cerner_open']['ident_token_prefix'] + "|" + cerner_mrn
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
