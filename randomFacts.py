import requests
import re

def loadAPIResponse(link):
    response = requests.get(link)
    data = response.json()
    return data

def uslessfacts1():
    # Make a GET request to the API endpoint
    data = loadAPIResponse('https://uselessfacts.jsph.pl/random.json?language=en')
    # Extract the random fact
    random_fact = data['text']
    return random_fact

def catFact():
    fact = loadAPIResponse("https://catfact.ninja/fact")["fact"]
    re.sub(r'(.+)', fact, '')
    return fact
