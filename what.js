curl 'https://sleeper.com/graphql' \
  -H 'Accept: application/json' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdmF0YXIiOiJmMGVkYmY0Mjc4ZjUzZjk0MjVkYjE3NTA3M2RmNjU4NCIsImRpc3BsYXlfbmFtZSI6IlNpbXBseUFtZWl6aW5nIiwiZXhwIjoxNzIzOTMzMDk0LCJpYXQiOjE2OTIzOTcwOTQsImlzX2JvdCI6ZmFsc2UsImlzX21hc3RlciI6ZmFsc2UsInJlYWxfbmFtZSI6bnVsbCwidXNlcl9pZCI6NzY4MjU5NTQ1MDg4MDE2Mzg0LCJ2YWxpZF8yZmEiOiJwaG9uZSJ9.i0iRlGoCiba1e8tSaWHXzaDBMpU3M9JgK6PIB7IH0eA' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: _gcl_au=1.1.582135886.1692397025; _scid=ccf2202c-8e2b-40f4-a9d4-945e07f10de3; _fbp=fb.1.1692397040658.1227532608; _scid_r=ccf2202c-8e2b-40f4-a9d4-945e07f10de3; _sctr=1%7C1692331200000; intercom-id-xstxtwfr=44f319c9-df04-4230-91fb-0f451c260a89; intercom-device-id-xstxtwfr=47035b21-92f7-47f8-9e05-bd5515364540; _gid=GA1.2.1306068091.1694712782; intercom-session-xstxtwfr=b1pENXNrNHI2TDdDSWRDYzdLRGl5bDRYbjdURDZycUhvdHBlSyttbExVTU05cmI4SHJMbmQxanE1aUVRc0I2Ky0tKzNiOWcvRjdBOTZVQlo1c3VZVXlXQT09--ab752977fe3da67b08aed7e7e541415e6ee31504; _ga_QEMDVZ8GRQ=GS1.1.1694712781.10.1.1694712988.60.0.0; _gat=1; _ga_1LF1E2KJ1W=GS1.1.1694712782.10.1.1694712988.60.0.0; _ga=GA1.1.1965859663.1692397026; _ga_D47X7ML72N=GS1.2.1694712782.12.1.1694712989.59.0.0' \
  -H 'Origin: https://sleeper.com' \
  -H 'Referer: https://sleeper.com/leagues/992182224076255232/team' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --data-raw '{"operationName":"get_league_detail","variables":{},"query":"query get_league_detail {\n        \n    league_rosters(league_id: \"992182224076255232\"){\n      league_id\n      metadata\n      owner_id\n      co_owners\n      players\n      roster_id\n      settings\n      starters\n      keepers\n      reserve\n      taxi\n      player_map\n    }\n  \n        \n      league_users(league_id: \"992182224076255232\"){\n        avatar\n        user_id\n        league_id\n        metadata\n        settings\n        display_name\n        is_owner\n        is_bot\n      }\n  \n        \n      league_transactions_filtered(league_id: \"992182224076255232\",roster_id_filters: [],type_filters: [],leg_filters: [],status_filters: [\"pending\",\"proposed\"]){\n        adds\n        consenter_ids\n        created\n        creator\n        draft_picks\n        drops\n        league_id\n        leg\n        metadata\n        roster_ids\n        settings\n        status\n        status_updated\n        transaction_id\n        type\n        player_map\n        waiver_budget\n      }\n  \n        \n      matchup_legs_2:matchup_legs(league_id: \"992182224076255232\",round: 2){\n        league_id\n        leg\n        matchup_id\n        roster_id\n        round\n        starters\n        players\n        player_map\n        points\n        proj_points\n        max_points\n        custom_points\n        starters_games\n        picks\n        bans\n      }\n    \n        \n      }"}' \
  --compressed

fetch("https://sleeper.com/graphql", {
  "headers": {
    "accept": "application/json",
    "accept-language": "en-US,en;q=0.9",
    "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdmF0YXIiOiJmMGVkYmY0Mjc4ZjUzZjk0MjVkYjE3NTA3M2RmNjU4NCIsImRpc3BsYXlfbmFtZSI6IlNpbXBseUFtZWl6aW5nIiwiZXhwIjoxNzIzOTMzMDk0LCJpYXQiOjE2OTIzOTcwOTQsImlzX2JvdCI6ZmFsc2UsImlzX21hc3RlciI6ZmFsc2UsInJlYWxfbmFtZSI6bnVsbCwidXNlcl9pZCI6NzY4MjU5NTQ1MDg4MDE2Mzg0LCJ2YWxpZF8yZmEiOiJwaG9uZSJ9.i0iRlGoCiba1e8tSaWHXzaDBMpU3M9JgK6PIB7IH0eA",
    "content-type": "application/json",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin"
  },
  "referrer": "https://sleeper.com/leagues/992182224076255232/team",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": "{\"operationName\":\"get_league_detail\",\"variables\":{},\"query\":\"query get_league_detail {\\n        \\n    league_rosters(league_id: \\\"992182224076255232\\\"){\\n      league_id\\n      metadata\\n      owner_id\\n      co_owners\\n      players\\n      roster_id\\n      settings\\n      starters\\n      keepers\\n      reserve\\n      taxi\\n      player_map\\n    }\\n  \\n        \\n      league_users(league_id: \\\"992182224076255232\\\"){\\n        avatar\\n        user_id\\n        league_id\\n        metadata\\n        settings\\n        display_name\\n        is_owner\\n        is_bot\\n      }\\n  \\n        \\n      league_transactions_filtered(league_id: \\\"992182224076255232\\\",roster_id_filters: [],type_filters: [],leg_filters: [],status_filters: [\\\"pending\\\",\\\"proposed\\\"]){\\n        adds\\n        consenter_ids\\n        created\\n        creator\\n        draft_picks\\n        drops\\n        league_id\\n        leg\\n        metadata\\n        roster_ids\\n        settings\\n        status\\n        status_updated\\n        transaction_id\\n        type\\n        player_map\\n        waiver_budget\\n      }\\n  \\n        \\n      matchup_legs_2:matchup_legs(league_id: \\\"992182224076255232\\\",round: 2){\\n        league_id\\n        leg\\n        matchup_id\\n        roster_id\\n        round\\n        starters\\n        players\\n        player_map\\n        points\\n        proj_points\\n        max_points\\n        custom_points\\n        starters_games\\n        picks\\n        bans\\n      }\\n    \\n        \\n      }\"}",
  "method": "POST",
  "mode": "cors",
  "credentials": "include"
});