import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

def dropRecordsbyRowIndex(featureName, df):
  index_val = df[df[featureName].isnull()]
  secId_to_remove = list(index_val.index.values.tolist())
  print("Removing Index --> ",secId_to_remove )
  df = df.drop(index=secId_to_remove)
  return df

def checkNullValues(df):
  null_columns = df.columns[df.isnull().any()]
  #print(df[null_columns].isnull().sum().sort_values(ascending=False))
  #print("Type --> " , type(df[null_columns].isnull().sum().sort_values(ascending=False)))
  return df[null_columns].isnull().sum().sort_values(ascending=False)

def checkNullValuesByFeature(df,featureName):
    return featureName + " has Null Values :" + str(df.PerformanceFeeActual.isnull().sum())
    
def displayCorrelationMatrix(df,titleString):
    plt.figure(figsize=(12, 4))
    heatmap = sns.heatmap(df.corr(), cmap="coolwarm", annot=True)
    heatmap.set_title(titleString, fontdict={'fontsize':18}, pad=12)

def displayCorrelationMatrixAsPerFeatureList(df,featureList,comparisonColumnName,titleString):
    featureList.append(comparisonColumnName)
    plt.figure(figsize=(12, 4))
    heatmap = sns.heatmap(df[featureList].corr(), cmap="coolwarm", annot=True)
    heatmap.set_title(titleString, fontdict={'fontsize':18}, pad=12)
    featureList.remove(comparisonColumnName)

def displayBarSubPlots(dfList,titleList,featureName, nrows=1, ncols=2):
    fig,ax = plt.subplots(nrows,ncols,figsize=(15,4))
    for i,df in enumerate(dfList):
        df.groupby(by=[featureName])[['Name']].count().plot(kind='bar',ax=ax[i], title=titleList[i])
    

def generalizeMorningStarCategories(df):
    categories = df['CategoryName'].value_counts(dropna=False)
    #type(categories)
    categories_df = pd.DataFrame(data = categories).reset_index()
    categories_df.rename(columns={"index": "category_name","CategoryName" : "value_counts"},inplace=True)
    
    #Extracting Large Funds
    tmp_df = categories_df[categories_df['category_name'].str.contains('Large')]
    large_fund_count = tmp_df['value_counts'].sum()
    large_fund_cat = tmp_df.category_name.to_list()

    #Extracting Mid/Small Funds
    tmp_df = categories_df[categories_df['category_name'].str.contains('Mid|Small')]
    small_mid_fund_count = tmp_df['value_counts'].sum()
    small_mid_fund_cat = tmp_df.category_name.to_list()

    #Extracting Flex Funds
    tmp_df = categories_df[categories_df['category_name'].str.contains('Flex')]
    flex_fund_count = tmp_df['value_counts'].sum()
    flex_fund_cat = tmp_df.category_name.to_list()

    #Extracting Income Funds
    tmp_df = categories_df[categories_df['category_name'].str.contains('Income')]
    income_fund_count = tmp_df['value_counts'].sum()
    income_fund_cat = tmp_df.category_name.to_list()

    #Calculating Miscellaneous Categories
    categories_list = categories_df.category_name.to_list()
    [categories_list.remove(element) for element in large_fund_cat]
    [categories_list.remove(element) for element in small_mid_fund_cat]
    [categories_list.remove(element) for element in flex_fund_cat]
    [categories_list.remove(element) for element in income_fund_cat]

    misc_fund_cat = categories_list
    misc_fund_count = categories_df['value_counts'].sum() - large_fund_count - small_mid_fund_count - flex_fund_count - income_fund_count

    df = df.replace(large_fund_cat,"Large-Cap")
    df = df.replace(small_mid_fund_cat,"Mid_Small-Cap")
    df = df.replace(flex_fund_cat,"Flex-Cap")
    df = df.replace(income_fund_cat,"Income")
    df = df.replace(misc_fund_cat,"Miscellaneous")

    print(df['CategoryName'].value_counts(dropna=False))

    newdf= pd.get_dummies(df.CategoryName, prefix='Cat')
    df = pd.concat([df,newdf], axis=1)
    df = df.drop(columns=['CategoryName'])

    return df

def createSize_InvestmentTypeFeature(df):
    df["Size"] = -1
    df["Style"] = -1
    df["Size"] =  df["EquityStyleBox"].apply(lambda x : 3 if (x in (7,8,9)) else (2 if (x in (4,5,6)) else 1))
    df["Style"] =  df["EquityStyleBox"].apply(lambda x : 3 if (x in (3,6,9)) else (2 if (x in (2,5,8)) else 1))
    return df


def dropColumns(df,*ColumnNames):
    colList = []
    colList = [col for col in ColumnNames]
    df = df.drop(columns = colList)
    return df

def applyLogTransformation(df,featureList):
    for feature in featureList:
        minValue = df[feature].min()
        df[feature] =  df[feature].apply(lambda x : round(math.log1p(x-minValue),4))        
    return df

def replaceMisValUsingGroupMedian(df,groupByColumn,missingValCol):
    d = df.groupby(groupByColumn)[missingValCol].median().to_dict()
    d = {key : round(d[key],2) for key in d.keys()}
    df[missingValCol] = df[missingValCol].fillna(df[groupByColumn].map(d))
    return df


def createSameFund_Flag_Feature(df):
    new_index = []
    for index,row in df.iterrows(): 
        indices = df[(df.AverageMarketCapital == row['AverageMarketCapital']) & 
                (df.ManagerTenure == row['ManagerTenure'])].index
        #print(indices.to_list())
    new_index.append(indices.to_list())

    df['SameFund_Flag'] = -1

    for lst in new_index:
        if len(lst) == 1:
            df.loc[lst[0],'SameFund_Flag'] = 2
            
        elif len(lst) == 2:
            if df.loc[lst[0],'AlphaM36'] > df.loc[lst[-1],'AlphaM36']:
                df.loc[lst[0],'SameFund_Flag'] = 1
                df.loc[lst[1],'SameFund_Flag'] = 0
            else:
                df.loc[lst[0],'SameFund_Flag'] = 0
                df.loc[lst[1],'SameFund_Flag'] = 1

        else:
            if df.loc[lst[0],'AlphaM36'] > df.loc[lst[1],'AlphaM36'] and df.loc[lst[1],'AlphaM36'] > df.loc[lst[-1],'AlphaM36'] :
                df.loc[lst[0],'SameFund_Flag'] = 2
                df.loc[lst[1],'SameFund_Flag'] = 1
                df.loc[lst[2],'SameFund_Flag'] = 0
            elif df.loc[lst[1],'AlphaM36'] > df.loc[lst[-1],'AlphaM36'] and df.loc[lst[-1],'AlphaM36'] > df.loc[lst[0],'AlphaM36'] :
                df.loc[lst[0],'SameFund_Flag'] = 0
                df.loc[lst[1],'SameFund_Flag'] = 2
                df.loc[lst[2],'SameFund_Flag'] = 1
            else:
                df.loc[lst[0],'SameFund_Flag'] = 1
                df.loc[lst[1],'SameFund_Flag'] = 0
                df.loc[lst[2],'SameFund_Flag'] = 2

    return df
