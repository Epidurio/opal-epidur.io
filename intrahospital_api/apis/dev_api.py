from django.conf import settings
from intrahospital_api.apis import base_api
import datetime
import random


MALE_FIRST_NAMES = [
    'Harry', 'Ron', 'Tom', 'Albus', 'Severus', 'Rubeus', 'Draco',
]

FEMALE_FIRST_NAMES = [
    'Hermione', 'Minerva', 'Padma', 'Parvati', 'Lilly', 'Rita', 'Rowena'
]

LAST_NAMES = [
    'Potter', 'Granger', 'Weasley', 'Malfoy', 'Dumbledore', 'Gryffindor',
    'Greyback', 'Filch', 'Diggory', 'McGonagall'
]


class DevApi(base_api.BaseApi):
    def get_date_of_birth(self):
        return datetime.date.today() - datetime.timedelta(
            random.randint(1, 365 * 70)
        )

    def generate_random_demographics(self):
        return self.demographics(self.get_external_identifier())

    def to_date_str(self, date_obj):
        return datetime.datetime.combine(
            date_obj,
            datetime.datetime.min.time()
        ).strftime(settings.DATE_INPUT_FORMATS[0])

    def demographics(self, hospital_number):
        # will always be found unless you prefix it with 'x'
        if hospital_number.startswith('x'):
            return

        sex = random.choice(["Male", "Female"])
        if sex == "Male":
            first_name = random.choice(MALE_FIRST_NAMES)
            title = random.choice(["Dr", "Mr", "Not Specified"])
        else:
            first_name = random.choice(FEMALE_FIRST_NAMES)
            title = random.choice(["Dr", "Ms", "Mrs", "Not Specified"])

        return dict(
            sex=sex,
            date_of_birth=self.to_date_str(self.get_date_of_birth()),
            first_name=first_name,
            surname=random.choice(LAST_NAMES),
            title=title,
            hospital_number=hospital_number,
            nhs_number=self.get_external_identifier(),
        )

    def get_external_identifier(self):
        random_str = str(random.randint(0, 100000000))
        return "{}{}".format("0" * (9-len(random_str)), random_str)
