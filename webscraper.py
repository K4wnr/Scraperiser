import requests
from bs4 import BeautifulSoup
from time import sleep
import os
def getNews():
    soup = BeautifulSoup(requests.get("https://www.bbc.com/news/").content, "html.parser")
    l = soup.find("div", {"class":"nw-c-most-read__items gel-layout gel-layout--no-flex"}).get_text("|",strip=True).split("|")
    for i in range(len(l)//2):
        l[i] = l[i*2]+". "+l[(i*2)+1] +"\t https://www.bbc.co.uk" + soup.find(string=l[(i*2)+1]).find_parent("a")["href"]
    return l[0:(len(l)//2)]
while True:
    os.system("cls")
    for i in getNews():
        print(i)
    sleep(20)