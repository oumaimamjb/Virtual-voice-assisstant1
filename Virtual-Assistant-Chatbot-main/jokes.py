import requests

def joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    json_data = requests.get(url).json()

    if 'setup' in json_data and 'punchline' in json_data:
        setup = json_data['setup']
        punchline = json_data['punchline']
        return setup, punchline
    else:
        return "Couldn't fetch joke", "Sorry, unable to fetch the punchline"


