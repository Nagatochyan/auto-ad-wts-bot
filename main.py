
import requests
import schedule
import time
channelid=input(f'サーバーID: ')
naiyou=input(f'送る内容：')
t0ken="YOUR TOKEN"
def qawsed():
    payload={
        'content':naiyou
    }
    header={
    'authorization':t0ken
    }
    r=requests.post("https://discord.com/api/v9/channels/"+channelid+"/messages",data=payload,headers=header)
    print(naiyou+"send")
schedule.every(1).minutes.do(qawsed)

while True:
    schedule.run_pending()
    time.sleep(1)
