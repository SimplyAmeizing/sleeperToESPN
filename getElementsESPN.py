import json
import requests
from cookiesESPN import *
import time
from espn_api.football import League
import urllib3
from models.player import Player
from datetime import datetime, timezone, timedelta
import pytz
import sys

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

def getPlayedArray(weekNumber):
    league = League(league_id=402922762, 
                    year=2025, 
                    espn_s2="AECP0LhuK3ctJxUubi%2Bvkt3Fx%2FyDPlm7ewHQPriGXgrQLIcCIsZoQKxBS5D0ktJvCLZPQ%2B0WVaaFeu4Q3HqXa7kql8zEY1FliVyTw99xWBn8X9v9j%2FOoqMzjp2C50tELPjGPxGpOkm%2FtTN%2BXCcjN%2F78T460r3rPFrt0gU%2FNwOFT8eoybJ7g08CU1Dz75Z%2FpVTpZRkKAodGGf9ulVLK91mLXmOh7zg%2BlyrKIku4mxiHRJ%2FWB%2B59uf53p%2FKdWOSnGlQhUp3zgzbkSRN%2FulR1wwfFvCDVDnxRBPwiX2A2KvQbtD8g%3D%3D", 
                    swid='{F53FF6DD-1278-4465-BF66-72F48AAA1569}'
                    )

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

    playedArray = {}
    box = league.box_scores(int(weekNumber))
    teamConversion = {
        "Team(Ben)" : 6,
        "Team(Tiya)" : 4,
        "Team(Han)" : 1,
        "Team(Kings)" : 10,
        "Team(Chris)" : 9,
        "Team(Pardue)": 8,
        "Team(Bakes)" : 7,
        "Team(Matt)" : 2,
        "Team(Ethan)" : 3,
        "Team(Kabir)" : 5
    }

    for matchup in box:
        for player in matchup.home_lineup:
            playedArray[player.playerId] = player.position
            if player.lineupSlot != "BE":
                if player.lineupSlot == "QB":
                    json_data = {
                        'isLeagueManager': True,
                        'teamId': teamConversion[str(matchup.home_team)],
                        'type': 'ROSTER',
                        'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                        'scoringPeriodId': weekNumber,
                        'executionType': 'EXECUTE',
                        'items': [
                            {
                                'playerId': player.playerId,
                                'type': 'LINEUP',
                                'fromLineupSlotId': 0,
                                'toLineupSlotId': 20
                            },
                        ],
                    }
                if player.lineupSlot == "RB":
                    json_data = {
                        'isLeagueManager': True,
                        'teamId': teamConversion[str(matchup.home_team)],
                        'type': 'ROSTER',
                        'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                        'scoringPeriodId': weekNumber,
                        'executionType': 'EXECUTE',
                        'items': [
                            {
                                'playerId': player.playerId,
                                'type': 'LINEUP',
                                'fromLineupSlotId': 2,
                                'toLineupSlotId': 20
                            },
                        ],
                    }
                if player.lineupSlot == "WR":
                    json_data = {
                        'isLeagueManager': True,
                        'teamId': teamConversion[str(matchup.home_team)],
                        'type': 'ROSTER',
                        'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                        'scoringPeriodId': weekNumber,
                        'executionType': 'EXECUTE',
                        'items': [
                            {
                                'playerId': player.playerId,
                                'type': 'LINEUP',
                                'fromLineupSlotId': 4,
                                'toLineupSlotId': 20
                            },
                        ],
                    }

                if player.lineupSlot == "RB/WR/TE":
                    json_data = {
                        'isLeagueManager': True,
                        'teamId': teamConversion[str(matchup.home_team)],
                        'type': 'ROSTER',
                        'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                        'scoringPeriodId': weekNumber,
                        'executionType': 'EXECUTE',
                        'items': [
                            {
                                'playerId': player.playerId,
                                'type': 'LINEUP',
                                'fromLineupSlotId': 23,
                                'toLineupSlotId': 20
                            },
                        ],
                    }

                if player.lineupSlot == "TE":
                    json_data = {
                        'isLeagueManager': True,
                        'teamId': teamConversion[str(matchup.home_team)],
                        'type': 'ROSTER',
                        'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                        'scoringPeriodId': weekNumber,
                        'executionType': 'EXECUTE',
                        'items': [
                            {
                                'playerId': player.playerId,
                                'type': 'LINEUP',
                                'fromLineupSlotId': 6,
                                'toLineupSlotId': 20
                            },
                        ],
                    }

                if player.lineupSlot == "D/ST":
                    json_data = {
                        'isLeagueManager': True,
                        'teamId': teamConversion[str(matchup.home_team)],
                        'type': 'ROSTER',
                        'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                        'scoringPeriodId': weekNumber,
                        'executionType': 'EXECUTE',
                        'items': [
                            {
                                'playerId': player.playerId,
                                'type': 'LINEUP',
                                'fromLineupSlotId': 16,
                                'toLineupSlotId': 20
                            },
                        ],
                    }

                if player.lineupSlot == "K":
                    json_data = {
                        'isLeagueManager': True,
                        'teamId': teamConversion[str(matchup.home_team)],
                        'type': 'ROSTER',
                        'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                        'scoringPeriodId': weekNumber,
                        'executionType': 'EXECUTE',
                        'items': [
                            {
                                'playerId': player.playerId,
                                'type': 'LINEUP',
                                'fromLineupSlotId': 17,
                                'toLineupSlotId': 20
                            },
                        ],
                    }
                
                response = requests.post('https://lm-api-writes.fantasy.espn.com/apis/v3/games/ffl/seasons/2025/segments/0/leagues/402922762/transactions/', cookies=cookiesESPN, headers=headers, json=json_data)
    
        for player in matchup.away_lineup:
            playedArray[player.playerId] = player.position
            if player.lineupSlot != "BE":
                if player.lineupSlot == "QB":
                    json_data = {
                        'isLeagueManager': True,
                        'teamId': teamConversion[str(matchup.away_team)],
                        'type': 'ROSTER',
                        'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                        'scoringPeriodId': weekNumber,
                        'executionType': 'EXECUTE',
                        'items': [
                            {
                                'playerId': player.playerId,
                                'type': 'LINEUP',
                                'fromLineupSlotId': 0,
                                'toLineupSlotId': 20
                            },
                        ],
                    }
                if player.lineupSlot == "RB":
                    json_data = {
                        'isLeagueManager': True,
                        'teamId': teamConversion[str(matchup.away_team)],
                        'type': 'ROSTER',
                        'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                        'scoringPeriodId': weekNumber,
                        'executionType': 'EXECUTE',
                        'items': [
                            {
                                'playerId': player.playerId,
                                'type': 'LINEUP',
                                'fromLineupSlotId': 2,
                                'toLineupSlotId': 20
                            },
                        ],
                    }
                if player.lineupSlot == "WR":
                    json_data = {
                        'isLeagueManager': True,
                        'teamId': teamConversion[str(matchup.away_team)],
                        'type': 'ROSTER',
                        'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                        'scoringPeriodId': weekNumber,
                        'executionType': 'EXECUTE',
                        'items': [
                            {
                                'playerId': player.playerId,
                                'type': 'LINEUP',
                                'fromLineupSlotId': 4,
                                'toLineupSlotId': 20
                            },
                        ],
                    }

                if player.lineupSlot == "RB/WR/TE":
                    json_data = {
                        'isLeagueManager': True,
                        'teamId': teamConversion[str(matchup.away_team)],
                        'type': 'ROSTER',
                        'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                        'scoringPeriodId': weekNumber,
                        'executionType': 'EXECUTE',
                        'items': [
                            {
                                'playerId': player.playerId,
                                'type': 'LINEUP',
                                'fromLineupSlotId': 23,
                                'toLineupSlotId': 20
                            },
                        ],
                    }

                if player.lineupSlot == "TE":
                    json_data = {
                        'isLeagueManager': True,
                        'teamId': teamConversion[str(matchup.away_team)],
                        'type': 'ROSTER',
                        'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                        'scoringPeriodId': weekNumber,
                        'executionType': 'EXECUTE',
                        'items': [
                            {
                                'playerId': player.playerId,
                                'type': 'LINEUP',
                                'fromLineupSlotId': 6,
                                'toLineupSlotId': 20
                            },
                        ],
                    }

                if player.lineupSlot == "D/ST":
                    json_data = {
                        'isLeagueManager': True,
                        'teamId': teamConversion[str(matchup.away_team)],
                        'type': 'ROSTER',
                        'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                        'scoringPeriodId': weekNumber,
                        'executionType': 'EXECUTE',
                        'items': [
                            {
                                'playerId': player.playerId,
                                'type': 'LINEUP',
                                'fromLineupSlotId': 16,
                                'toLineupSlotId': 20
                            },
                        ],
                    }

                if player.lineupSlot == "K":
                    json_data = {
                        'isLeagueManager': True,
                        'teamId': teamConversion[str(matchup.away_team)],
                        'type': 'ROSTER',
                        'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                        'scoringPeriodId': weekNumber,
                        'executionType': 'EXECUTE',
                        'items': [
                            {
                                'playerId': player.playerId,
                                'type': 'LINEUP',
                                'fromLineupSlotId': 17,
                                'toLineupSlotId': 20
                            },
                        ],
                    }
                
                response = requests.post('https://lm-api-writes.fantasy.espn.com/apis/v3/games/ffl/seasons/2025/segments/0/leagues/402922762/transactions/', cookies=cookiesESPN, headers=headers, json=json_data)
                    
    print(sys.getsizeof(playedArray))
    return playedArray

