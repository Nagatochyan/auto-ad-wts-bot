import time
import requests
import schedule
channelid=input(f'サーバーID: ')
naiyou=input(f'送る内容：')
t0ken=input(f'貴方のtoken:')
teisoku=input(f'低速の時間:')
def qawsed():
    payload＝{
        'content':naiyou
    }
header={
    'authorization':t0ken
}
    r=reqests.post("https://discord.com/api/v9/channels/"+channelid+"/messages",data＝payload,headers=header)
schedule.every(teisoku).minutes.do(qawsed)
