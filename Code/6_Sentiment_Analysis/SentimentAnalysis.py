import pandas as pd
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


df = pd.read_csv("./Mutual_Funds/Top_Equities_UK.csv").set_index("SecId")
analyzer = SentimentIntensityAnalyzer()

#print(df.head())

# This should come from UI Dropdown selection
select_company = "F00000WRZM"

companyNameList = []
companyNameList.append(df.loc[select_company,'company_1'])
companyNameList.append(df.loc[select_company,'company_2'])
companyNameList.append(df.loc[select_company,'company_3'])
print(companyNameList)


with open("./MutualFunds_TickerData/Company_Ticker_Map.json","r") as f:
    company_ticker_map_dict = json.load(f)

tickerFileList = [v +'.json' for k,v in company_ticker_map_dict.items() if k in companyNameList]
print(tickerFileList)
tickerList=[]
newsList=[]
for fname in tickerFileList:
    with open("./MutualFunds_TickerData/" + fname,"r") as f:
        file = json.load(f)
    
    news_headlines =  file["News"]
    
    for news in news_headlines:
        tickerList.append(fname.split(".")[0])
        newsList.append(news)

news_data_dict = { "Ticker" : tickerList, "Headlines":newsList }
news_df = pd.DataFrame(news_data_dict)

    # print(newsList)
    # print(tickerList)
print(news_df)
    
scores = news_df['Headlines'].apply(analyzer.polarity_scores).tolist()
scores_df = pd.DataFrame(scores)

news_df = news_df.join(scores_df,how='right')


# mean_scores = news_df.groupby(['Ticker']).mean()
# mean_scores = mean_scores.xs('compound', axis="columns")
# #mean_scores2 =mean_scores['compound']
# print(mean_scores)

# Compound Score > 0.35 (Positive), < -0.35 (Negative), Between - Neutral
news_df['Sentiment'] = news_df['compound'].apply(lambda score: "Postive" if score > 0 else "Negative")
sentiments_df = news_df.groupby(['Ticker','Sentiment'])[['Sentiment']].count().reset_index()

print(sentiments_df)

import matplotlib.pyplot as plt



# mean_scores.plot(kind = 'bar')
# plt.grid()
# plt.show()








