import requests
import json
import time
# from flask import request

header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

while(1):
    welcome='https://api.telegram.org/bot5521409024:AAGtt1z3ZvG-xkHlzFNFQva4MSp0d4j0chU/sendMessage?chat_id=-622638037&&text=This_is_notifier_for_Punjab_Circuit every 15 minutes'
    requests.get(welcome)
    msg=[]
    for i in range(479,500):
        i=str(i)
        x='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id='+i+'&date=09-07-2022'
        data=requests.get(x,headers=header)
        results=json.loads(data.text)
        count=results["sessions"]
        if(len(count)>0):
            msg=[]
            for session in count:
                msg.append({"district_name":session["district_name"],"Centre_name":session["name"],"Centre_Address":session["address"],"Vaccine":session["vaccine"],"Fee":session["fee"],"Min_age_Limit":session["min_age_limit"],"Capacity_available":session["available_capacity"],"Minimum_Age_Limit":session["min_age_limit"],"Date":session["date"],"Slots":session["slots"]})
            parse_data=json.dumps(msg)
            parse_data=parse_data.replace("{","")
            parse_data=parse_data.replace("}","\n\n")
            parse_data=parse_data.replace("[","")
            parse_data=parse_data.replace("]","")
            parse_data=parse_data.replace(",","\n")
            print(parse_data)
            welcome2="https://api.telegram.org/bot5521409024:AAGtt1z3ZvG-xkHlzFNFQva4MSp0d4j0chU/sendMessage?chat_id=-622638037&&text=Notification for district ->"+session["district_name"]
            requests.get(welcome2)
            w_url='https://api.telegram.org/bot5521409024:AAGtt1z3ZvG-xkHlzFNFQva4MSp0d4j0chU/sendMessage?chat_id=-622638037&&text='+parse_data
            y=requests.get(w_url)
            print(y)
            time.sleep(6)
    time.sleep(900)  #Is pyth on time sleep in seconds?
# We can use python sleep function to halt the execution of the program for given time in seconds.
#  ok git also updated