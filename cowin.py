import json
from datetime import datetime
from threading import Timer
from datetime import datetime
import pytz
import requests
import time

def epoch_seconds(str_dt, timezone):
    timezone = pytz.timezone(timezone)
    dt = datetime.strptime(str_dt, '%Y-%m-%d %H:%M:%S')
    dt_timezone = timezone.localize(dt)
    return int(dt_timezone.timestamp())*1000

def telegram_bot_sendtext(bot_message):

   bot_token = 'XXXXXXXXXXX'
   bot_chatID = 'XXXXXXXXX'
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(send_text)

   return response.json()


pincode = 'XXXXXXXX'
date = '02-05-2021'
scriptEndDate = '2021-05-03 00:00:00'
wekbook_url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByPin?pincode='+pincode+'&date='+ date




epocEnd = epoch_seconds(scriptEndDate, "Asia/Kolkata")

while round(time.time() * 1000) < epocEnd :
    try :
        avaibleCount = 0
        message = "Avaible in >"
        res = requests.get(wekbook_url)
        if res.status_code == 200:
            jsonBody = json.loads(res.text)
            totalCentre = len(jsonBody["centers"])
            for i in range(totalCentre):
                center = jsonBody["centers"][i]
                sessionsLength = len(center["sessions"])
                for j in range(sessionsLength):
                    capacity = center["sessions"][j]["available_capacity"]
                    ageLimit = center["sessions"][j]["min_age_limit"]
                    if (capacity > 0) and ageLimit == 18:
                        avaibleCount = avaibleCount + 1
                        message = message + str(center["name"]) + "|"

            print(avaibleCount)

            if avaibleCount > 0:
                test = telegram_bot_sendtext("Empty slot available slot " + str(avaibleCount) + " in " + message)
                print(test)
        else:
            print("code Not 200")
    except:
        print("Exception Occur")

    time.sleep(600)