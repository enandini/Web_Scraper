#for grabbing web details
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import pandas as pd 
import numpy as np


def parsePage(pageNumber):

    quote_page = 'https://www.workana.com/jobs?query=data+scientist&publication=any&language=en&page=' + str(pageNumber)
    page = urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')
    #next_page_link = quote_page+ elm['href']

    #extract titles
    title_box = soup.findAll('h2', attrs={'class': 'h2 project-title'})
    for each in title_box:
        #title = each.text.strip()
        title = each.text.strip().encode('utf-8')
        #print (title)
        title_col.append(title)
        #response = requests.get(next_page_link)


    #extract project descriptions
    project_det = soup.findAll('div', attrs={'class': 'html-desc project-details'})
    for each1 in project_det:
        proj = each1.text.strip().encode('utf-8')
        #proj = each1.text.strip()
        #print (project_det)
        project_col.append(proj)
        #response = requests.get(next_page_link)

    #title_col2 = np.transpose(title_col)
    #project_col2 = np.transpose(project_col)

#pagination

farPage = 'https://www.workana.com/jobs?query=data+scientist&publication=any&language=en&page=100'
endPage = urlopen(farPage)
endPageSoup = BeautifulSoup(endPage, 'html.parser')
pagination = endPageSoup.find('ul', attrs={'class': 'pagination'}).findAll('a')
pagination = pagination[len(pagination) - 2].string
endPageN = int(pagination)

title_col =  []
project_col = []

for i in range(1, endPageN):
    parsePage(i)

#creating data frame
df = pd.DataFrame(project_col, title_col)
df.to_csv('Workana_1.csv', header=False)




