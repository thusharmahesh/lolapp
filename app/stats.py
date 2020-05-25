import requests
from app.constants import apikey

def WinRate(summonerId):
    URL = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summonerId + '?api_key=' + apikey
    response = requests.get(URL)
    encryptedSummonerId = response.json()['id']
    new_URL = 'https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/' + encryptedSummonerId + '?api_key=' + apikey
    new_response = requests.get(new_URL)
    out = new_response.json()
    wins = out[0]['wins']
    losses = out[0]['losses']
    winrate = ((wins)/(wins+losses))*100
    return winrate