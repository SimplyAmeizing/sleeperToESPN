import requests
import asyncio
from getElementsSleeper import *
from getElementsESPN import *

async def main():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # Monkeypatch requests.Session.request to always verify=False
    _old_request = requests.Session.request
    def _new_request(self, *args, **kwargs):
        kwargs['verify'] = False
        return _old_request(self, *args, **kwargs)
    requests.Session.request = _new_request

    sleeperLeagueId = "1255956974311321600"
    weekNumber = input("Enter week number: ")
    action = input("Enter populate or lineup or all: ")

    sleeperConvertedToEspnId = await convertSleeperRosterToEspnIds(sleeperLeagueId)
    slotMap = {}

    if (action == "populate" or action == "all"):
        playedArray = set()
        espnRostersForLeague = getRosterESPN()

        dropAllPlayersESPN(weekNumber, espnRostersForLeague)

        addAllPlayersESPN(weekNumber, sleeperConvertedToEspnId)

    if (action == "lineup" or action == "all"):
        playedArray = getPlayedArray(weekNumber)

        setLineupESPN(weekNumber, sleeperConvertedToEspnId, playedArray)





#add functionality to add in week number to the main parameter
if __name__ == '__main__':
    asyncio.run(main())