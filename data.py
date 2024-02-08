import requests

NUM_OF_QUESTIONS = 10
QUESTION_TYPE = "boolean"
URL = "https://opentdb.com/api.php"

# API request parameters
parameters = {
    "amount": NUM_OF_QUESTIONS,
    "type": QUESTION_TYPE
}

# Making API request
response = requests.get(URL, params=parameters)
response.raise_for_status()
question_data = response.json()['results']
