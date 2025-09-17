from selenium import webdriver
from selenium.webdriver.common.by import By
import asyncio
import json
import requests
from cookiesSleeper import *
import certifi
import csv

async def findAndSendUserName(driver, username):
    input_element1 = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
    input_element1.send_keys(username)

async def findAndSendPassword(driver, password):
    input_element2 = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    input_element2.send_keys(password)

async def SubmitUsername(driver, username):
    await findAndSendUserName(driver, username)
    click_element = driver.find_element(By.CLASS_NAME, "app-button-gradient.login-button")
    click_element.click()

async def SubmitPassword(driver, username):
    await findAndSendPassword(driver, username)
    click_element = driver.find_element(By.CLASS_NAME, "app-button-gradient.login-button")
    click_element.click()

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
            for j in team['players']:
                espnConvertedIds['Justin'].append(sleeperMappedToEspnIds[j])

        elif team['owner_id'] == '762564117293830144':
            espnConvertedIds['Matt'] = []
            for j in team['players']:
                espnConvertedIds['Matt'].append(sleeperMappedToEspnIds[j])
        
        elif team['owner_id'] == '768036706015383552':
            espnConvertedIds['Ethan'] = []
            for j in team['players']:
                espnConvertedIds['Ethan'].append(sleeperMappedToEspnIds[j])

        elif team['owner_id'] == '768979142942302208':
            espnConvertedIds['Tiya'] = []
            for j in team['players']:
                espnConvertedIds['Tiya'].append(sleeperMappedToEspnIds[j])

        elif team['owner_id'] == '768352868104507392':
            espnConvertedIds['Kabir'] = []
            for j in team['players']:
                espnConvertedIds['Kabir'].append(sleeperMappedToEspnIds[j])

        elif team['owner_id'] == '465992895061553152':
            espnConvertedIds['Benny'] = []
            for j in team['players']:
                espnConvertedIds['Benny'].append(sleeperMappedToEspnIds[j])

        elif team['owner_id'] == '474300335561633792':
            espnConvertedIds['Baker'] = []
            for j in team['players']:
                espnConvertedIds['Baker'].append(sleeperMappedToEspnIds[j])

        elif team['owner_id'] == '768354602214375424':
            espnConvertedIds['Brady'] = []
            for j in team['players']:
                espnConvertedIds['Brady'].append(sleeperMappedToEspnIds[j])

        elif team['owner_id'] == '768259545088016384':
            espnConvertedIds['Chris'] = []
            for j in team['players']:
                espnConvertedIds['Chris'].append(sleeperMappedToEspnIds[j])

        elif team['owner_id'] == '768932331951149056':
            espnConvertedIds['Kingsley'] = []
            for j in team['players']:
                espnConvertedIds['Kingsley'].append(sleeperMappedToEspnIds[j])
        
    return espnConvertedIds

