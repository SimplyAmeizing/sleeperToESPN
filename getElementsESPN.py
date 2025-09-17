import json
import requests
from cookies import *
import time
from espn_api.football import League
import urllib3

def getRosterESPN():
    # This disables SSL certificate warnings
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # Monkeypatch requests to always use verify=False
    _old_request = requests.Session.request


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

    # for k in range (1,11):
    #     cookies = cookiesESPN

    #     url = "https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/2025/segments/0/leagues/402922762?rosterForTeamId=" + str(k) + "&view=mDraftDetail&view=mLiveScoring&view=mMatchupScore&view=mPendingTransactions&view=mPositionalRatings&view=mRoster&view=mSettings&view=mTeam&view=modular&view=mNav"
    #     headers = {
    #         'authority': 'lm-api-reads.fantasy.espn.com',
    #         'accept': 'application/json',
    #         'accept-language': 'en-US,en;q=0.9',
    #         'if-none-match': 'W/"02219796b8d16530b962ce5b001476b4f',
    #         'origin': 'https://fantasy.espn.com',
    #         'referer': 'https://fantasy.espn.com/',
    #         'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    #         'sec-ch-ua-mobile': '?0',
    #         'sec-ch-ua-platform': '"Windows"',
    #         'sec-fetch-dest': 'empty',
    #         'sec-fetch-mode': 'cors',
    #         'sec-fetch-site': 'same-site',
    #         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    #         'x-fantasy-filter': '{"players":{}}',
    #         'x-fantasy-platform': 'kona-PROD-4bf5ad99065b78300041623712026402b4d5f9c1',
    #         'x-fantasy-source': 'kona',
    #     }

    #     cookie_string = """s_ecid=MCMID%7C29455170474594074870364868669099251486; tveAuth=espn3; _cc_id=d1edd3bb12d9907abfa462d9b4519d14; _gcl_au=1.1.707456343.1757356719; _cb=BAjLXvB_YBqswc6_x; _scor_uid=e55f3da0832241cb9f13a3d7a9b6858b; _ga=GA1.1.303108334.1757356775; _ga_2H3SPEKBHV=GS2.1.s1757356774$o1$g0$t1757356774$j60$l0$h0; _pubcid=5580de9b-fa13-4484-8373-e64b9bf08a42; _pubcid_cst=1izpLMgsJw%3D%3D; _au_1d=AU1D-0100-001754931286-NRRZGYNV-CMT0; check=true; userZip=75201; country=us; hashedIp=73e736b6ea7ff5ee9f40364ae1b7783737215ccd2957bcdbae56b9b91400d424; IR_gbd=espn.com; tveProviderName=; _v__chartbeat3=BvUE_YiiBbYBVwpnY; AMCVS_EE0201AC512D2BE80A490D4C%40AdobeOrg=1; nol_fpid=moam6k3b38fplyn1wlioc2rxuicjr1757356765|1757356765007|1757950722432|1757950722485; s_cc=true; cto_bidid=qyqNZF95ZFJreDcyJTJGTG16Skt4MjYzRVFTayUyQlM4ek54UjdPR3NqcVdCZHI5V2hkQ3A5TzYwc09KcHJUMkxEdjVhVnhIdXdhSzljS2xYb2FvNmdjak1MaDhab3lFYUkzJTJGS2Zuc29RTnUxaklVJTJGU0pzJTNE; mboxEdgeCluster=35; panoramaId_expiry=1758646432142; panoramaId=40744d091a301478312375399c1816d53938bd2a5ddd6c1c545e4444f93d7f86; panoramaIdType=panoIndiv; tveMVPDAuth=; block.check=false%7Cfalse; connectId={"ttl":86400000,"lastUsed":1758041633142,"lastSynced":1758041633142}; tvid=a4590e741d8d490997e2cc1703145fdf; AMCV_EE0201AC512D2BE80A490D4C%40AdobeOrg=-50417514%7CMCMID%7C29455170474594074870364868669099251486%7CMCAAMLH-1758646438%7C9%7CMCAAMB-1758646438%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1758048838s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.5.0; device_f1259fe1=2717b707-dde3-4507-a3b2-4f3ad83271c7; ESPN-ONESITE.WEB-PROD.api=QpT7Oceq0/ByqveOtHI5rw05DWxbsKTERtZ1aKhoLBLEC97HAADAWTmCwGlkH0HM3kOKbeV1Z+QS0CpzMCUEmv6isEID; ESPN-ONESITE.WEB-PROD.ts=2025-09-16T17:25:03.447Z; SWID={F53FF6DD-1278-4465-BF66-72F48AAA1569}; ESPN-ONESITE.WEB-PROD.token=5=eyJhY2Nlc3NfdG9rZW4iOiJleUpyYVdRaU9pSm5kV1Z6ZEdOdmJuUnliMnhzWlhJdExURTJNakF4T1RNMU5EUWlMQ0poYkdjaU9pSkZVekkxTmlKOS5leUpxZEdraU9pSldhbFV5TkVzMFpWQXpNalJvYzFGWVlrVnBYMmxCSWl3aWFYTnpJam9pYUhSMGNITTZMeTloZFhSb0xuSmxaMmx6ZEdWeVpHbHpibVY1TG1kdkxtTnZiU0lzSW1GMVpDSTZJblZ5Ympwa2FYTnVaWGs2YjI1bGFXUTZjSEp2WkNJc0ltbGhkQ0k2TVRjMU9EQTBNVFk1T0N3aWJtSm1Jam94TnpVNE1EUXhOams0TENKbGVIQWlPakUzTlRneE1qZ3dPVGdzSW1Oc2FXVnVkRjlwWkNJNklrVlRVRTR0VDA1RlUwbFVSUzVYUlVJdFVGSlBSQ0lzSW1OaGRDSTZJbWQxWlhOMElpd2liR2xrSWpvaU9UUXdOR1E1TVRNdFptUmhPQzAwWXpjeUxUazFaakV0TVRjNE1EaGhNRE0zWVdRMUlpd2lhV1JsYm5ScGRIbGZhV1FpT2lJNVlUVTFZV0pqWXkxak9UTXlMVFJrWVRrdFltUXpZaTB4WXpsak5EazBOVGt4TnpnaUxDSnpkV0lpT2lKN1JqVXpSa1kyUkVRdE1USTNPQzAwTkRZMUxVSkdOall0TnpKR05EaEJRVUV4TlRZNWZTSjkuX25mVG8tZGpZd0d0Q3NqZ2NJeXlmUS0tajJyV1B0MWlRUE9Sa2NVOFh0SElRVFdwYl9pWFFWeWVEbU96azljQ3ppNXlYRWVmcGM5bXNab3REZ3ZZSnciLCJyZWZyZXNoX3Rva2VuIjoiZXlKcmFXUWlPaUpuZFdWemRHTnZiblJ5YjJ4c1pYSXRMVEUyTWpBeE9UTTFORFFpTENKaGJHY2lPaUpGVXpJMU5pSjkuZXlKcWRHa2lPaUp5VkcxUFlXRlBkemhIZDNWQ05EUkNjbEZsU1cxM0lpd2ljM1ZpSWpvaWUwWTFNMFpHTmtSRUxURXlOemd0TkRRMk5TMUNSalkyTFRjeVJqUTRRVUZCTVRVMk9YMGlMQ0pwYzNNaU9pSm9kSFJ3Y3pvdkwyRjFkR2d1Y21WbmFYTjBaWEprYVhOdVpYa3VaMjh1WTI5dElpd2lZWFZrSWpvaWRYSnVPbVJwYzI1bGVUcHZibVZwWkRwd2NtOWtJaXdpYVdGMElqb3hOelU0TURReE5qazRMQ0p1WW1ZaU9qRTNOVGd3TkRFMk9UZ3NJbVY0Y0NJNk1UYzNNelU1TXpZNU9Dd2lZMnhwWlc1MFgybGtJam9pUlZOUVRpMVBUa1ZUU1ZSRkxsZEZRaTFRVWs5RUlpd2lZMkYwSWpvaWNtVm1jbVZ6YUNJc0lteHBaQ0k2SWprME1EUmtPVEV6TFdaa1lUZ3ROR00zTWkwNU5XWXhMVEUzT0RBNFlUQXpOMkZrTlNJc0ltbGtaVzUwYVhSNVgybGtJam9pT1dFMU5XRmlZMk10WXprek1pMDBaR0U1TFdKa00ySXRNV001WXpRNU5EVTVNVGM0SW4wLmxQMDhpTGdYWG1rcHlnd3NPbmIxdWszYTEyYzMwNVlUTHZnRVN4TktiS1NwY1FLV3JUM2M4TVJJclJkUmI0Wmdybml2R2hjV0ltMV9IUlN3ZFhUZ3V3Iiwic3dpZCI6IntGNTNGRjZERC0xMjc4LTQ0NjUtQkY2Ni03MkY0OEFBQTE1Njl9IiwidHRsIjo4NjM5OSwicmVmcmVzaF90dGwiOjE1NTUxOTk5LCJoaWdoX3RydXN0X2V4cGlyZXNfaW4iOjE3OTksImluaXRpYWxfZ3JhbnRfaW5fY2hhaW5fdGltZSI6MTc1ODA0MTY5ODAwMCwiaWF0IjoxNzU4MDQxNjk4MDAwLCJleHAiOjE3NTgxMjgwOTgwMDAsInJlZnJlc2hfZXhwIjoxNzczNTkzNjk4MDAwLCJoaWdoX3RydXN0X2V4cCI6MTc1ODA0MzQ5ODAwMCwic3NvIjpudWxsLCJhdXRoZW50aWNhdG9yIjpudWxsLCJsb2dpblZhbHVlIjpudWxsLCJjbGlja2JhY2tUeXBlIjpudWxsLCJzZXNzaW9uVHJhbnNmZXJLZXkiOiJsSG8wOGlHdXJwZUoyMUN4V2NNOGdZdmxpZFhweklPcUZ3bE1EYmN3a2M5cnZKZWswdUlYWHFkZUxQeVZhNzJmSUxlQ0lLUE5sLXVrWWhlLVVpVW9iMFNQamNDOTFtTzV5eXYyMUlXVGJQa2I2T3NBbks4IiwiY3JlYXRlZCI6IjIwMjUtMDktMTZUMTY6NTU6MDQuNDQ3WiIsImxhc3RDaGVja2VkIjoiMjAyNS0wOS0xNlQxNjo1NTowNC40NDdaIiwiZXhwaXJlcyI6IjIwMjUtMDktMTdUMTY6NTQ6NTguMDAwWiIsInJlZnJlc2hfZXhwaXJlcyI6IjIwMjYtMDMtMTVUMTY6NTQ6NTguMDAwWiJ9|eyJraWQiOiJndWVzdGNvbnRyb2xsZXItLTE2MjAxOTM1NDQiLCJhbGciOiJFUzI1NiJ9.eyJqdGkiOiJOTlpYUDV1Ym5wakNYQUNnVjdYcThBIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLnJlZ2lzdGVyZGlzbmV5LmdvLmNvbSIsImF1ZCI6IkVTUE4tT05FU0lURS5XRUItUFJPRCIsInN1YiI6IntGNTNGRjZERC0xMjc4LTQ0NjUtQkY2Ni03MkY0OEFBQTE1Njl9IiwiaWF0IjoxNzU4MDQxNjk4LCJuYmYiOjE3NTgwNDE2OTgsImV4cCI6MTc1ODEyODA5OCwiY2F0IjoiaWR0b2tlbiIsImVtYWlsIjoiY2hyaXNtZWl0eEBnbWFpbC5jb20iLCJpZGVudGl0eV9pZCI6IjlhNTVhYmNjLWM5MzItNGRhOS1iZDNiLTFjOWM0OTQ1OTE3OCJ9.QOp4l84tI5ZgZl4gwUqAP6Qo8Zdil6MQ0sDfSQUMgE7wY3oMFtsusWuDzTvI-vsFCvDetl3eHp269b5nHy53WA; ESPN-ONESITE.WEB-PROD-ac=XUS; espnAuth={"swid":"{F53FF6DD-1278-4465-BF66-72F48AAA1569}"}; dtcAuth=; timeOffset=-5; ab.storage.deviceId.96ad02b7-2edc-4238-8442-bc35ba85853c=g%3A8e9c143c-7c8f-f02c-c9ae-8077c1dbdae9%7Ce%3Aundefined%7Cc%3A1757950722959%7Cl%3A1758041711193; ab.storage.userId.96ad02b7-2edc-4238-8442-bc35ba85853c=g%3A%257BF53FF6DD-1278-4465-BF66-72F48AAA1569%257D%7Ce%3Aundefined%7Cc%3A1758041711191%7Cl%3A1758041711193; cto_bundle=4lLh0191dW9Eak9WcTRwMTV6YmlLQnlNSXpnajg1MmZoSVJMRlglMkZ4anVWR3dIZkh0NnZTR3E1UVp5bTZ5UGpiSEM3ZFhIczlLVlNkZG5JTDhMb3BiZWNKM2liQUpVRWslMkY0cEZSSHRMJTJGV3lDZWdPTmI3eXJLRXlKMlBFWm1XYWNKempQVGp2SVJOZFpYeUVmM1BQR1dJcWN4b2clM0QlM0Q; mbox=PC#b5c6864cfac6460ab650a2a6a0e0e57d.35_0#1821287194|session#ec81d015fa89461dbb0a6f4ace06cd5a#1758044254; __gads=ID=08ac8a2cf63d77bc:T=1757356715:RT=1758042394:S=ALNI_Ma5-QcI_C7Z-G-hZMX1IGP_VkHhLQ; __gpi=UID=000011154813b385:T=1757356715:RT=1758042394:S=ALNI_Ma3ZUbXxB3w-s8iTnJANhlIC-XajQ; __eoi=ID=8958ca77938706c4:T=1757356715:RT=1758042394:S=AA-Afjbp54fHhJ7XrDZ_DgeSuytB; ab.storage.sessionId.96ad02b7-2edc-4238-8442-bc35ba85853c=g%3Ae56b818f-9dfe-f10d-fb0b-6707019d6cce%7Ce%3A1758044197271%7Cc%3A1758041711192%7Cl%3A1758042397271; s_sq=%5B%5BB%5D%5D; s_ensNR=1758042403259-New; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Sep+16+2025+12%3A06%3A43+GMT-0500+(Central+Daylight+Time)&version=202407.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=2b562777-258b-4b43-b13f-3a9ff070e468&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CBG407%3A1%2CC0002%3A1%2CC0004%3A1%2CC0005%3A1&AwaitingReconsent=false; espn-prev-page=fantasy%3Afootball%3Aleague%3Amy%20team; IR_9070=1758042403797%7C0%7C1758042403797%7C%7C; _chartbeat2=.1754931281225.1758042403810.0000000100000011.2sOmPB7BO4egyqlNDG22TR8wbVL.1; _cb_svref=https%3A%2F%2Fwww.espn.com%2F; espn_s2=AEAwKONpzm3WB%2BCwaPHVAIwRnwlLIdxuZ07xb95dVKRYKq6%2BTAOfUeKaQyzy5%2Fi0NJq802%2FJ2JChr4RrPW%2BggBnFpnO03SFPS4s1DBaOSLQRr9kyKBL%2Bgsf3XqwZtT%2B487VD52CrLhztircymB6tLQxIto87IRpVC1%2FjMbyEsTmKLZjltQR1G3gGLukSnWteLA83rzQOaSu%2FmRl1TAMOpXj6vFhn0KBNhjhy6plbAH4m%2B4Xbo6rErCk7%2FGALCqiENrFJz6FALod4GyvDMVPVuEAG08IsjPh1h%2BBY8srATFwyKw%3D%3D; ESPN-ONESITE.WEB-PROD.idn=0099b3ecc1; _chartbeat4=t=Dk7SR7Cdeue7DA5MwPC38mwHBzzRhZ&E=10&x=0&c=8.06&y=1922&w=896"""

    #     # # Split and create dict:
    #     # cookiesES = {kv.split('=', 1)[0].strip(): kv.split('=', 1)[1] for kv in cookie_string.split('; ') if '=' in kv}
    #     response = requests.get(url, headers=headers, cookies=cookiesES, verify=False)

    #     finalArray = [None] * 10
    #     if response.status_code == 200:
    #         json_data = response.json()
    #         schedule = json_data.get('schedule')
            
    #         if schedule:
    #             indexer = (int(weekNumber) * 5) - 5

    #             for i in range(indexer, int(weekNumber)*5):
    #                 away_roster = schedule[i].get('away', {}).get('rosterForCurrentScoringPeriod', {}).get('entries')
    #                 team_id_away = schedule[i].get('away').get('teamId')

    #                 tempArray_away = []
    #                 for j in away_roster:
    #                     tempArray_away.append(j['playerId'])
                    
    #                 finalArray[team_id_away-1] = tempArray_away

                    
    #                 home_roster = schedule[i].get('home', {}).get('rosterForCurrentScoringPeriod', {}).get('entries')
    #                 team_id_home = schedule[i].get('home').get('teamId')

    #                 tempArray_home = []
    #                 for j in home_roster:
    #                     tempArray_home.append(j['playerId'])
                    
    #                 finalArray[team_id_home-1] = tempArray_home
                    
    #         else:
    #             print("No schedule data in the JSON response.")
    #     else:
    #         print(response)
    #         print("Request failed with status code:", response.status_code)

    # print(finalArray)
    # return finalArray


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

        if i == 5:
            time.sleep(120)
        elif i == 8:
            time.sleep(120)

        max_retries = 5
        retry_wait_time = 300  # 15 minutes in seconds


        for j in sleeperRoster['Chris']:
            print(j)
            for k in j:
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
                dictTemp['playerId'] = k
                dictTemp['type'] = "ADD"
                dictTemp['toTeamId'] = i
                json_data['items'].append(dictTemp)
                for attempt in range(max_retries):
                    response = requests.post('https://lm-api-writes.fantasy.espn.com/apis/v3/games/ffl/seasons/2025/segments/0/leagues/402922762/transactions/', cookies=cookiesESPN, headers=headers, json=json_data)
                    if response.status_code == 409:
                        print(f"409 Conflict! Cooling down for 5 minutes...")
                        time.sleep(retry_wait_time)
                    else:
                        print(response.status_code, response.text)
                        break
        # for j in addLaterArray:
        #     json_data = {
        #         'isLeagueManager': True,
        #         'teamId': i,
        #         'type': 'FREEAGENT',
        #         'scoringPeriodId': weekNumber,
        #         'executionType': 'EXECUTE',
        #         'items': [],
        #         'isActingAsTeamOwner': False,
        #         'skipTransactionCounters': False,
        #     }

        #     dictTemp = {}
        #     dictTemp['playerId'] = j
        #     dictTemp['type'] = "ADD"
        #     dictTemp['toTeamId'] = i
        #     json_data['items'].append(dictTemp)

        #     response = requests.post('https://lm-api-writes.fantasy.espn.com/apis/v3/games/ffl/seasons/2025/segments/0/leagues/402922762/transactions/', cookies=cookiesESPN, headers=headers, json=json_data, verify=False)


