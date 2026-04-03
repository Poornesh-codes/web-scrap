i used import requests from which i can scrap the web , and bs4 BeautifulSoul gives me to find the id or span tag , 
i used re to clean if t contains rupee symbol , and used time for the track loop , for the given interval i gave 7200
i made a class called priceTracer in which 
in the class the self.user_agent acts as a brower , self.response fetchs webpages html

i used a header : user_agent mimic a real browser and avoid getting blocked by Amazon
bs4 helps me find id or span tag

self.soup convert html to lxml
in Product_title function from the help of self.soup to find the title of product and .strip to extract clean text 

I also handled cases where price or title is not found to avoid runtime errors

and function product_price to scrap the price
i made a clean_price  function to convert the string to floot value to compare with target price

made a check_price_drop function which compares the price and if found it gives alert messge 

self.__init__(self.url) to update the webpage each time 

and finally with the function track with time tnterval as 7200 while calling the function 
and used a while loop which is true this makes it to enter in infinite loop but every time interval it gives the messaage