async def queryLeagueDetail(weekNumber, finalStarters):
    url = "https://sleeper.com/graphql"

    headers = {
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9",
        #authorization is only one we need to replace
        "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdmF0YXIiOiJmMGVkYmY0Mjc4ZjUzZjk0MjVkYjE3NTA3M2RmNjU4NCIsImRpc3BsYXlfbmFtZSI6IlNpbXBseUFtZWl6aW5nIiwiZXhwIjoxNzg5NTc2ODczLCJpYXQiOjE3NTgwNDA4NzMsImlzX2JvdCI6ZmFsc2UsImlzX21hc3RlciI6ZmFsc2UsInJlYWxfbmFtZSI6bnVsbCwidXNlcl9pZCI6NzY4MjU5NTQ1MDg4MDE2Mzg0LCJ2YWxpZF8yZmEiOiIifQ.236Wr0R19VYDQdTP5mbBdg_i2JDyCokH8e4eN0h5CtQ",  # Replace with your actual authorization token
        "content-type": "application/json",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin"
    }

    payload = {
        "operationName": "get_league_detail",
        "variables": {},
        #replace this yearly
        "query": "query get_league_detail {\n        \n    league_rosters(league_id: \"1255956974311321600\"){\n      league_id\n      metadata\n      owner_id\n      co_owners\n      players\n      roster_id\n      settings\n      starters\n      keepers\n      reserve\n      taxi\n      player_map\n    }\n  \n        \n      league_users(league_id: \"1255956974311321600\"){\n        avatar\n        user_id\n        league_id\n        metadata\n        settings\n        display_name\n        is_owner\n        is_bot\n      }\n  \n        \n      league_transactions_filtered(league_id: \"1255956974311321600\",roster_id_filters: [],type_filters: [],leg_filters: [],status_filters: [\"pending\",\"proposed\"]){\n        adds\n        consenter_ids\n        created\n        creator\n        draft_picks\n        drops\n        league_id\n        leg\n        metadata\n        roster_ids\n        settings\n        status\n        status_updated\n        transaction_id\n        type\n        player_map\n        waiver_budget\n      }\n  \n        \n      matchup_legs_3:matchup_legs(league_id: \"1255956974311321600\",round: 3){\n        league_id\n        leg\n        matchup_id\n        roster_id\n        round\n        starters\n        players\n        player_map\n        points\n        proj_points\n        max_points\n        custom_points\n        starters_games\n        picks\n        bans\n        subs\n      }\n    \n        \n      }"
    }

    response = requests.post(url, headers=headers, json=payload, verify=False)

    if response.status_code == 200:
        data = response.json()
        
        count = 0
        with open('sleeperPlayers.json') as f:
            jsonData = json.load(f)
            matchup = "matchup_legs_" + weekNumber

            players = [None] * 10
            starters = [None] * 10

            for i in data['data'][matchup]:
                tempArray = []
                tempArray1 = []
                for j in i['players']:
                    if (j == '0'):
                        continue

                    if('espn_id' not in jsonData[j]):
                        total_name = jsonData[j]['last_name'] + ' D/ST'
                        tempArray.append(total_name)

                    elif(jsonData[j]['espn_id'] != None):
                        tempArray.append(jsonData[j]['espn_id'])

                    else:
                        tempArray.append(jsonData[j]['full_name'])
                
                for k in i['starters']:
                    if (k == '0'):
                        continue

                    elif('espn_id' not in jsonData[k]):
                        total_name = jsonData[k]['last_name'] + ' D/ST'
                        tempArray1.append(total_name)

                    elif(jsonData[k]['espn_id'] != None):
                        tempArray1.append(jsonData[k]['espn_id'])

                    else:
                        tempArray1.append(jsonData[k]['full_name'])

                if(i['roster_id'] == 1):#Justin
                    players[4] = tempArray
                    starters[4] = tempArray1

                elif(i['roster_id'] == 2):#Matt
                    players[5] = tempArray
                    starters[5] = tempArray1

                elif(i['roster_id'] == 3):#Ethan
                    players[7] = tempArray
                    starters[7] = tempArray1

                elif(i['roster_id'] == 4):#Tiya
                    players[3] = tempArray
                    starters[3] = tempArray1

                elif(i['roster_id'] == 5):#Kabir
                    players[6] = tempArray
                    starters[6] = tempArray1

                elif(i['roster_id'] == 6):#Benny
                    players[8] = tempArray
                    starters[8] = tempArray1

                elif(i['roster_id'] == 7):#Baker
                    players[9] = tempArray
                    starters[9] = tempArray1

                elif(i['roster_id'] == 8):#Brady
                    players[1] = tempArray
                    starters[1] = tempArray1

                elif(i['roster_id'] == 9):#Chris
                    players[0] = tempArray
                    starters[0] = tempArray1

                elif(i['roster_id'] == 10):#Kingsley
                    players[2] = tempArray
                    starters[2] = tempArray1

        finalRes = []
        with open('espnPlayers.json') as f:
            jsonData = json.load(f)
            for i in players:
                tempArray = []
                for j in i:
                    if(isinstance(j, int)):
                        tempArray.append(j)
                        continue
                    else:
                        for item in jsonData:
                            if item["fullName"] == j:
                                tempArray.append(item['id'])

                finalRes.append(tempArray)
            
            for i in starters:
                tempDict = set()
                for j in i:
                    if(isinstance(j, int)):
                        tempDict.add(j)
                        continue
                    else:
                        for item in jsonData:
                            if item["fullName"] == j:
                                tempDict.add(item['id'])

                finalStarters.append(tempDict)

        print(finalStarters)
        return finalRes
        
    else:
        print(f"Request failed with status code: {response.status_code}")
        return "failed"