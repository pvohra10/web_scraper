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
