import json
import os

Path = "E:\\Nishit\\Mutual_Fund_Scrapped\\Europe\\Batch_"

featureList = ["Style_Measures","Holdings","Top_Equities","Factor_Profile","Market_Cap"]

style_Measures_list = []
holdings_list = []
top_equities_list = []
factor_profile_list = []
market_cap_list = []

style_measures_json = {}
holdings_json = {}
top_equities_json = {}
factor_profile_json = {}
market_cap_json = {}

for count in range(10,30):
    batchPath = Path + str(count)
    #print(batchPath)
    lst = os.listdir(batchPath)
    for file_ in lst:
        if file_.__contains__("json"):
            #print(file_)
            f =open(batchPath + "\\" + file_)
            data = json.load(f)
            for feature in featureList:
                for eachItem in data[feature]:
                    if feature.__contains__("Style"):
                        style_Measures_list.append(eachItem)
                    elif feature.__contains__("Holdings"):
                        holdings_list.append(eachItem)
                    elif feature.__contains__("Top"):
                        top_equities_list.append(eachItem)
                    elif feature.__contains__("Factor"):
                        factor_profile_list.append(eachItem)
                    elif feature.__contains__("Market"):
                        market_cap_list.append(eachItem)


style_measures_json["Style_Measures"] = style_Measures_list
holdings_json["Holdings"] = holdings_list
top_equities_json["Top_Equities"] = top_equities_list
factor_profile_json["Factor_Profile"] = factor_profile_list
market_cap_json["Market_Cap"] = market_cap_list
#print(style_measure_json)    

with open("Style_Measures.json", 'w') as fp:
    json.dump(style_measures_json, fp,indent=4)

with open("Holdings.json", 'w') as fp:
    json.dump(holdings_json, fp,indent=4)

with open("Top_Equities.json", 'w') as fp:
    json.dump(top_equities_json, fp,indent=4)

with open("Factor_Profile.json", 'w') as fp:
    json.dump(factor_profile_json, fp,indent=4)

with open("Market_Cap.json", 'w') as fp:
    json.dump(market_cap_json, fp,indent=4)