import requests
import json

r = requests.get('http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key=CBF58D86B866AF9E5B20A4A48664DA5A&steamid=76561198298885338')

data = r.json()

for key, value in data.items():
    mydict = value

for key, value in mydict.items():
    #print("Data: ", key)
    #print("Value: ", value)
    if key == "steamID" or key == "gameName":
        continue
    print()
    print(key.upper())
    for name in value:
        print(name)



