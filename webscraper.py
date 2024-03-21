from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Web_Data"

def scrapeMarket():
    dataSize = 0
    pageToScrape = requests.get("https://steamcommunity.com/market/")
    soup = BeautifulSoup(pageToScrape.text, "html.parser")

    # titles = soup.findAll ('span', attrs = {'class':'market_listing_item_name'})
    # for title in titles:
    #     print (title.txt)

    data=[]
    authors = soup.findAll('span', attrs= {'class':'normal_price'})
    for author in authors:
        data.append(author)
        dataSize = dataSize + 1

    for i in range (1,dataSize):
        cellref = ws.cell(row=i, column = 1)
        cellref.value = (data[i]).text
    
    wb.save("Data_Entry.xlsx")

scrapeMarket()

