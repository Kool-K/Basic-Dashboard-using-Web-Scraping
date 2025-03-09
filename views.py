from django.shortcuts import render

import requests
from bs4 import BeautifulSoup
import time

URL = "https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data"

country_names=[]
total_cases=[]
total_deaths=[]
combined_data=[]
# dir=()
# () defines a tuple [] defines variables, we are making some empty variables and empty tuples

# get and scrape the url and get it's html content
# //get url and store content in page 1

def fetch():
    page_1=requests.get(URL)
    tmp=[]
    soup = BeautifulSoup(page_1.content, 'html.parser')
    # store entire html content/data in soup

    # we are finding table tag in the code ,
    # then we are finding the body tags in the table tag
    # we are excluding the last row since it doesn't contain data
    row= soup.find('table')
    row=row.find('tbody')
    row=row.find_all('tr')[:-1]

    for i in range (1,100):
        th=row[i].find('th')
        country_names.append(th.text.strip())
        # it means get me the country names from th table
        tds=row[i].find_all('td')[1:]
        # skip the 1st row as it contains flags
        total_cases.append(tds[0].text.strip())
        total_deaths.append(tds[1].text.strip())

    # now we have the data but it is in the form of 3 diff arrays, we have to categorie it according to the country

    # country_names=[Ind, Afg, Ban];
    # total_cases=[22,32,4]
    # total_deaths=[1,2,3]

    #we want it in this format [Ind, 22, 1] 

    for i in range (1,99):
        tmp.append(country_names[i])
        tmp.append(total_cases[i])
        tmp.append(total_deaths[i])
        combined_data.append(tmp)
        tmp=[]

fetch()
print(combined_data)

def index(req):
    return render(req,"myapp/index.html",{"combined_data":combined_data})