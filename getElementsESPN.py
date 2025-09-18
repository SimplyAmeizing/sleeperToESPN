import json
import requests
from cookiesESPN import *
import time
from espn_api.football import League
import urllib3

def getRosterESPN():
    league = League(league_id=402922762, 
                    year=2025, 
                    espn_s2="AECP0LhuK3ctJxUubi%2Bvkt3Fx%2FyDPlm7ewHQPriGXgrQLIcCIsZoQKxBS5D0ktJvCLZPQ%2B0WVaaFeu4Q3HqXa7kql8zEY1FliVyTw99xWBn8X9v9j%2FOoqMzjp2C50tELPjGPxGpOkm%2FtTN%2BXCcjN%2F78T460r3rPFrt0gU%2FNwOFT8eoybJ7g08CU1Dz75Z%2FpVTpZRkKAodGGf9ulVLK91mLXmOh7zg%2BlyrKIku4mxiHRJ%2FWB%2B59uf53p%2FKdWOSnGlQhUp3zgzbkSRN%2FulR1wwfFvCDVDnxRBPwiX2A2KvQbtD8g%3D%3D", 
                    swid='{F53FF6DD-1278-4465-BF66-72F48AAA1569}'
                    )
    
    # Find the team you want

    tempArray = []
    for team in league.teams:
        temp = []
        for player in team.roster:
            temp.append(player.playerId)
        tempArray.append(temp)

    return tempArray

def dropAllPlayersESPN(weekNumber, playersArray):
    headers = {
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://fantasy.espn.com',
        'referer': 'https://fantasy.espn.com/',
        'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
        'x-fantasy-platform': 'kona-PROD-4bf5ad99065b78300041623712026402b4d5f9c1',
        'x-fantasy-source': 'kona'
    }
    for i in range(1, 11):
        json_data = {
            'isLeagueManager': True,
            'teamId': i,
            'type': 'ROSTER',
            'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
            'scoringPeriodId': weekNumber,
            'executionType': 'EXECUTE',
            'items': [],
            'isActingAsTeamOwner': False,
            'skipTransactionCounters': False,
        }

        for j in playersArray[i-1]:
            dictTemp = {}
            dictTemp['playerId'] = j
            dictTemp['type'] = "DROP"
            dictTemp['fromTeamId'] = i
            json_data['items'].append(dictTemp)
        
        #maybe it shouldn't be verify=false?
        requests.post('https://lm-api-writes.fantasy.espn.com/apis/v3/games/ffl/seasons/2025/segments/0/leagues/402922762/transactions/', cookies=cookiesESPN, json=json_data, headers=headers)
        
def addAllPlayersESPN(weekNumber, sleeperRoster, finalStarters):
    leagueTeamList = ["Justin", "Matt", "Ethan", "Tiya", "Kabir", "Benny", "Baker", "Brady", "Chris", "Kingsley"]

    for i in range(1, 11):
        headers = {
            'accept': 'application/json',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://fantasy.espn.com',
            'referer': 'https://fantasy.espn.com/',
            'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
            'x-fantasy-platform': 'kona-PROD-4bf5ad99065b78300041623712026402b4d5f9c1',
            'x-fantasy-source': 'kona'
        }


        for j in sleeperRoster[leagueTeamList[i-1]]:

            json_data = {
                'isLeagueManager': True,
                'teamId': i,
                'type': 'FREEAGENT',
                'scoringPeriodId': weekNumber,
                'executionType': 'EXECUTE',
                'items': [],
                'isActingAsTeamOwner': False,
                'skipTransactionCounters': False,
            }

            dictTemp = {}
            dictTemp['playerId'] = j
            dictTemp['type'] = "ADD"
            dictTemp['toTeamId'] = i
            json_data['items'].append(dictTemp)

            response = requests.post('https://lm-api-writes.fantasy.espn.com/apis/v3/games/ffl/seasons/2025/segments/0/leagues/402922762/transactions/', cookies=cookiesESPN, headers=headers, json=json_data)
            if response.status_code == 409:
                print(f"409 Conflict! Cooling down for 5 minutes...")
                # Status code
                print(f"Status Code: {response.status_code}")

                # Response headers
                print(f"Response Headers: {response.headers}")

                # Response content as text (decoded using inferred encoding)
                print(f"Response Text: {response.text[:200]}...") # Print first 200 characters

                # Response content as bytes
                print(f"Response Content (bytes): {response.content[:200]}...")
