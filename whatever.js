//adding players one by one
fetch("https://lm-api-writes.fantasy.espn.com/apis/v3/games/ffl/seasons/2023/segments/0/leagues/1908531039/transactions/", {
  "headers": {
    "accept": "application/json",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "sec-ch-ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "x-fantasy-platform": "kona-PROD-52ef5dee942a41adf22628f67f5e63b1f734fdd1",
    "x-fantasy-source": "kona"
  },
  "referrer": "https://fantasy.espn.com/",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": "{\"isLeagueManager\":true,\"teamId\":3,\"type\":\"FREEAGENT\",\"scoringPeriodId\":1,\"executionType\":\"EXECUTE\",\"items\":[{\"playerId\":3930066,\"type\":\"ADD\",\"toTeamId\":3}],\"isActingAsTeamOwner\":false,\"skipTransactionCounters\":false}",
  "method": "POST",
  "mode": "cors",
  "credentials": "include"
}).then(function (a) {
  return a.json(); // call the json method on the response to get JSON
})
.then(function (json) {
  console.log(json);
  // console.log(json['schedule'][0]['away']['rosterForCurrentScoringPeriod']['entries'])
});;



//getting current rosters (does it by schedule so be sure to do make sure matchup weeks are linked up)
fetch("https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/2023/segments/0/leagues/1908531039?rosterForTeamId=4&view=mDraftDetail&view=mLiveScoring&view=mMatchupScore&view=mPendingTransactions&view=mPositionalRatings&view=mRoster&view=mSettings&view=mTeam&view=modular&view=mNav", {
  "headers": {
    "accept": "application/json",
    "accept-language": "en-US,en;q=0.9",
    "sec-ch-ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "x-fantasy-filter": "{\"players\":{}}",
    "x-fantasy-platform": "kona-PROD-52ef5dee942a41adf22628f67f5e63b1f734fdd1",
    "x-fantasy-source": "kona"
  },
  "referrer": "https://fantasy.espn.com/",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": null,
  "method": "GET",
  "mode": "cors",
  "credentials": "include"
}).then(function (a) {
        return a.json(); // call the json method on the response to get JSON
    })
    .then(function (json) {
        console.log(json);
        // console.log(json['schedule'][0]['away']['rosterForCurrentScoringPeriod']['entries'])
    });


//how to drop players (this is in one by one format; the functionality supports dropping multiple players in one query) NOTE: scoring period id is p important as well
fetch("https://lm-api-writes.fantasy.espn.com/apis/v3/games/ffl/seasons/2023/segments/0/leagues/1908531039/transactions/", {
    "headers": {
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "sec-ch-ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "x-fantasy-platform": "kona-PROD-52ef5dee942a41adf22628f67f5e63b1f734fdd1",
        "x-fantasy-source": "kona"
    },
    "referrer": "https://fantasy.espn.com/",
    "referrerPolicy": "strict-origin-when-cross-origin",
    "body": "{\"isLeagueManager\":true,\"teamId\":1,\"type\":\"ROSTER\",\"memberId\":\"{F53FF6DD-1278-4465-BF66-72F48AAA1569}\",\"scoringPeriodId\":1,\"executionType\":\"EXECUTE\",\"items\":[{\"playerId\":4367209,\"type\":\"DROP\",\"fromTeamId\":1}],\"isActingAsTeamOwner\":false,\"skipTransactionCounters\":false}",
    "method": "POST",
    "mode": "cors",
    "credentials": "include"
    }).then(function (a) {
      return a.json(); // call the json method on the response to get JSON
  })
  .then(function (json) {
      console.log(json);
      // console.log(json['schedule'][0]['away']['rosterForCurrentScoringPeriod']['entries'])
  });;

//antoher example of drop but on kingsleys team
fetch("https://lm-api-writes.fantasy.espn.com/apis/v3/games/ffl/seasons/2023/segments/0/leagues/1908531039/transactions/", {
    "headers": {
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "sec-ch-ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "x-fantasy-platform": "kona-PROD-52ef5dee942a41adf22628f67f5e63b1f734fdd1",
        "x-fantasy-source": "kona"
    },
    "referrer": "https://fantasy.espn.com/",
    "referrerPolicy": "strict-origin-when-cross-origin",
    "body": "{\"isLeagueManager\":true,\"teamId\":3,\"type\":\"ROSTER\",\"memberId\":\"{F53FF6DD-1278-4465-BF66-72F48AAA1569}\",\"scoringPeriodId\":1,\"executionType\":\"EXECUTE\",\"items\":[{\"playerId\":4426385,\"type\":\"DROP\",\"fromTeamId\":3}],\"isActingAsTeamOwner\":false,\"skipTransactionCounters\":false}",
    "method": "POST",
    "mode": "cors",
    "credentials": "include"
    }).then(function (a) {
      return a.json(); // call the json method on the response to get JSON
  })
  .then(function (json) {
      console.log(json);
      // console.log(json['schedule'][0]['away']['rosterForCurrentScoringPeriod']['entries'])
  });;