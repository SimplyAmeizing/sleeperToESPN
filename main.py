from audioop import add
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import requests
import json
import asyncio
from getElementsSleeper import *
from getElementsESPN import *
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

async def main():
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

    weekNumber = input("What week number is it in the NFL right now: ")
    action = input("Enter populate or lineup: ")

    if (action == "populate"):

        finalStarters = []
        sleeperConvertedToEspnId = await queryLeagueDetail(weekNumber, finalStarters)

        # driver.close()
        # service = Service(executable_path="C:\Personal\SleeperToEspn\geckodriver.exe")

        # firefox_options = Options()
        # firefox_options.add_argument('--headless')

        # Initialize the Firefox driver with headless options
        # driver = webdriver.Firefox(service=service)

        # driver.get("https://www.espn.com/fantasy/football/")
        # time.sleep(30)

        litArray = getRosterESPN(weekNumber)

        dropAllPlayersESPN(weekNumber, litArray)

        addAllPlayersESPN(weekNumber, sleeperConvertedToEspnId, finalStarters)

        print(litArray)
    
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

        finalStarters = []
        sleeperConvertedToEspnId = await queryLeagueDetail(weekNumber, finalStarters)

        setLineup(weekNumber, finalStarters)
    

        


#add functionality to add in week number to the main parameter
if __name__ == '__main__':
    asyncio.run(main())