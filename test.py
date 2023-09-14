import json

with open('sleeperPlayers.json') as f:
    data = json.load(f)
    print(data['7528']['espn_id'])