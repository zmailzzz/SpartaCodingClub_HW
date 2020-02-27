# import pytube
# import subprocess
from bs4 import BeautifulSoup
# import time
# import os
import requests
# import re

playlist = [] #재생목록 저장용!
lists = [] #유투브 재생목록 내에 각각의 영상 링크들 저장용
url = input("https://www.youtube.com/playlist?list=PL3g4-ArZ2i-_HGN_h3xty5rZYxeljb3Xp")
# path = input("Insert your locale : ")
# path += '/'

def listParshing(url): #각 영상의 링크들을 가져오기 위한 함수
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    countlist = soup.find_all("a", class_=" spf-link playlist-video clearfix yt-uix-sessionlink spf-link ") #영상 링크들 가져오기...
    for i in range(0, len(countlist), 1):
        strchange = str(countlist[i])
        cleanr = strchange[168:187]
        lists.append("http://www.youtube.com" + "/" + cleanr) #링크 추가!
        print(countlist)
        print(lists)
        print(playlist)

