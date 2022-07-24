import requests
import schedule
import time
channelid=input(f'チャンネルID: ')
t0ken='YOUR TOKEN'
d = open('words.txt', 'r', encoding="utf-8")
mess = d.read()
def qawsed():
    payload={
        'content':mess
    }
    header={
    'authorization':t0ken
    }
    r=requests.post("https://discord.com/api/v9/channels/"+channelid+"/messages",data=payload,headers=header)
    print(mess+"send")
schedule.every(1).minutes.do(qawsed)

while True:
    schedule.run_pending()
    time.sleep(1)
