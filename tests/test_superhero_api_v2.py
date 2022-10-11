from data_models.model_superhero import ModelSuperHero
from pydantic import parse_obj_as, ValidationError
import pytest
import requests
from typing import List

# Endpoint URL
BASE_URL = "https://superhero.qa-test.csssr.com/superheroes"


class TestSuperheroAPI:

    @pytest.fixture
    def grab_data(self):
        """
        Grab data from endpoint URL
        :return: response
        """
        response = requests.get(BASE_URL)
        return response

    def test_superheroes_endp(self, grab_data):
        """
        Try to validate response & check response code == 200
        """
        superhero = parse_obj_as(List[ModelSuperHero], grab_data.json())

        # Use strings below if you need to push validation errors forward
        # try:
        #     superhero = parse_obj_as(List[ModelSuperHero], grab_data.json())
        # except ValidationError as e:
        #     print(e.json())

        assert grab_data.status_code == 200
