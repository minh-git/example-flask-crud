import urllib.request

bank_pdf_list = [
"http://www.bom.gov.au/fwo/IDV60901/IDV60901.95936.axf"]


def get_pdf(url):
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    
    #url = "https://www.yesbank.in/pdf/forexcardratesenglish_pdf"
    headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
      'AppleWebKit/537.11 (KHTML, like Gecko) '
      'Chrome/23.0.1271.64 Safari/537.11',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
      'Accept-Encoding': 'none',
      'Accept-Language': 'en-US,en;q=0.8',
      'Connection': 'keep-alive'}
    
    request=urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    #print(response.text)
    data = response.read()
#    print(type(data))
    
    name = url.split("www.")[-1].split("//")[-1].split(".")[0]+"_FOREX_CARD_RATES.pdf"
    f = open(name, 'wb')
    f.write(data)
    f.close()
    

for bank_url in bank_pdf_list:
    try: 
        get_pdf(bank_url)
    except Exception as e:
        print(e)
        pass