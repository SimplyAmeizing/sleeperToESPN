import requests
from cookies import *

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

        response = requests.get(url, headers=headers, cookies=cookiesESPN)

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

    print(finalArray)
    return finalArray


def dropAllPlayersESPN():
    headers = {
    'authority': 'lm-api-writes.fantasy.espn.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'cookie': 's_ecid=MCMID%7C07674328463150203593883664827359665918; _cc_id=c499a743204e92478f690c335c0b5dc5; _gcl_au=1.1.1550799294.1693860936; _cb=DD0ed_B8uzI3CevLH6; _fbp=fb.1.1693860939475.2086035205; device_f1259fe1=b9ee777d-3446-4581-817a-8c89a59e8a4d; SWID={F53FF6DD-1278-4465-BF66-72F48AAA1569}; ESPN-ONESITE.WEB-PROD-ac=XUS; espnAuth={"swid":"{F53FF6DD-1278-4465-BF66-72F48AAA1569}"}; s_fid=6A0809F37C95BA3E-0806A23974686AC6; ctoLocalVisitor={%22localVisitorId%22:%221693863166165-214673225344%22}; ctoVisitor={%22firstPageName%22:%22dgame:espn:homepage%20/%20category:Draft%22%2C%22firstRefUrl%22:%22na%22%2C%22firstUrl%22:%22https://support.espn.com/hc/en-us/sections/360000355371-Draft%22%2C%22sessionCount%22:3}; connectId={"lastUsed":1694491845721,"lastSynced":1694491845721}; panoramaId_expiry=1695096646119; panoramaId=0da36756000cff50ce39a84e6f7d16d5393813331b27d79d5ecfb3d17700b530; panoramaIdType=panoIndiv; tvid=f397d71b43e34220be806ac729d3d89e; _ga=GA1.1.339139746.1694491952; _ga_H0P43ZY447=GS1.1.1694491951.1.1.1694492272.0.0.0; device_67d7288d=cced75f6-ecf4-4bd0-9aa0-2ed1c88b9e14; tveAuth=; tveMVPDAuth=; s_nr=1694580271946-Repeat; cto_bundle=61aZSF9qOGJoJTJCS2RjTyUyRnF5JTJCM3E2TzdLOThRdDE0WEUlMkJMRHA5dFVqMG9iQThPbDdGMXgyV1VFOE5KU3BFUTQ0MExVODA1RFRselU3ZCUyQjRpNmhvV1RlbVdDcCUyQnRiNmh3Z1ZHOEFRcWQlMkJmQTFFJTJCb1l0M2t2RFVIdjBYJTJCVUlWM2NvdGZEMmkzZWRaZVVNYTFiMlRUTkc0R2olMkZ6MGI3azZZQWhZVk5VbU02ZFJLQlc3QW5FaXFmNjU5bThkdWNMenpSJTJGQ1lpWmtsYXJsSmFUQlA1eGtERkElMkJ2TVlnJTNEJTNE; ESPN-ONESITE.WEB-PROD.token=5=eyJhY2Nlc3NfdG9rZW4iOiJhNDg1ZTc0OGQ4YjY0NTBkYTgzOWNlNWMxYTI1MWU3MiIsInJlZnJlc2hfdG9rZW4iOiJlNzk2NjcyZjVjZjg0ZGQ2YTcxNTA5YzZmZDc3ZDY4MiIsInN3aWQiOiJ7RjUzRkY2REQtMTI3OC00NDY1LUJGNjYtNzJGNDhBQUExNTY5fSIsInR0bCI6ODY0MDAsInJlZnJlc2hfdHRsIjoxNTU1MjAwMCwiaGlnaF90cnVzdF9leHBpcmVzX2luIjpudWxsLCJpbml0aWFsX2dyYW50X2luX2NoYWluX3RpbWUiOjE2OTQ0OTU4NDY0NzMsImlhdCI6MTY5NDY1OTI2OTAwMCwiZXhwIjoxNjk0NzQ1NjY5MDAwLCJyZWZyZXNoX2V4cCI6MTcxMDIxMTI2OTAwMCwiaGlnaF90cnVzdF9leHAiOm51bGwsInNzbyI6bnVsbCwiYXV0aGVudGljYXRvciI6ImRpc25leWlkIiwibG9naW5WYWx1ZSI6bnVsbCwiY2xpY2tiYWNrVHlwZSI6bnVsbCwic2Vzc2lvblRyYW5zZmVyS2V5IjoiTy1CRGZweE55M1djVWg0cF9WTXpTTTdJNjZlamFEMkhoTkRTM3c4MXk0Z1F5QlVucXN3R3lNeW9JOVBkYnQwS1c0NWhOd3RzQldoN0VpSEc3N3V3ZkpkYk9lNWVkcXNENHFXVFlHZzNPamN2Um4tTmpsRSIsImNyZWF0ZWQiOiIyMDIzLTA5LTE0VDAyOjQxOjA4Ljc0M1oiLCJsYXN0Q2hlY2tlZCI6IjIwMjMtMDktMTRUMDI6NDE6MDguNzQzWiIsImV4cGlyZXMiOiIyMDIzLTA5LTE1VDAyOjQxOjA5LjAwMFoiLCJyZWZyZXNoX2V4cGlyZXMiOiIyMDI0LTAzLTEyVDAyOjQxOjA5LjAwMFoifQ==|eyJraWQiOiJxUEhmditOL0tONE1zYnVwSE1PWWxBc0pLcWVaS1U2Mi9DZjNpSm1uOEJ6dzlwSW5xbTVzUnc9PSIsImFsZyI6IlJTMjU2In0.eyJpc3MiOiJodHRwczovL2F1dGhvcml6YXRpb24uZ28uY29tIiwic3ViIjoie0Y1M0ZGNkRELTEyNzgtNDQ2NS1CRjY2LTcyRjQ4QUFBMTU2OX0iLCJhdWQiOiJFU1BOLU9ORVNJVEUuV0VCLVBST0QiLCJleHAiOjE2OTQ3NDU2NjksImlhdCI6MTY5NDY1OTI2OSwianRpIjoieXdadXVXeThSR09yQ2lSUjFuV01zZyIsIm5iZiI6MTY5NDY1OTIwOSwiYV90eXAiOiJPTkVJRF9UUlVTVEVEIiwiYV9jYXQiOiJHVUVTVCIsImF0ciI6ImRpc25leWlkIiwic2NvcGVzIjpbIkFVVEhaX0dVRVNUX1NFQ1VSRURfU0VTU0lPTiJdLCJjX3RpZCI6IjEzMjQiLCJpZ2ljIjoxNjk0NDk1ODQ2NDczLCJodGF2IjoyLCJodGQiOjE4MDAsInJ0dGwiOjE1NTUyMDAwLCJlbWFpbCI6ImNocmlzbWVpdHhAZ21haWwuY29tIn0.Af6C2rdWr0XQpME6f3dh3L5Vs8jYMpWch1b2XVWEbbUfF9XhNE8ZRRDCH5Yxc6xT6PIwzAm9HMN_w9H9YQ2Ik6wOKhm8ywcs1WvYUxT9U8QrRKxUdqf4cnkb8ghe8xy5duzKqL0hgxkmRnC23ABIoghT1ezNhsrrC5NtKbaURWJkH1B9g0afNMbAW6ZRS7ZnzD7cjQNL2ltgjMI0WENuBV_Xfzcy1aMOeKlVtvlckZkXwo1iMcUYgzb8vRSJz_QqTMtYAOq8_mgRlsmGTpX2Dfn8kfLdAOeXMlgZYW6EI0l_DMC1noPgiEQsFo_qLw44eWIpuJw1KROwdU4M_-v6eQ; nol_fpid=ufdxdbizg6pewgk5hxjayylgexdoo1693863047|1693863047779|1694667591961|1694667591963; check=true; mbox=PC#16bca791b25f42599d4fdbe3e76fac44.34_0#1757947567|session#274a91d925844f52801a2060b8600243#1694704627; mboxEdgeCluster=34; userZip=23221; _omnicwtest=works; __gads=ID=526c880626ba46b2:T=1693860933:RT=1694702769:S=ALNI_MahYJI_c1rEgNv6fEepJQFQj_DDlA; __gpi=UID=00000d8fe6880a74:T=1693860933:RT=1694702769:S=ALNI_MYIy3EeSdRn1rJ13tcbom8DUOONHQ; AMCVS_EE0201AC512D2BE80A490D4C%40AdobeOrg=1; AMCV_EE0201AC512D2BE80A490D4C%40AdobeOrg=-330454231%7CMCIDTS%7C19615%7CMCMID%7C07674328463150203593883664827359665918%7CMCAAMLH-1695307574%7C7%7CMCAAMB-1695307574%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1694709974s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.1.2; s_c24_s=Less%20than%201%20day; s_cc=true; IR_gbd=espn.com; block.check=false%7Cfalse; _cb_svref=https%3A%2F%2Fwww.espn.com%2F; s_omni_lid=%5B%5BB%5D%5D; s_ensNR=1694702900816-Repeat; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Sep+14+2023+10%3A48%3A21+GMT-0400+(Eastern+Daylight+Time)&version=202212.1.0&isIABGlobal=false&hosts=&consentId=7b243501-a6d8-40b7-bc82-c0446f764e7d&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CSSPD_BG%3A1%2CC0002%3A1%2CC0004%3A1%2CC0005%3A1&AwaitingReconsent=false; IR_9070=1694702901272%7C0%7C1694702901272%7C%7C; _chartbeat5=; _chartbeat2=.1667115110227.1694702907223.0000010000000111.DlK86QBSmfx5BXobULBZNyDdC2YSZB.4; s_gpv_pn=fantasy%3Afootball%3Aleague%3Almdropplayers; s_c6=1694702907767-Repeat; espn_s2=AEBhDeIViqT%2Bq4GMEVcfq18bLQJMQw%2FDOnEODkCCt36%2FmOGSOEq%2BXQuIJoXHBM%2F2K%2Fgbvma6Idd%2FidmpwXpktXbob3AQeyOsN5xtoxdjL716geqJHYqhJY9bD%2FvxDVbeJ700WnA7h%2FedCEuv2Aq7mnuzZw5eB08QjIHF5a8pvAJuHbBSyP%2FnDmhHLllPXEU%2F6vzbkorVmApzUD6ZLzygRD6rftBthDr%2Bj3nbpl20zFZva%2FJrMlGpzSdOIJV2q6HlZFiq4y%2Fel%2FG792nh36sVVqgQ7wsOhA8hLzc%2BOuXMY%2FOdbA%3D%3D; ESPN-ONESITE.WEB-PROD.idn=00efb0ac69; s_sq=wdgespcom%252Cwdgespge%3D%2526pid%253Dfantasy%25253Afootball%25253Aleague%25253Almdropplayers%2526pidt%253D1%2526oid%253Dfunctionvr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSUBMIT; s_c24=1694702918470',
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

json_data = {
    'isLeagueManager': True,
    'teamId': 2,
    'type': 'ROSTER',
    'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
    'scoringPeriodId': 2,
    'executionType': 'EXECUTE',
    'items': [
        {
            'playerId': 4360310,
            'type': 'DROP',
            'fromTeamId': 2,
        },
        {
            'playerId': 4429084,
            'type': 'DROP',
            'fromTeamId': 2,
        },
    ],
    'isActingAsTeamOwner': False,
    'skipTransactionCounters': False,
}

response = requests.post('https://lm-api-writes.fantasy.espn.com/apis/v3/games/ffl/seasons/2023/segments/0/leagues/1908531039/transactions/', cookies=cookiesESPN, headers=headers, json=json_data)