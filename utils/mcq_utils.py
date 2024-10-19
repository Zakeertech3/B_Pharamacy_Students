import json

def get_mcq_data():
    with open('data/mcq_questions.json') as file:
        return json.load(file)
