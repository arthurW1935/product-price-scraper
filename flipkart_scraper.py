# scraping flipkart website for product prices
import time
import requests
from bs4 import BeautifulSoup

class FlipkartScraper:
    '''
    A class to scrape the flipkart.com website for product prices
    '''
    def __init__(self):
        self.flipkart_url = "https://www.flipkart.com"
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OSX 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/71.0.3578.98 Safari/537.36", 
          "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"}
        
    def get_products_by_name(self, keyword, n_products=4):
        '''
        Returns a list of products with their name, price and link
        Parameters:
            keyword (str): The name of the product
            n_products (int): The number of products to be returned
        '''
        if not str(n_products).isnumeric()  or n_products<=0:
            raise ValueError("n_products should be a positive integer")

        keyword = keyword.strip().replace(" ", "+")
        url = self.flipkart_url + "/search?q=" + keyword

        tries=0
        while tries<15:
            time.sleep(0.5)
            url_obj = requests.get(url, headers=self.headers)
            if url_obj.status_code==200: break
            tries+=1
        if tries==15:
            raise Exception("Error occured while fetching the data from flipkart.com")
            
        try:
            content = BeautifulSoup(url_obj.text, "html.parser")
        except Exception as e:
            raise Exception("Error occured while fetching the data from flipkart.com")
        
        count=0
        products = []
        try:
            for i in content.find_all("div", {"class": "_2kHMtA"}):
                if count>=n_products: break
                eachProduct = BeautifulSoup(str(i), "html.parser")
                name = eachProduct.find("div", {"class": "_4rR01T"})
                price = eachProduct.find("div", {"class": "_30jeq3 _1_WHN1"})
                if name is not None and price is not None:
                    count+=1
                    thisProduct = {}
                    thisProduct["product_name"] = name.get_text().strip()
                    thisProduct["price"] = float("".join([i for i in price.get_text().strip() if i.isnumeric() or i=="."]))
                    link = eachProduct.find("a", {"class": "_1fQZEK"})
                    if link is not None: 
                        thisProduct["link"] = self.flipkart_url + link["href"]
                    else:
                        thisProduct["link"] = ""
                    products.append(thisProduct)
        except:
            raise Exception("Error occured while processing the data")
        
        try:
            for i in content.find_all("div", {"class": "_4ddWXP"}):
                if count>=n_products: break
                eachProduct = BeautifulSoup(str(i), "html.parser")
                name = eachProduct.find("a", {"class": "s1Q9rs"})
                price = eachProduct.find("div", {"class": "_30jeq3"})
                if name is not None and price is not None:
                    count+=1
                    thisProduct = {}
                    thisProduct["product_name"] = name["title"].strip()
                    thisProduct["price"] = float("".join([i for i in price.get_text().strip() if i.isnumeric() or i=="."]))
                    link = eachProduct.find("a", {"class": "s1Q9rs"})
                    if link is not None: 
                        thisProduct["link"] = self.flipkart_url + link["href"]
                    else:
                        thisProduct["link"] = ""
                    products.append(thisProduct)
        except:
            raise Exception("Error occured while processing the data")
            return products
        
        return products
    
    def get_products_by_link(self, link):
        '''
        Returns a dictionary of product with its name, price and link
        Parameters:
            link (str): The Flipkart link to the product
        '''
        if not link.startswith(self.flipkart_url):
            raise ValueError("Link should be a valid Flipkart link")

        try:
            url_obj = requests.get(link, headers=self.headers)
            content = BeautifulSoup(url_obj.text, "html.parser")
            product = {}
        except:
            raise Exception("Error occured while fetching the data from flipkart.com")
        
        name = content.find("span", {"class": "B_NuCI"})
        price = content.find("div", {"class": "_30jeq3 _16Jk6d"})

        try:
            if name is not None and price is not None:
                product["product_name"] = name.get_text().strip()
                product["price"] = float("".join([i for i in price.get_text().strip() if i.isnumeric() or i=="."]))
                product["link"] = link
        except:
            raise Exception("Error occured while processing the data")
        return product

if __name__ == "__main__":
    scraper = FlipkartScraper()
    print(scraper.get_products_by_name("toys"))
    print(scraper.get_products_by_link("https://www.flipkart.com/prekrasna-lcd-writing-slate-digital-notepad-pen-8-5-inch-screen-tablet-kids/p/itmd27bab4d2c7d0?pid=ETYGBHGXHTZPFFAG&lid=LSTETYGBHGXHTZPFFAGV8TBOW&marketplace=FLIPKART&q=toys&store=tng&srno=s_1_4&otracker=search&fm=organic&iid=4ca599e7-4cff-4f34-b697-423668772d81.ETYGBHGXHTZPFFAG.SEARCH&ppt=None&ppn=None&ssid=n57vh7c91c0000001698770601610&qH=efacc176332496ff"))