def setLineupESPN(weekNumber, espnPlayers, playedArray):
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

        rb_count = 0
        wr_count = 0
        count = 0
        for j in espnPlayers[leagueTeamList[i-1]]:
            if int(j) in playedArray:
                if playedArray[int(j)] == "QB":
                    json_data = {
                        'isLeagueManager': True,
                        'teamId': i,
                        'type': 'ROSTER',
                        'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                        'scoringPeriodId': weekNumber,
                        'executionType': 'EXECUTE',
                        'items': [
                            {
                                'playerId': j,
                                'type': 'LINEUP',
                                'fromLineupSlotId': 20,
                                'toLineupSlotId': 0
                            },
                        ],
                    }
                elif playedArray[int(j)] == "RB" and rb_count < 2:
                    json_data = {
                        'isLeagueManager': True,
                        'teamId': i,
                        'type': 'ROSTER',
                        'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                        'scoringPeriodId': weekNumber,
                        'executionType': 'EXECUTE',
                        'items': [
                            {
                                'playerId': j,
                                'type': 'LINEUP',
                                'fromLineupSlotId': 20,
                                'toLineupSlotId': 2
                            },
                        ],
                    }
                    rb_count += 1

                elif playedArray[int(j)] == "WR" and wr_count < 2:
                    json_data = {
                        'isLeagueManager': True,
                        'teamId': i,
                        'type': 'ROSTER',
                        'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                        'scoringPeriodId': weekNumber,
                        'executionType': 'EXECUTE',
                        'items': [
                            {
                                'playerId': j,
                                'type': 'LINEUP',
                                'fromLineupSlotId': 20,
                                'toLineupSlotId': 4
                            },
                        ],
                    }
                    wr_count += 1
                
                elif (playedArray[int(j)] == "WR" and wr_count == 2) or (playedArray[int(j)] == "RB" and rb_count==2):
                    json_data = {
                        'isLeagueManager': True,
                        'teamId': i,
                        'type': 'ROSTER',
                        'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                        'scoringPeriodId': weekNumber,
                        'executionType': 'EXECUTE',
                        'items': [
                            {
                                'playerId': j,
                                'type': 'LINEUP',
                                'fromLineupSlotId': 20,
                                'toLineupSlotId': 23
                            },
                        ],
                    }

                elif playedArray[int(j)] == "TE":
                    json_data = {
                        'isLeagueManager': True,
                        'teamId': i,
                        'type': 'ROSTER',
                        'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                        'scoringPeriodId': weekNumber,
                        'executionType': 'EXECUTE',
                        'items': [
                            {
                                'playerId': j,
                                'type': 'LINEUP',
                                'fromLineupSlotId': 20,
                                'toLineupSlotId': 6
                            },
                        ],
                    }

                elif playedArray[int(j)] == "D/ST":
                    json_data = {
                        'isLeagueManager': True,
                        'teamId': i,
                        'type': 'ROSTER',
                        'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                        'scoringPeriodId': weekNumber,
                        'executionType': 'EXECUTE',
                        'items': [
                            {
                                'playerId': j,
                                'type': 'LINEUP',
                                'fromLineupSlotId': 20,
                                'toLineupSlotId': 16
                            },
                        ],
                    }

                elif playedArray[int(j)] == "K":
                    json_data = {
                        'isLeagueManager': True,
                        'teamId': i,
                        'type': 'ROSTER',
                        'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                        'scoringPeriodId': weekNumber,
                        'executionType': 'EXECUTE',
                        'items': [
                            {
                                'playerId': j,
                                'type': 'LINEUP',
                                'fromLineupSlotId': 20,
                                'toLineupSlotId': 17
                            },
                        ],
                    }

                count += 1
                response = requests.post('https://lm-api-writes.fantasy.espn.com/apis/v3/games/ffl/seasons/2025/segments/0/leagues/402922762/transactions/', cookies=cookiesESPN, headers=headers, json=json_data)


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
        
def addAllPlayersESPN(weekNumber, sleeperRoster):
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
