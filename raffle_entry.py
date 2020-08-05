import requests
from tokenizer import CaptchaToken
from taskinator import Dataframe
import json
from colorama import init
from colorama import Fore, Back, Style
from datetime import datetime

init(autoreset=True)


POST_URL = 'https://rq06iiykwb.execute-api.eu-west-1.amazonaws.com/entries/prod'
token= CaptchaToken()

task = Dataframe('task.csv')
task = task.createTaskObj()
#rint(task)


payload = {}
headers = {
    'Accept': 'text/plain, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'Content-Type': 'application/json',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty'
}

def updatePayload(i, token):
    payload["firstName"] = task["task_" + str(i)]["firstName"]
    payload["rafflesID"] = str(task["task_" + str(i)]["rafflesID"])
    payload["lastName"] = task["task_" + str(i)]["lastName"]
    payload["email"] = task["task_" + str(i)]["email"]
    payload["paypalEmail"] = task["task_" + str(i)]["paypalEmail"]
    payload["mobile"] = str(task["task_" + str(i)]["mobile"])
    payload["dateofBirth"] = task["task_" + str(i)]["dateofBirth"]
    payload["shoeSize"] = task["task_" + str(i)]["shoeSize"]
    payload["address1"] = task["task_" + str(i)]["address1"]
    payload["address2"] = str(task["task_" + str(i)]["address2"])
    payload["city"] = task["task_" + str(i)]["city"]
    payload["county"] = task["task_" + str(i)]["county"]
    payload["siteCode"] = task["task_" + str(i)]["siteCode"]
    payload["postCode"] = task["task_" + str(i)]["postCode"]
    payload["hostname"] = "https://raffles.footpatrol.com"
    payload["sms_optin"] = int(0)
    payload["email_optin"]=int(1)
    payload["token"]=token


payload_json= {}

client = requests.Session()
dateTimeObj = datetime.now()
print(Fore.CYAN + '[{}] Starting Session'.format(str(dateTimeObj)))
for i in range(len(task)):
    dateTimeObj = datetime.now()
    print(Fore.YELLOW + '[{}] Loading Task'.format(str(dateTimeObj)))
    updatePayload(i, token.getToken())
    payload_json = json.dumps(payload)
    dateTimeObj = datetime.now()
    print(Fore.YELLOW + '[{}] Getting Token'.format(str(dateTimeObj)))
    r = client.post(POST_URL, headers=headers, data=payload_json)

    if r.status_code == 200 or r.status_code == 201:
        dateTimeObj = datetime.now()
        print(Fore.GREEN + '[{}] Raffle Entry Complete'.format(str(dateTimeObj)))
    else:
        dateTimeObj = datetime.now()
        print(Fore.RED + '[{}] Raffle Entry Not Completed'.format(str(dateTimeObj)))
