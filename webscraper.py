from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook

def scrapeMarket():
    wb = Workbook()
    ws = wb.active
    ws.title = "Web_Data"

    base_url = "https://steamcommunity.com/market/"
    num_pages = 2125  # Number of pages to scrape (in this case 2125 because 2125 steam market pages for counter strike 2)

    #Lets me know how many values Im gonna be getting 
    dataSize = 0

    for page_num in range(1, num_pages + 1):
        # Construct the URL for the current page
        url = f"{base_url}?page={page_num}"
        pageToScrape = requests.get(url)
        soup = BeautifulSoup(pageToScrape.text, "html.parser")

        data = []

        authors = soup.findAll('span', attrs={'class': 'normal_price'})
        for author in authors:
            data.append(author)
            dataSize = dataSize + 1

        # Write data to the Excel sheet for the current page
        for i in range(0, dataSize):
            cellref = ws.cell(row=i + 1, column=1)  # Adjust row index to start from 1
            cellref.value = data[i].text

    wb.save("Data_Entry.xlsx")

scrapeMarket()
