
import requests

myKey = '5b3ce3597851110001cf62484ba713a9c9e54b70a25bb6453bf059ed'

body = {"locations":[[11.3908086,47.2675221]
                     ,[11.3930573,47.266932]
                     ,[11.4002235,47.2635087]
                     ,[11.3975994,47.2667978]
                     ,[11.3953351,47.2700619]
                     ,[11.3981243,47.2756296]
                     ,[11.4080819,47.2730177]
                     ,[11.4099909,47.2645752]
                     ,[11.4095803,47.2603696]
                     ,[11.4124073,47.2567091]
                     ,[11.4299444,47.2556179]
                     ,[11.4121679,47.2573154]
                     ,[11.3998987,47.2531879]
                     ,[11.4009585,47.2508032]
                     ,[11.3985525,47.254931]
                     ,[11.3949407,47.2619768]
                     ,[11.3935693,47.2651109]
                     ,[11.3870062,47.2678484]]
        ,"destinations":[0,1,2]
        ,"metrics":["distance"]
        ,"sources":[0,1,2]
        }

headers = {
    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    'Authorization': myKey,
    'Content-Type': 'application/json; charset=utf-8'
}
call = requests.post('https://api.openrouteservice.org/v2/matrix/cycling-road', json=body, headers=headers)

print(call.status_code, call.reason)
print(call.text)

import json

json1 = json.loads(call.text)
print("\n", json1["distances"])


