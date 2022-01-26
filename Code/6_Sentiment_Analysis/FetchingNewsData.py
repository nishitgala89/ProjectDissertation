import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import TickerLookup
import json
import os
import logging
import math

logging.basicConfig(filename='FetchingTickerNewsData.log', filemode='w', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

news_data_lookup_url = "https://www.marketwatch.com/investing/stock/###?countrycode=UK"

url = news_data_lookup_url

def fetchNewsData(ticker, full_co_name):    
    url = news_data_lookup_url.replace("###",ticker)
    req = Request(url=url,headers={'user-agent': 'my-app/0.0.1'}) 
    response = urlopen(req)    

    # Read the contents of the file into 'html'
    soup = BeautifulSoup(response, "html.parser")
    results = soup.find(class_ = "collection__elements")    
    lst =[]
    for tag in results.find_all('a'):
        if full_co_name.split(" ")[0] in tag.text:
            tmp = tag.text
            tmp=tmp.strip()
            lst.append(tmp)
    
    return lst


### Part 1 - Getting the unique Stock List comprising of Top 3 stocks of UK funds using pandas

df = pd.read_csv(".\Mutual_Funds\Top_Equities_UK.csv")

top_3_companies = df[['company_1','company_2','company_3']].values.ravel()

unique_top3_companies = pd.unique(top_3_companies)
unique_top3_companies = list(unique_top3_companies)

unique_top3_companies = [x for x in unique_top3_companies if 'nan' != str(x)]

# # print(unique_top3_companies)

#unique_top3_companies = ["Reach PLC","Domino's Pizza Group PLC"]

### Part 2 - Fetching the latest News Data from FinWiz Business Website and saving it as JSON

for company in unique_top3_companies:
    full_company_name =company
    #company = company.replace("'","")
    split_co = company.split(" ")    
    #print(len(split_co))
    #print(full_company_name.split(" ")[0])
    
    if len(split_co) >= 3:
        companyName = split_co[0] + "+" + split_co[1] + "+" + split_co[2]  
    else:
        companyName = company.replace(" ","")
  
    print(companyName)
    ticker_news_dict = {}
    ticker = ""
    news_headlines_list=[]
    try:
        ticker = TickerLookup.getTicker(companyName)
        
    except Exception as e:
        logging.error("Cannot process News Data for company: {}-->".format(full_company_name))
        logging.error("Reason --> Unable to fetch News Ticker")
        logging.error(e)

    if ticker is None:  
        pass
    else:      
        try:
            news_headlines_list = fetchNewsData(ticker,full_company_name)
        except Exception as e:
            logging.error("Cannot process News Data for company {}-->".format(full_company_name))
            logging.error("URL: {}-->".format(url))
            logging.error(e)

        if len(news_headlines_list) > 0:
            ticker_news_dict["News"] = news_headlines_list
            filename = ticker + ".json"
            fpath = os. path. join("./MutualFunds_TickerData/", filename)

            with open(fpath, "w") as json_file:
                json.dump(ticker_news_dict, json_file, indent = 4) 
                logging.info("Processed News Data for company {} with Ticker {} and saved to file {}".format(full_company_name, ticker,filename))
                
    
    
    
    