def setLineup(weeknumber, finalStarters):
    for i in range(1, 11):

        rosterESPN = getRosterESPN(weeknumber)
        rbCount = 0
        wrCount = 0
        teCount = 0
        for j in rosterESPN[i-1]:
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
                'x-fantasy-platform': 'kona-PROD-6ee6d5a5bb4b5179168f499396f975244a11e9e5',
                'x-fantasy-source': 'kona',
            }
            
            with open('espnPlayers.json') as f:
                jsonData = json.load(f)

                defaultPositionId = None
                for item in jsonData:
                    if (item['id'] == j):
                        defaultPositionId = item["defaultPositionId"]

            if(defaultPositionId == 1):
                json_data = {
                    'isLeagueManager': True,
                    'teamId': i,
                    'type': 'ROSTER',
                    'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                    'scoringPeriodId': weeknumber,
                    'executionType': 'EXECUTE',
                    'items': [
                        {
                            'playerId': j,
                            'type': 'LINEUP',
                            'fromLineupSlotId': 0,
                            'toLineupSlotId': 20,
                        },
                    ],
                }

                response = requests.post('https://lm-api-writes.fantasy.espn.com/apis/v3/games/ffl/seasons/2023/segments/0/leagues/1908531039/transactions/', cookies=cookiesESPN, headers=headers, json=json_data)


            elif(defaultPositionId == 2):
                json_data = {
                    'isLeagueManager': True,
                    'teamId': i,
                    'type': 'ROSTER',
                    'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                    'scoringPeriodId': weeknumber,
                    'executionType': 'EXECUTE',
                    'items': [
                        {
                            'playerId': j,
                            'type': 'LINEUP',
                            'fromLineupSlotId': 2,
                            'toLineupSlotId': 20,
                        },
                    ],
                }

                # if (rbCount == 2):
                #     json_data['items']['fromLineupSlotId'] = 23

                response = requests.post('https://lm-api-writes.fantasy.espn.com/apis/v3/games/ffl/seasons/2023/segments/0/leagues/1908531039/transactions/', cookies=cookiesESPN, headers=headers, json=json_data)
                # if(response.status_code == "200"):
                #     rbCount += 1

            elif(defaultPositionId == 3):
                json_data = {
                    'isLeagueManager': True,
                    'teamId': i,
                    'type': 'ROSTER',
                    'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                    'scoringPeriodId': weeknumber,
                    'executionType': 'EXECUTE',
                    'items': [
                        {
                            'playerId': j,
                            'type': 'LINEUP',
                            'fromLineupSlotId': 4,
                            'toLineupSlotId': 20,
                        },
                    ],
                }

                # if (wrCount == 2):
                #     json_data['items'][0]['fromLineupSlotId'] = 23

                response = requests.post('https://lm-api-writes.fantasy.espn.com/apis/v3/games/ffl/seasons/2023/segments/0/leagues/1908531039/transactions/', cookies=cookiesESPN, headers=headers, json=json_data)
                # if(response.status_code == "200"):
                #     wrCount += 1

            elif(defaultPositionId == 4):
                json_data = {
                    'isLeagueManager': True,
                    'teamId': i,
                    'type': 'ROSTER',
                    'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                    'scoringPeriodId': weeknumber,
                    'executionType': 'EXECUTE',
                    'items': [
                        {
                            'playerId': j,
                            'type': 'LINEUP',
                            'fromLineupSlotId': 6,
                            'toLineupSlotId': 20,
                        },
                    ],
                }

                # if (teCount == 2):
            #         json_data['items'][0]['fromLineupSlotId'] = 23

                response = requests.post('https://lm-api-writes.fantasy.espn.com/apis/v3/games/ffl/seasons/2023/segments/0/leagues/1908531039/transactions/', cookies=cookiesESPN, headers=headers, json=json_data)
                # if(response.status_code == "200"):
                #     teCount += 1

            elif(defaultPositionId == 5):
                json_data = {
                    'isLeagueManager': True,
                    'teamId': i,
                    'type': 'ROSTER',
                    'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                    'scoringPeriodId': weeknumber,
                    'executionType': 'EXECUTE',
                    'items': [
                        {
                            'playerId': j,
                            'type': 'LINEUP',
                            'fromLineupSlotId': 17,
                            'toLineupSlotId': 20
                        },
                    ],
                }

                response = requests.post('https://lm-api-writes.fantasy.espn.com/apis/v3/games/ffl/seasons/2023/segments/0/leagues/1908531039/transactions/', cookies=cookiesESPN, headers=headers, json=json_data)

            elif(defaultPositionId == 16):
                json_data = {
                    'isLeagueManager': True,
                    'teamId': i,
                    'type': 'ROSTER',
                    'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                    'scoringPeriodId': weeknumber,
                    'executionType': 'EXECUTE',
                    'items': [
                        {
                            'playerId': j,
                            'type': 'LINEUP',
                            'fromLineupSlotId': 16,
                            'toLineupSlotId': 20
                        },
                    ],
                }

                response = requests.post('https://lm-api-writes.fantasy.espn.com/apis/v3/games/ffl/seasons/2023/segments/0/leagues/1908531039/transactions/', cookies=cookiesESPN, headers=headers, json=json_data)
        
        for j in finalStarters[i-1]:


            with open('espnPlayers.json') as f:
                jsonData = json.load(f)

                defaultPositionId = None
                for item in jsonData:
                    if (item['id'] == j):
                        defaultPositionId = item["defaultPositionId"]

            if(defaultPositionId == 1):
                json_data = {
                    'isLeagueManager': True,
                    'teamId': i,
                    'type': 'ROSTER',
                    'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                    'scoringPeriodId': weeknumber,
                    'executionType': 'EXECUTE',
                    'items': [
                        {
                            'playerId': j,
                            'type': 'LINEUP',
                            'fromLineupSlotId': 20,
                            'toLineupSlotId': 0,
                        },
                    ],
                }

                response = requests.post('https://lm-api-writes.fantasy.espn.com/apis/v3/games/ffl/seasons/2023/segments/0/leagues/1908531039/transactions/', cookies=cookiesESPN, headers=headers, json=json_data)


            elif(defaultPositionId == 2):
                json_data = {
                    'isLeagueManager': True,
                    'teamId': i,
                    'type': 'ROSTER',
                    'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                    'scoringPeriodId': weeknumber,
                    'executionType': 'EXECUTE',
                    'items': [
                        {
                            'playerId': j,
                            'type': 'LINEUP',
                            'fromLineupSlotId': 20,
                            'toLineupSlotId': 2,
                        },
                    ],
                }

                if (rbCount == 2):
                    json_data['items'][0]['toLineupSlotId'] = 23

                response = requests.post('https://lm-api-writes.fantasy.espn.com/apis/v3/games/ffl/seasons/2023/segments/0/leagues/1908531039/transactions/', cookies=cookiesESPN, headers=headers, json=json_data)
                rbCount += 1

            elif(defaultPositionId == 3):
                json_data = {
                    'isLeagueManager': True,
                    'teamId': i,
                    'type': 'ROSTER',
                    'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                    'scoringPeriodId': weeknumber,
                    'executionType': 'EXECUTE',
                    'items': [
                        {
                            'playerId': j,
                            'type': 'LINEUP',
                            'fromLineupSlotId': 20,
                            'toLineupSlotId': 4,
                        },
                    ],
                }

                if (wrCount == 2):
                    json_data['items'][0]['toLineupSlotId'] = 23

                response = requests.post('https://lm-api-writes.fantasy.espn.com/apis/v3/games/ffl/seasons/2023/segments/0/leagues/1908531039/transactions/', cookies=cookiesESPN, headers=headers, json=json_data)
                wrCount += 1

            elif(defaultPositionId == 4):
                json_data = {
                    'isLeagueManager': True,
                    'teamId': i,
                    'type': 'ROSTER',
                    'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                    'scoringPeriodId': weeknumber,
                    'executionType': 'EXECUTE',
                    'items': [
                        {
                            'playerId': j,
                            'type': 'LINEUP',
                            'fromLineupSlotId': 20,
                            'toLineupSlotId': 6,
                        },
                    ],
                }

                if (teCount == 2):
                    json_data['items'][0]['toLineupSlotId'] = 23

                response = requests.post('https://lm-api-writes.fantasy.espn.com/apis/v3/games/ffl/seasons/2023/segments/0/leagues/1908531039/transactions/', cookies=cookiesESPN, headers=headers, json=json_data)
                teCount += 1

            elif(defaultPositionId == 5):
                json_data = {
                    'isLeagueManager': True,
                    'teamId': i,
                    'type': 'ROSTER',
                    'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                    'scoringPeriodId': weeknumber,
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

                response = requests.post('https://lm-api-writes.fantasy.espn.com/apis/v3/games/ffl/seasons/2023/segments/0/leagues/1908531039/transactions/', cookies=cookiesESPN, headers=headers, json=json_data)

            elif(defaultPositionId == 16):
                json_data = {
                    'isLeagueManager': True,
                    'teamId': i,
                    'type': 'ROSTER',
                    'memberId': '{F53FF6DD-1278-4465-BF66-72F48AAA1569}',
                    'scoringPeriodId': weeknumber,
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

                response = requests.post('https://lm-api-writes.fantasy.espn.com/apis/v3/games/ffl/seasons/2023/segments/0/leagues/1908531039/transactions/', cookies=cookiesESPN, headers=headers, json=json_data)

