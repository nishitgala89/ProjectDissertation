import pandas as pd
import math
import TickerLookup
df = pd.read_csv(".\Mutual_Funds\Top_Equities_UK.csv")

top_3_companies = df[['company_1','company_2','company_3']].values.ravel()

unique_top3_companies = pd.unique(top_3_companies)
unique_top3_companies = list(unique_top3_companies)

#print(unique_top3_companies)
print(len(unique_top3_companies))
unique_top3_companies = [x for x in unique_top3_companies if 'nan' != str(x)]
print(len(unique_top3_companies))

company_ticker_map = {}

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
    
    try:
        ticker = TickerLookup.getTicker(companyName)
        company_ticker_map[full_company_name] = ticker
        
    except Exception as e:
        company_ticker_map[full_company_name] = "NONE"
        pass

import json
import os
filename ="Company_Ticker_Map.json"
fpath = os. path. join("./MutualFunds_TickerData/", filename)
with open(fpath, "w") as json_file:
    json.dump(company_ticker_map, json_file, indent = 4) 
    

