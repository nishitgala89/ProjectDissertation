from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
import json
import time
import pandas as pd
import logging

logging.basicConfig(filename='MutualFunds.log', filemode='w', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def loadBrowserUrl(driver,final_url):
    try:    
        driver.get(final_url)          
        #print("Final URL ---> " ,final_url)
        driver.implicitly_wait(4)
        time.sleep(3)
        driver.maximize_window() 
        logging.info("Successfully Loaded URL -->  " +  final_url)
    
    except:
        logging.warning("Unable to Load URL for -->  "+ final_url)
        pass

def userDialogHandle(driver):     

    # Initial Investor Option Dialog
    
    driver.find_element_by_xpath("//span[@id='individualinvestor']/span[1]").click()
    driver.find_element_by_id("_evidon-accept-button").click()
    driver.refresh()
    
    try:
        userDialogHandle(driver)
    except:
        pass
    time.sleep(1)

replace_string = "replace_value"

chrome_opt = Options()  
chrome_opt.add_argument("--headless") 
driver = webdriver.Chrome(executable_path = './chromedriver',chrome_options = None,)


base_url = "https://www.morningstar.co.uk/uk/funds/snapshot/snapshot.aspx?id="
#mf_id = "F000002YHY"
end_url = "&tab=3"

df = pd.read_csv('./Mutual_Funds/TestBatch.csv')

fund_ids = df["SecId"].to_list()
n = 5

batchSize =  len(fund_ids) //n  if len(fund_ids) % 5 == 0  else len(fund_ids) //n + 1

logging.info("Total Samples  -->  " +  str(len(fund_ids)) )
logging.info("Total batches  -->  " +  str(batchSize))

batch = [fund_ids[count * n : (count+1) * n] for count in range(batchSize) ]


style_measures_xpath = "(.//div[@class=\'sal-measures__value-table\']/table/tbody/tr[replace_value]/td[2])[1]"
holdings_xpath = ".//div[@class=\'sal-holdings__summaryBand\']/ul/li[replace_value]/div/div[2]"
sector_xpath = "//table[@class=\'sal-sector-exposure__sector-table\']/tbody/tr"
equity_holdings_xpath = "(//table[@class='sal-holdings__tableWhenEquity'])[2]/tbody/tr"
# For Fund of Funds
fund_holdings_xpath = "(//table[@class='sal-holdings__tableWhenOthers'])[2]/tbody/tr"

factor_profile_fundValue_xpath = "(//tr[@class='sal-mip-factor-profile__table-data'])[replace_value]/td[2]"
factor_profile_5min_xpath = "(//tr[@class='sal-mip-factor-profile__table-data'])[replace_value]/td[3]"
factor_profile_5max_xpath = "(//tr[@class='sal-mip-factor-profile__table-data'])[replace_value]/td[4]"

market_cap_xpath = "(.//div[@class='sal-market-cap__value-table']/table/tbody)[1]/tr"

def fetchStyleSheet(style_measures_dict):
    style_measures_dict["P_E"] = driver.find_element_by_xpath(style_measures_xpath.replace(replace_string,"1")).text
    style_measures_dict["P_B"] = driver.find_element_by_xpath(style_measures_xpath.replace(replace_string,"2")).text
    style_measures_dict["P_Sales"] = driver.find_element_by_xpath(style_measures_xpath.replace(replace_string,"3")).text
    style_measures_dict["P_CashFlow"] = driver.find_element_by_xpath(style_measures_xpath.replace(replace_string,"4")).text
    style_measures_dict["Dividend_Yield_Percent"] = driver.find_element_by_xpath(style_measures_xpath.replace(replace_string,"5")).text
    style_measures_dict["Long_term_earning_Percent"] = driver.find_element_by_xpath(style_measures_xpath.replace(replace_string,"6")).text
    style_measures_dict["Historical_earning_Percent"] = driver.find_element_by_xpath(style_measures_xpath.replace(replace_string,'7')).text
    style_measures_dict["Sales_growth_percent"] = driver.find_element_by_xpath(style_measures_xpath.replace(replace_string,'8')).text
    style_measures_dict["Cashflow_growth_percent"] = driver.find_element_by_xpath(style_measures_xpath.replace(replace_string,'9')).text
    style_measures_dict["Book_value_growth_percent"] = driver.find_element_by_xpath(style_measures_xpath.replace(replace_string,'10')).text
    return style_measures_dict

def fetchFactorProfileDetails(factor_profile_dict):
    factor_profile_dict["SecId"] = mf_id
    factor_profile_dict['Style'] = driver.find_element_by_xpath(factor_profile_fundValue_xpath.replace(replace_string,"1")).text
    factor_profile_dict['Style_5_Min'] = driver.find_element_by_xpath(factor_profile_5min_xpath.replace(replace_string,"1")).text
    factor_profile_dict['Style_5_Max'] = driver.find_element_by_xpath(factor_profile_5max_xpath.replace(replace_string,"1")).text

    factor_profile_dict['Yield'] = driver.find_element_by_xpath(factor_profile_fundValue_xpath.replace(replace_string,"2")).text
    factor_profile_dict['Yield_5_Min'] = driver.find_element_by_xpath(factor_profile_5min_xpath.replace(replace_string,"2")).text
    factor_profile_dict['Yield_5_Max'] = driver.find_element_by_xpath(factor_profile_5max_xpath.replace(replace_string,"2")).text

    factor_profile_dict['Momentum'] = driver.find_element_by_xpath(factor_profile_fundValue_xpath.replace(replace_string,"3")).text
    factor_profile_dict['Momentum_5_Min'] = driver.find_element_by_xpath(factor_profile_5min_xpath.replace(replace_string,"3")).text
    factor_profile_dict['Momentum_5_Max'] = driver.find_element_by_xpath(factor_profile_5max_xpath.replace(replace_string,"3")).text

    factor_profile_dict['Quality'] = driver.find_element_by_xpath(factor_profile_fundValue_xpath.replace(replace_string,"4")).text
    factor_profile_dict['Quality_5_Min'] = driver.find_element_by_xpath(factor_profile_5min_xpath.replace(replace_string,"4")).text
    factor_profile_dict['Quality_5_Max'] = driver.find_element_by_xpath(factor_profile_5max_xpath.replace(replace_string,"4")).text

    factor_profile_dict['Volatility'] = driver.find_element_by_xpath(factor_profile_fundValue_xpath.replace(replace_string,"5")).text
    factor_profile_dict['Volatility_5_Min'] = driver.find_element_by_xpath(factor_profile_5min_xpath.replace(replace_string,"5")).text
    factor_profile_dict['Volatility_5_Max'] = driver.find_element_by_xpath(factor_profile_5max_xpath.replace(replace_string,"5")).text

    factor_profile_dict['Liquidity'] = driver.find_element_by_xpath(factor_profile_fundValue_xpath.replace(replace_string,"6")).text
    factor_profile_dict['Liquidity_5_Min'] = driver.find_element_by_xpath(factor_profile_5min_xpath.replace(replace_string,"6")).text
    factor_profile_dict['Liquidity_5_Max'] = driver.find_element_by_xpath(factor_profile_5max_xpath.replace(replace_string,"6")).text

    factor_profile_dict['Size'] = driver.find_element_by_xpath(factor_profile_fundValue_xpath.replace(replace_string,"7")).text
    factor_profile_dict['Size_5_Min'] = driver.find_element_by_xpath(factor_profile_5min_xpath.replace(replace_string,"7")).text
    factor_profile_dict['Size_5_Max'] = driver.find_element_by_xpath(factor_profile_5max_xpath.replace(replace_string,"7")).text

    return(factor_profile_dict)

for count in range(len(batch)):
    # For Part 1
    style_measures_list =[]

    # For Part 2
    holdings_list=[]

    # For Part 3
    top_equity_holdings_list =[]

    # For Part 4
    factor_profile_list=[]

    # For part 5
    market_cap_list = []


    for i in range(len(batch[count])):
        style_measures_dict = {}
        holdings_dict={}
        sector_list =[]
        top_equity_holdings_dict = {}
        factor_profile_dict ={}
        market_cap_dict = {}

        mf_id = batch[count][i]
        final_url = base_url + mf_id + end_url
        
        loadBrowserUrl(driver,final_url)
        try:
            userDialogHandle(driver)
        except:
            logging.info("No Dialog to Handle")
        
                    
        # Initial Investor Option Dialog
        # driver.find_element_by_xpath("//span[@id='individualinvestor']/span[1]").click()
        # driver.find_element_by_id("_evidon-accept-button").click()

        
        # # Refresh to reload the DOM
        # driver.refresh()
        

        # Switch to the Iframe
        try:
            driver.switch_to.frame("portfolio")
        except:
            loadBrowserUrl(driver,final_url)
            try:
                logging.info("No Dialog to handle for ---> " + mf_id)                
                userDialogHandle(driver)              
            except:
                loadBrowserUrl(driver,final_url)
                try:
                    userDialogHandle(driver)  
                except:
                    logging.info("No Dialog to handle for ---> " + mf_id)        
            try:
                driver.switch_to.frame("portfolio")
            except:
                logging.critical("Issue with URL, Cannot Switch to Iframe Portfolio --> "+ mf_id)
                continue        
        
            # Part 1 - Capture the Style Measures 
        style_measures_dict["SecId"] = mf_id
        try:
            style_measures_dict = fetchStyleSheet(style_measures_dict)
            
        except:
            logging.warning("Issue with URL, Retrying capturing Style Sheet parameters --> "+ mf_id)
            loadBrowserUrl(driver,final_url)
            try:
                userDialogHandle(driver)    
            except:
                pass
            try:
                driver.switch_to.frame("portfolio")
            except:
                logging.critical("Issue with URL, Cannot Switch to Iframe Portfolio --> "+ mf_id)
                continue   
            style_measures_dict = fetchStyleSheet(style_measures_dict)

                


        style_measures_list.append(style_measures_dict)

        time.sleep(1)
        

        # Part 2 - Capture the Holdings Data
        

        holdings_dict["SecId"] = mf_id
        holdings_dict["Equity_Holding"] = driver.find_element_by_xpath(holdings_xpath.replace(replace_string,"2")).text
        holdings_dict["Other_Holding"] = driver.find_element_by_xpath(holdings_xpath.replace(replace_string,"4")).text
        holdings_dict["Assets_in_top10_holdings_percent"] = driver.find_element_by_xpath(holdings_xpath.replace(replace_string,"5")).text
        holdings_dict["Reported_turnover_percent"] = driver.find_element_by_xpath(holdings_xpath.replace(replace_string,"6")).text
        # This field not present in all funds
        try:
            holdings_dict["Active_Share_percent"] = driver.find_element_by_xpath(holdings_xpath.replace(replace_string,"7")).text
        except:
            logging.warning("Active Share Percent not available for -->  "+ mf_id)
                   
        try:
            
            sector_rows = driver.find_elements_by_xpath(sector_xpath)

            for j in range(1,len(sector_rows)+1):
                sector_list.append(driver.find_element_by_xpath(sector_xpath + "[" + str(j) + ']/td[2]').text)

            sector_list = [float(item) for item in sector_list]

            sector_list.sort(reverse=True)
            #print("Holding Dict ==>", holdings_dict)
            #print("Sector List ==>",sector_list)

            holdings_dict["Top3_sector_percent"] = round(sector_list[0] +  sector_list[1] + sector_list[2],2)
            holdings_dict["Top5_sector_percent"] = round(sector_list[0] +  sector_list[1] + sector_list[2] + sector_list[3] + sector_list[4],2)
        except:
            logging.warning("Sector Percent details not scrapped for -->  " + mf_id)
            pass
        
        #print("Holding Dict ==>", holdings_dict)
        holdings_list.append(holdings_dict)
        time.sleep(1)

        # Part 3 - ---------- Top 10 Equity Holdings ------------------

        equity_rows = driver.find_elements_by_xpath(equity_holdings_xpath)

        if len(equity_rows) <= 1 :
            # This is Fund of Fund hence need to re calculate 
            logging.info("Seems to be a Fund of Fund -->  " + mf_id)
            equity_rows = driver.find_elements_by_xpath(fund_holdings_xpath)
            if len(equity_rows) > 1:
                equity_xpath = fund_holdings_xpath
        else:
            equity_xpath = equity_holdings_xpath
             
        top_equity_holdings_dict["SecId"] = mf_id
        if len(equity_rows) > 1:
            for j in range(2,len(equity_rows)+1):
                top_equity_holdings_dict['company_' + str(j-1)] = driver.find_element_by_xpath(equity_xpath + "[" + str(j) + ']/td').text
                top_equity_holdings_dict['percent_' + str(j-1)] = driver.find_element_by_xpath(equity_xpath + "[" + str(j) + ']/td[2]').text
        else:
            logging.warning("Top Equity Holdings details not scrapped for -->  " + mf_id)
            pass

        top_equity_holdings_list.append(top_equity_holdings_dict)
        time.sleep(1)

        ###### Part 4 - Getting the Factor Profile 
        
        try:
            driver.find_element_by_xpath('.//button[1]/span[1]/*[1]').click()
            factor_profile_dict = fetchFactorProfileDetails(factor_profile_dict)
        except:
            try: 
                driver.find_element_by_xpath('(.//button[1]/span[1]/*[1])[1]').click()
                factor_profile_dict = fetchFactorProfileDetails(factor_profile_dict)
            except:
                logging.warning("Unable to switch to Factor Profile table details using button click for -->  " + mf_id)
                pass
        

        factor_profile_list.append(factor_profile_dict)

        time.sleep(1)
        ### Part 5 - Getting the Market Cap Details (Select Style Measures as Market Cap)

        #driver.find_element_by_xpath('(.//span[contains(text(),\'Measures\')])[1]').click()
        #driver.find_element_by_xpath('.//span[contains(text(),\'Market Cap\')]').click()
        
        try:
            driver.find_element_by_xpath(".//input[@value='Market Cap']").click()            
        except:
            logging.info("Unable to scrap details of Market Cap for  -->  " + mf_id)        
        #print("No User Dialog to handle")
            continue

        market_cap_dict["SecId"] = mf_id
        market_cap_dict["Equity_Holding"] = driver.find_element_by_xpath(".//div[@class='sal-market-cap__summary']/ul/li[1]/div/div[2]").text
        
        try:
            market_cap_rows = driver.find_elements_by_xpath(market_cap_xpath)

            for j in range(1,len(market_cap_rows)+1):
                size = driver.find_element_by_xpath(market_cap_xpath + '['+ str(j) + ']/td[1]').text
                if size.upper() == "GIANT":
                    market_cap_dict["giant_percent"] = driver.find_element_by_xpath(market_cap_xpath + '['+ str(j) + ']/td[2]').text
                elif size.upper() == "LARGE":
                    market_cap_dict["large_percent"] = driver.find_element_by_xpath(market_cap_xpath + '['+ str(j) + ']/td[2]').text
                elif size.upper() == "MID":
                    market_cap_dict["mid_percent"] = driver.find_element_by_xpath(market_cap_xpath + '['+ str(j) + ']/td[2]').text
                elif size.upper() == "SMALL":
                    market_cap_dict["small_percent"] = driver.find_element_by_xpath(market_cap_xpath + '['+ str(j) + ']/td[2]').text
                elif size.upper() == "MICRO":
                    market_cap_dict["micro_percent"] = driver.find_element_by_xpath(market_cap_xpath + '['+ str(j) + ']/td[2]').text
        except:
            pass

        market_cap_list.append(market_cap_dict)
        logging.info("Detailes Scrapped Successfully for -->  " + mf_id)
        
        time.sleep(1)

    output_dict = {"Style_Measures" : style_measures_list ,
                    "Holdings" : holdings_list,
                    "Top_Equities" : top_equity_holdings_list,
                    "Factor_Profile": factor_profile_list,
                    "Market_Cap" : market_cap_list
                    }        


    with open('MutualFundsScrapped_test_' + str(count+1) + '.json', 'w') as fp:
        json.dump(output_dict,fp,indent=4)

time.sleep(2)

driver.quit()
