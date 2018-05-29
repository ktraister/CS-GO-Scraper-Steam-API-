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
    print("==========================")
    for name in value:
        #cut out our field
        val = str(name)
        field = val[10:]
        findex = field.find("'")
        field = field[:findex]

        #cut out our value
        rindex = val.rfind(':')
        svalue = val[rindex + 2:]
        svalue = svalue.replace("}", '')
        print("%s : %s" % (field, svalue))

        #KDR
        if field == "total_kills":
            total_kills = svalue
        if field == "total_deaths":
            total_deaths = svalue
        #total shots hit/total shots fired
        if field == "total_shots_fired":
            total_shots_fired = svalue
        if field == "total_shots_hit":
            total_shots_hit = svalue
        #head shot ratio
        if field == "total_kills_headshot":
            total_kills_headshot = svalue
        #win/loss ratio
        if field == "total_wins":
            total_wins = svalue
        if field == "total_rounds_played":
            total_rounds_played = svalue
        #last match composites
        if field == "last_match_wins":
            last_match_wins = svalue
        if field == "last_match_kills":
            last_match_kills = svalue
        if field == "last_match_deaths":
            last_match_deaths = svalue
        if field == "last_match_mvps":
            last_match_mvps = svalue
        if field == "last_match_damage":
            last_match_damage = svalue

#code to read last data and set us up for delta
if os.path.isfile('.csgofile'):
    with open('.csgofile', 'r') as infile:
        #is this the best way to do this?
        for line in infile.readlines():
            if kdr in line:
                lastkdr = line.split(':')
                lastkdr = lastkdr[1]
            if rot in line:
                lastrot = line.split(':')
                lastrot = lastrot[1]
            if hsr in line:
                lasthsr = line.split(':')
                lasthsr = lasthsr[1]
            if wlr in line:
                lastwlr = line.split(':')
                lastwlr = lastwlr[1]
            if lmkdr in line:
                lastlmkdr = line.split(':')
                lastlmkdr = lastlmkdr[1]
            if last_match_wins in line:
                last_last_match_wins = line.split(':')
                last_last_match_wins = last_last_match_wins[1]
            if last_match_mvps in line:
                last_last_match_mvps = line.split(':')
                last_last_match_mvps = last_last_match_mvps[1]
            if last_match_damage in line:
                last_last_match_damage = line.split(':')
                last_last_match_damage = last_last_match_damage[1]

print()
print("GLOBAL COMPOSITES")
print("==========================")
kdr = int(total_kills) / int(total_deaths)
rot = int(total_shots_hit) / int(total_shots_fired)
hsr = int(total_kills_headshot) / int(total_kills)
wlr = int(total_wins) / int(total_rounds_played)
print("KDR: ", kdr)
print("ROT: ", rot)
print("HSR: ", hsr)
print("WLR: ", wlr)

print()
print("GLOBAL COMPOSITES DELTA")
print("==========================")
#kdr block
if lastkdr > kdr:
    print("KDR Delta: ", "↓")
elif lastkdr == kdr:
    print("KDR Delta: ", "=")
elif lastkdr < kdr:
    print("KDR Delta: ", "↑")
#rot block
#hsr block
#wlr block

print()
print("LAST MATCH COMPOSITES")
print("==========================")
lmkdr = int(last_match_kills) / int(last_match_deaths)
print("Last Match Win: ", last_match_wins)
print("Last Match KDR: ", lmkdr)
print("Last Match MVPs: ", last_match_mvps)
print("Last Match Damage: ", last_match_damage)

print()
print("LAST MATCH COMPOSITES DELTA")
print("==========================")
#lmw block
#lmkdr block
#lmm block
#lmd block


# write here to use this to determine delta in gameplay since last run
with open('.csgofile', 'w') as outfile:
    kdro = "%s:%s" % ("kdr", kdr)
    outfile.write(kdro)
    roto = "%s:%s" % ("rot", rot)
    outfile.write(roto)
    hsro = "%s:%s" % ("hsr", hsr)
    outfile.write(hsro)
    wlro = "%s:%s" % ("wlr", wlr)
    ourtilfe.write(wlro)
    lmwo = "%s:%s" % ("lmw", last_match_wins)
    outfile.write(lmwo)
    lmkdro = "%s:%s" % ("lmkdr", lmkdr)
    outfile.write(lmkdro)
    lmmo = "%s:%s" % ("lmm", last_match_mvps)
    outfile.write(lmmo)
    lmdo = "%s:%s" % ("lmd", last_match_damage)
    outfile.write(lmdo)
