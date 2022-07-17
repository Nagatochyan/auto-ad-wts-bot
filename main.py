import requests
import schedule
import time
channelid=input(f'チャンネルID: ')
naiyou=input(f'送る内容：')
t0ken=input(f'貴方のtoken:')
def qawsed():
    payload={
        'content':naiyou
    }
    header={
    'authorization':t0ken
    }
    r=requests.post("https://discord.com/api/v9/channels/"+channelid+"/messages",data=payload,headers=header)
schedule.every(1).minutes.do(qawsed)

while True:
    schedule.run_pending()
    time.sleep(1)
