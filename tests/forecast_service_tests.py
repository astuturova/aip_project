import unittest
from unittest.mock import patch

import requests


class TestMyClient(unittest.TestCase):
    @patch('utils.requests.get')
    def test_send_request_then_correct(self, mock_post):
        mock_post.return_value.status_code = 200
        headers = {"accept": "application/json"}
        response = requests.get(
            url=f"https://api.tomorrow.io/v4/weather/forecast?location=RU-MOW&timesteps=1d&apikey=1cE6v5BNFWnfPXBHicHZTuv9H7qENWxt",
            headers=headers)
        self.assertEqual(response.status_code, 200)

    @patch('utils.requests.get')
    def test_send_request_then_error(self, mock_post):
        mock_post.return_value.status_code = 400
        headers = {"accept": "application/json"}
        response = requests.get(
            url=f"https://api.tomorrow.io/v4/weather/forecast?location=&timesteps=1d&apikey=1cE6v5BNFWnfPXBHicHZTuv9H7qENWxt",
            headers=headers)
        self.assertEqual(response.status_code, 400)