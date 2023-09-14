from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import requests
import json
import asyncio
from getElements import *
from getElementsESPN import *
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

sleeperPlayerIdArray = []


async def main():
    username = "simplyameizing"
    password = "Mc384179"

    # driver = webdriver.Chrome()

    # head to github login page
    # driver.get("https://sleeper.com/login")
    # # find username/email field and send the username itself to the input field

    # await SubmitUsername(driver, username)
    # time.sleep(2)

    # await SubmitPassword(driver, password)
    # time.sleep(30)

    # sleeperConvertedToEspnId = await queryLeagueDetail(sleeperPlayerIdArray, sys.argv[1])
    # time.sleep(2)
    service = Service(executable_path="D:\PersonalProjects\SleeperToEspnTransfer\geckodriver.exe")

    # firefox_options = Options()
    # firefox_options.add_argument('--headless')

    # Initialize the Firefox driver with headless options
    driver = webdriver.Firefox(service=service)

    driver.get("https://www.espn.com/fantasy/football/")
    time.sleep(30)

    litArray = getRosterESPN(sys.argv[1])
    driver.close()

#add functionality to add in week number to the main parameter
if __name__ == '__main__':
    asyncio.run(main())