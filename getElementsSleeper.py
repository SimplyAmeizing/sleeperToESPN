from selenium import webdriver
from selenium.webdriver.common.by import By
import asyncio
import json
import requests
from cookiesSleeper import *

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

async def queryLeagueDetail(weekNumber, finalStarters):
    url = "https://sleeper.com/graphql"

    headers = {
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9",
        "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdmF0YXIiOiJmMGVkYmY0Mjc4ZjUzZjk0MjVkYjE3NTA3M2RmNjU4NCIsImRpc3BsYXlfbmFtZSI6IlNpbXBseUFtZWl6aW5nIiwiZXhwIjoxNzIzOTMzMDk0LCJpYXQiOjE2OTIzOTcwOTQsImlzX2JvdCI6ZmFsc2UsImlzX21hc3RlciI6ZmFsc2UsInJlYWxfbmFtZSI6bnVsbCwidXNlcl9pZCI6NzY4MjU5NTQ1MDg4MDE2Mzg0LCJ2YWxpZF8yZmEiOiJwaG9uZSJ9.i0iRlGoCiba1e8tSaWHXzaDBMpU3M9JgK6PIB7IH0eA",  # Replace with your actual authorization token
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
        "query": "query get_league_detail { league_rosters(league_id: \"992182224076255232\") { league_id metadata owner_id co_owners players roster_id settings starters keepers reserve taxi player_map } league_users(league_id: \"992182224076255232\") { avatar user_id league_id metadata settings display_name is_owner is_bot } league_transactions_filtered(league_id: \"992182224076255232\", roster_id_filters: [], type_filters: [], leg_filters: [], status_filters: [\"pending\",\"proposed\"]) { adds consenter_ids created creator draft_picks drops league_id leg metadata roster_ids settings status status_updated transaction_id type player_map waiver_budget } matchup_legs_" + str(weekNumber) + ":matchup_legs(league_id: \"992182224076255232\", round:" + str(weekNumber) + ") { league_id leg matchup_id roster_id round starters players player_map points proj_points max_points custom_points starters_games picks bans } }"
    }

    response = requests.post(url, headers=headers, json=payload)

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

        return finalRes
        
    else:
        print(f"Request failed with status code: {response.status_code}")
        return "failed"