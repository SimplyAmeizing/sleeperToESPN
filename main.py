import time
import requests
import json
import asyncio
from getElementsSleeper import *
from getElementsESPN import *
import sys
from selenium.webdriver.chrome.service import Service

async def main():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # Monkeypatch requests.Session.request to always verify=False
    _old_request = requests.Session.request
    def _new_request(self, *args, **kwargs):
        kwargs['verify'] = False
        return _old_request(self, *args, **kwargs)
    requests.Session.request = _new_request
    
    username = "simplyameizing"
    password = "Mc384179"

    # driver = webdriver.Chrome()

    # # head to github login page
    # driver.get("https://sleeper.com/login")
    # # find username/email field and send the username itself to the input field

    # await SubmitUsername(driver, username)
    # time.sleep(2)

    # await SubmitPassword(driver, password)
    # time.sleep(30)

    sleeperLeagueId = "1255956974311321600"
    espnLeagueId = "402922762"
    weekNumber = input("Enter week number: ")
    action = input("Enter populate or lineup: ")

    if (action == "populate"):

        finalStarters = []

        sleeperConvertedToEspnId = await convertSleeperRosterToEspnIds(sleeperLeagueId)

        # driver.close()
        # service = Service(executable_path="C:\Personal\SleeperToEspn\geckodriver.exe")

        # firefox_options = Options()
        # firefox_options.add_argument('--headless')

        # Initialize the Firefox driver with headless options
        # driver = webdriver.Firefox(service=service)

        # driver.get("https://www.espn.com/fantasy/football/")
        # time.sleep(30)

        espnRostersForLeague = getRosterESPN()

        dropAllPlayersESPN(weekNumber, espnRostersForLeague)

        addAllPlayersESPN(weekNumber, sleeperConvertedToEspnId, sleeperConvertedToEspnId)

        # print(litArray)
    
    elif (action == "lineup"):
        service = Service(executable_path="D:\PersonalProjects\SleeperToEspn\geckodriver.exe")

        # firefox_options = Options()
        # firefox_options.add_argument('--headless')

        # # Initialize the Firefox driver with headless options
        # driver = webdriver.Firefox(service=service)

        # # head to github login page
        # driver.get("https://sleeper.com/login")
        # # find username/email field and send the username itself to the input field

        # await SubmitUsername(driver, username)
        # time.sleep(2)

        # await SubmitPassword(driver, password)
        # time.sleep(30)

        # finalStarters = []
        # sleeperConvertedToEspnId = await queryLeagueDetail(weekNumber, finalStarters)

        # setLineup(weekNumber, finalStarters)
    

        


#add functionality to add in week number to the main parameter
if __name__ == '__main__':
    asyncio.run(main())