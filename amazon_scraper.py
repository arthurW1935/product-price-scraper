# scraping amazon website for product prices
import time
import requests
from bs4 import BeautifulSoup


class AmazonScraper:
    '''
    A class to scrape the amazon.in website for product prices
    '''
    def __init__(self):
        self.amazon_url = "https://www.amazon.in"
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
        url = self.amazon_url + "/s?k=" + keyword + "&ref=nb_sb_noss_2"
        
        tries=0
        while tries<15:
            time.sleep(0.5)
            url_obj = requests.get(url, headers=self.headers)
            if url_obj.status_code==200: break
            tries+=1
        if tries==15:
            raise Exception("Error occured while fetching the data from Amazon!")
        
        try:
            content = BeautifulSoup(url_obj.text, "html.parser")
        except Exception as e:
            raise Exception("Error occured while fetching the data from Amazon!")
        
        count=0
        products = []
        try:
            for i in content.find_all("div", {"class": "puisg-col-inner"}):
                if count>=n_products: break
                eachProduct = BeautifulSoup(str(i), "html.parser")
                name = eachProduct.find("span", {"class": "a-size-medium a-color-base a-text-normal"})
                price = eachProduct.find("span", {"class": "a-price-whole"})
                if name is not None and price is not None:
                    thisProduct = {}
                    thisProduct["product_name"] = name.get_text().strip()
                    thisProduct["price"] = float("".join([i for i in price.get_text().strip() if i.isnumeric() or i=="."]))
                    if thisProduct["price"] == 0: continue
                    count+=1
                    link = eachProduct.find("a", {"class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})
                    if link is not None: 
                        thisProduct["link"] = self.amazon_url + link["href"]
                    else:
                        thisProduct["link"] = ""
                    products.append(thisProduct)
        except:
            raise Exception("Error occured while processing the data")
        
        try:
            for i in content.find_all("div", {"class": "puis-card-container"}):
                if count>=n_products: break
                eachProduct = BeautifulSoup(str(i), "html.parser")
                name = eachProduct.find("span", {"class": "a-size-base-plus a-color-base a-text-normal"})
                price = eachProduct.find("span", {"class": "a-price-whole"})
                if name is not None and price is not None:
                    thisProduct = {}
                    thisProduct["product_name"] = name.get_text().strip()
                    thisProduct["price"] = float("".join([i for i in price.get_text().strip() if i.isnumeric() or i=="."]))
                    if thisProduct["price"] == 0: continue
                    count+=1
                    link = eachProduct.find("a", {"class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})
                    if link is not None: 
                        thisProduct["link"] = self.amazon_url + link["href"]
                    else:
                        thisProduct["link"] = ""
                    products.append(thisProduct)
        except:
            raise Exception("Error occured while processing the data")
        
        return products
    
    def get_products_by_link(self, link):
        '''
        Returns a dictionary of product with its name, price and link
        Parameters:
            link (str): The Amazon link to the product
        '''

        if not link.startswith(self.amazon_url):
            raise ValueError("Link should be a valid Amazon link")
        
        try:
            url_obj = requests.get(link, headers=self.headers)
            content = BeautifulSoup(url_obj.text, "html.parser")
            product = {}
        except:
            raise Exception("Error occured while fetching the data from amazon.in")
        
        name = content.find("span", {"id": "productTitle"})
        price = content.find("span", {"class": "a-price-whole"})

        try:
            if name is not None and price is not None:
                product["product_name"] = name.get_text().strip()
                product["price"] = float("".join([i for i in price.get_text().strip() if i.isnumeric() or i=="."]))
                product["link"] = link
        except:
            raise Exception("Error occured while processing the data")
        return product

if __name__ == "__main__":
    scraper = AmazonScraper()
    print(scraper.get_products_by_name("iphone 12"))
    print(scraper.get_products_by_link("https://www.amazon.in/dp/B0BDJH6GL8"))