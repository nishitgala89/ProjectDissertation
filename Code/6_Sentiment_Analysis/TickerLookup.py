from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

ticker_lookup_url = "https://www.marketwatch.com/tools/quotes/lookup.asp?siteID=mktw&Lookup=###&Country=uk&Type=Stock"

def getTicker(companyName):
    
    url = ticker_lookup_url.replace("###",companyName)
    req = Request(url=url,headers={'user-agent': 'my-app/0.0.1'}) 
    response = urlopen(req)    

    # Read the contents of the file into 'html'
    soup = BeautifulSoup(response, "html.parser")
    results = soup.find(class_ = "results")
    tbody = results.find(lambda tag: tag.name=='tbody')
    anchor_tag =  tbody.find(lambda tag: tag.name=='a' )
    ticker = anchor_tag.get_text()
    ticker = ticker.split(":")[1]
    return ticker

# Note - Ticker should not have spaces and can only contain 2 words
print(getTicker("UnileverPLC"))