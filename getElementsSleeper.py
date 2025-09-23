import asyncio
import json
import requests
import certifi
import csv

def convertSleeperIdToEspn():
    mapping = {}
    with open("player_ids.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            mapping[row['sleeper_id']] = row['espn_id']
    return mapping

async def convertSleeperRosterToEspnIds(sleeperLeagueId):
    url = f'https://api.sleeper.app/v1/league/{sleeperLeagueId}/rosters'

    # Fetch the data
    response = requests.get(url, verify=False)
    sleeperRosters = response.json()  # This is your JSON object (parsed as Python list/dict)
    
    espnConvertedIds = {}
    sleeperMappedToEspnIds = convertSleeperIdToEspn()

    for team in sleeperRosters:
        if team['owner_id'] == '762559345467719680':
            espnConvertedIds['Justin'] = []
            dictTemp = set()
            for j in team['starters']:
                if(j == '0'):
                    continue
                espnConvertedIds['Justin'].append(sleeperMappedToEspnIds[j])
                dictTemp.add(j)
            for k in team['players']:
                if k not in dictTemp:
                    espnConvertedIds['Justin'].append(sleeperMappedToEspnIds[k])

        elif team['owner_id'] == '762564117293830144':
            espnConvertedIds['Matt'] = []
            dictTemp = set()
            for j in team['starters']:
                if(j == '0'):
                    continue
                espnConvertedIds['Matt'].append(sleeperMappedToEspnIds[j])
                dictTemp.add(j)
            for k in team['players']:
                if k not in dictTemp:
                    espnConvertedIds['Matt'].append(sleeperMappedToEspnIds[k])
        
        elif team['owner_id'] == '768036706015383552':
            espnConvertedIds['Ethan'] = []
            dictTemp = set()
            for j in team['starters']:
                if(j == '0'):
                    continue
                espnConvertedIds['Ethan'].append(sleeperMappedToEspnIds[j])
                dictTemp.add(j)
            for k in team['players']:
                if k not in dictTemp:
                    espnConvertedIds['Ethan'].append(sleeperMappedToEspnIds[k])

        elif team['owner_id'] == '768979142942302208':
            espnConvertedIds['Tiya'] = []
            dictTemp = set()
            for j in team['starters']:
                if(j == '0'):
                    continue
                espnConvertedIds['Tiya'].append(sleeperMappedToEspnIds[j])
                dictTemp.add(j)
            for k in team['players']:
                if k not in dictTemp:
                    espnConvertedIds['Tiya'].append(sleeperMappedToEspnIds[k])

        elif team['owner_id'] == '768352868104507392':
            espnConvertedIds['Kabir'] = []
            dictTemp = set()
            for j in team['starters']:
                if(j == '0'):
                    continue
                espnConvertedIds['Kabir'].append(sleeperMappedToEspnIds[j])
                dictTemp.add(j)
            for k in team['players']:
                if k not in dictTemp:
                    espnConvertedIds['Kabir'].append(sleeperMappedToEspnIds[k])

        elif team['owner_id'] == '465992895061553152':
            espnConvertedIds['Benny'] = []
            dictTemp = set()
            for j in team['starters']:
                if(j == '0'):
                    continue
                espnConvertedIds['Benny'].append(sleeperMappedToEspnIds[j])
                dictTemp.add(j)
            for k in team['players']:
                if k not in dictTemp:
                    espnConvertedIds['Benny'].append(sleeperMappedToEspnIds[k])

        elif team['owner_id'] == '474300335561633792':
            espnConvertedIds['Baker'] = []
            dictTemp = set()
            for j in team['starters']:
                if(j == '0'):
                    continue
                espnConvertedIds['Baker'].append(sleeperMappedToEspnIds[j])
                dictTemp.add(j)
            for k in team['players']:
                if k not in dictTemp:
                    espnConvertedIds['Baker'].append(sleeperMappedToEspnIds[k])

        elif team['owner_id'] == '768354602214375424':
            espnConvertedIds['Brady'] = []
            dictTemp = set()
            for j in team['starters']:
                if(j == '0'):
                    continue
                espnConvertedIds['Brady'].append(sleeperMappedToEspnIds[j])
                dictTemp.add(j)
            for k in team['players']:
                if k not in dictTemp:
                    espnConvertedIds['Brady'].append(sleeperMappedToEspnIds[k])

        elif team['owner_id'] == '768259545088016384':
            espnConvertedIds['Chris'] = []
            dictTemp = set()
            for j in team['starters']:
                if(j == '0'):
                    continue
                espnConvertedIds['Chris'].append(sleeperMappedToEspnIds[j])
                dictTemp.add(j)
            for k in team['players']:
                if k not in dictTemp:
                    espnConvertedIds['Chris'].append(sleeperMappedToEspnIds[k])

        elif team['owner_id'] == '768932331951149056':
            espnConvertedIds['Kingsley'] = []
            dictTemp = set()
            for j in team['starters']:
                if(j == '0'):
                    continue
                espnConvertedIds['Kingsley'].append(sleeperMappedToEspnIds[j])
                dictTemp.add(j)
            for k in team['players']:
                if k not in dictTemp:
                    espnConvertedIds['Kingsley'].append(sleeperMappedToEspnIds[k])
    
    return espnConvertedIds