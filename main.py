from email.message import _PayloadType
import requests
channelid=input(f'サーバーID: ')
naiyou=input(f'送る内容：')
def qwerty():
    payload＝{
        'content':naiyou
    }
    r=reqests.post("https://discord.com/api/v9/channels/"+channelid+"/messages",data＝payload)
