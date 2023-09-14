import json
import requests
from cookies import *
import time

def getRosterESPN(weekNumber):

    for k in range (1,11):
        cookies = cookiesESPN

        url = "https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/2023/segments/0/leagues/1908531039?rosterForTeamId=" + str(k) + "&view=mDraftDetail&view=mLiveScoring&view=mMatchupScore&view=mPendingTransactions&view=mPositionalRatings&view=mRoster&view=mSettings&view=mTeam&view=modular&view=mNav"
        headers = {
            'authority': 'lm-api-reads.fantasy.espn.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'if-none-match': 'W/"020743c848663f4e73f80d25f54a6a9bd"',
            'origin': 'https://fantasy.espn.com',
            'referer': 'https://fantasy.espn.com/',
            'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
            'x-fantasy-filter': '{"players":{}}',
            'x-fantasy-platform': 'kona-PROD-52ef5dee942a41adf22628f67f5e63b1f734fdd1',
            'x-fantasy-source': 'kona',
        }

        response = requests.get(url, headers=headers, cookies=cookiesESPN, verify=False)

        finalArray = [None] * 10
        if response.status_code == 200:
            json_data = response.json()
            schedule = json_data.get('schedule')
            
            if schedule:
                indexer = (int(weekNumber) * 5) - 5

                for i in range(indexer, int(weekNumber)*5):
                    away_roster = schedule[i].get('away', {}).get('rosterForCurrentScoringPeriod', {}).get('entries')
                    team_id_away = schedule[i].get('away').get('teamId')

                    tempArray_away = []
                    for j in away_roster:
                        tempArray_away.append(j['playerId'])
                    
                    finalArray[team_id_away-1] = tempArray_away

                    
                    home_roster = schedule[i].get('home', {}).get('rosterForCurrentScoringPeriod', {}).get('entries')
                    team_id_home = schedule[i].get('home').get('teamId')

                    tempArray_home = []
                    for j in home_roster:
                        tempArray_home.append(j['playerId'])
                    
                    finalArray[team_id_home-1] = tempArray_home
                    
            else:
                print("No schedule data in the JSON response.")
        else:
            print(response)
            print("Request failed with status code:", response.status_code)

    return finalArray


def dropAllPlayersESPN(weekNumber, playersArray):
    headers = {
    'authority': 'lm-api-writes.fantasy.espn.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://fantasy.espn.com',
    'referer': 'https://fantasy.espn.com/',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'x-fantasy-platform': 'kona-PROD-52ef5dee942a41adf22628f67f5e63b1f734fdd1',
    'x-fantasy-source': 'kona',
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
        requests.post('https://lm-api-writes.fantasy.espn.com/apis/v3/games/ffl/seasons/2023/segments/0/leagues/1908531039/transactions/', cookies=cookiesESPN, headers=headers, json=json_data, verify=False)

def addAllPlayersESPN(weekNumber, sleeperRoster):
    
    for i in range(1, 11):
        headers = {
        'Connection': 'keep-alive',
        'Origin': 'https://fantasy.espn.com',
        'Referer': 'https://fantasy.espn.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'x-fantasy-platform': 'kona-PROD-52ef5dee942a41adf22628f67f5e63b1f734fdd1',
        'x-fantasy-source': 'kona',
        }

        if i == 5:
            time.sleep(120)
        elif i == 8:
            time.sleep(120)

        for j in sleeperRoster[i-1]:
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

            response = requests.post('https://lm-api-writes.fantasy.espn.com/apis/v3/games/ffl/seasons/2023/segments/0/leagues/1908531039/transactions/', cookies=cookiesESPN, headers=headers, json=json_data, verify=False)