import requests
from bs4 import BeautifulSoup
import re
import time
class priceTracer:
    def __init__(self,url):
        self.url=url
        self.user_agent={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"}
        self.response=requests.get(url=self.url,headers=self.user_agent).text
        self.soup=BeautifulSoup(self.response,"lxml")
    def Product_title(self):
        title=self.soup.find("span",{"id": "productTitle"})
        if title is not None:
            return title.text.strip()
        else:
            return "Title not found"
    def Product_price(self):
        price=self.soup.find("span",{"class": "a-price-whole"})
        if price is not None:
            return price.text
        else:
            return "Price not found"
    def clean_price(self,price):
        cleaned=re.sub(r'[₹,]','',price)
        try:
            return float(cleaned)
        except:
            return None
    # this function will check the price drop and compare it with the target price which i gave it has 60000
    def check_price_drop(self,target_price):
        title=self.Product_title()
        price=self.Product_price()
        if price=="Price not found":
            print("price not found")
            return
        price_value=self.clean_price(price)
        if price_value is None:
            print("Invalid price format")
            return 
        print(f'\n Product:{title}\n current price:{price_value}')
        if price_value<=target_price:
            print("Price Drop ALERT!")
        else:
            print(f"price is still higher than target {target_price}")
    # this is the function that will track it for every 1 hour i used time module 
    def track(self,target_price,interval=3600):
        
        while True:
            self.__init__(self.url)
            self.check_price_drop(target_price)
            print(f"checking again in {interval} seconds.\n")
            time.sleep(interval)
# im using the while loop which enter into the infinite loop but need to kill the terminal to stop it.


device=priceTracer(url="https://www.amazon.in/Nikon-Digital-Camera-16-50mm-50-250mm/dp/B0B695LX4F/ref=sr_1_1?dib=eyJ2IjoiMSJ9.gyUiMCQVBouaK86RyM6KIbzvRgr5fgEtQkl5xJ3L1qqZS9_eORTlU_U-BOyUy339onnYj-l-H9c0H8Msd7f4EWyfW2rctZN5uG4z0owda_DJCRRhzLwAwGpeC0MwBDXA9gyf1U2Sfm89tiRACmZ0NWoqcIejsP0v6R-qbSHsrWu7Wl7MsxlcUIy9MoXB-2IMH3jq7MoeZ1WkVNAJ_PEahnhGljaXVCs8pPOB6oWJ7QKN7UZRY2wTzXSokXSIBT5lGO_MpWPXK_zbe7p59U7l2p0N30udhxHdJIG-V1YKl1E.1cGs5GF0tVy17ReZMEynk2bjoJn6EPpFTktKa-gnKzY&dib_tag=se&pf_rd_i=1388977031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=merchandised-search-8&qid=1775196232&sr=8-1")
device.check_price_drop(target_price=60000)
device.track(60000,interval=7200)
#print(device.Product_title())
#print(device.Product_price())