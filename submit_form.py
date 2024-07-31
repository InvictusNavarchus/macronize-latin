import requests
from bs4 import UnicodeDammit

def submit_form(text):
    # URL to which the form data will be submitted
    url = 'https://alatius.com/macronizer/'

    # Form data to be submitted
    form_data = {
        "textcontent": text,
        "macronize": "on",
        "scan": "0",
        "utov": "on",
    }

    # Send the POST request
    response = requests.post(url, data=form_data)
    response.encoding = 'utf-8'
    return response.text
    # return {response.text, response.status_code}