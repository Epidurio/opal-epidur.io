from fhirclient import client
import fhirclient.models.patient as p
import fhirclient.models.humanname as hn


API_BASES = {
    'cerner-open': 'https://fhir-open.sandboxcerner.com/dstu2/0b8a0111-e8e6-4c26-a91c-5069cbc6b1ca/',
    'smart-open': 'https://sb-fhir-dstu2.smarthealthit.org/api/smartdstu2/open/'
}


def search_server_by_cerner_mrn(cerner_mrn):
    # a cerner MRN identifier token urn:oid:2.2.2.2.2.2|412579456
    client = setup()
    search = p.Patient.where(struct={'identifier': cerner_mrn})
    patients = search.perform_resources(client.server)

    # returns an array of matching patients (hopefully just one unless they've reused the same identifier twice)
    return patients


def get_patient_demographics(cerner_mrn):
    patient = search_server_by_cerner_mrn(cerner_mrn)[0] # there should only be ONE
    print(patient.as_json())
    demographics = {
        'hospital_number': '',
        'nhs_number': 'NHS number placeholder',
        'first_name': patient.name[0].family,  # TODO: handle case of more than one name.family
        'surname': patient.name[0].given,  # TODO: handle case of more than one name.given
        'date_of_birth': patient.birthDate.date,
        'sex': patient.gender,
        'ethnicity': 'Ethnicity placeholder',
        'birth_place': 'Birth Place placeholder',
    }
    print(demographics)


def setup():
    client_instance = client.FHIRClient(
        settings={
            'app_id': 'epidurio',
            'api_base': API_BASES['cerner-open'],
            }
        )
    return client_instance
