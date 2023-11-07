import flipkart_scraper
import amazon_scraper
import tabulate
import socket

amazon_scraper_object = amazon_scraper.AmazonScraper()
flipkart_scraper_object = flipkart_scraper.FlipkartScraper()


def has_connection():
    '''
    Checks Internet Connection
    '''
    try:
        socket.create_connection(('google.com',80))
        return True
    except:
        return False

def search_products_by_name():
    '''
    Searches for the product on Amazon and Flipkart and displays the results
    '''

    if not has_connection():
        print("Please check your Internet Connection!")
        return
    
    product_name = input("Enter the name of the product: ").strip()
    n_products = input("Enter the max. number of products to be displayed: ").strip()
    if not n_products.isnumeric() or int(n_products) <= 0: 
        print("Please enter a valid number which is greater than zero")
        return
    n_products = int(n_products)

    try:
        print("\n")
        print("\rHold on while we fetch the data from Amazon...",end="")
        amazon_products = amazon_scraper_object.get_products_by_name(product_name, n_products=n_products)
        print(f"\rSearch results on Amazon: (found {len(amazon_products)} results)")
        if len(amazon_products) == 0:
            print("No results found on Amazon")
        else:
            table = [["Product Name", "Price (in ₹)", "Link"]]
            for i in amazon_products:
                table.append([i["product_name"], i["price"], i["link"]])
            print(tabulate.tabulate(table, headers="firstrow", tablefmt="fancy_grid", maxcolwidths=[30, 10, 90]))
    
    except Exception as e:
        print("\rError while fetching data from Amazon!")

    try:
        print()
        print("\rHold on while we fetch the data from Flipkart...",end="")
        flipkart_products = flipkart_scraper_object.get_products_by_name(product_name, n_products=n_products)
        print(f"\rSearch results on Flipkart: (found {len(flipkart_products)} results)")
        if len(flipkart_products) == 0:
            print("No results found on Flipkart")
        else:
            table = [["Product Name", "Price (in ₹)", "Link"]]
            for i in flipkart_products:
                table.append([i["product_name"], i["price"], i["link"]])
            print(tabulate.tabulate(table, headers="firstrow", tablefmt="fancy_grid", maxcolwidths=[30, 10, 90]))
    except Exception as e:
        print("\rError while fetching data from Flipkart!")

def compare_products_by_link():
    '''
    Compares the price of two products on Amazon and Flipkart
    Takes user input of the links of the products and compares them
    '''

    if not has_connection():
        print("Please check your Internet Connection!")
        return
    
    amazon_product_link = input("Enter the link of the product on Amazon: ")
    print()
    flipkart_product_link = input("Enter the link of the product on Flipkart: ")
    print()

    try:
        amazon_product = amazon_scraper_object.get_products_by_link(amazon_product_link)
    except ValueError as e:
        print("Please enter valid Amazon link!")
        return
    except Exception as e:
        print("Error while fetching data from Amazon!")
        return

    try:
        flipkart_product = flipkart_scraper_object.get_products_by_link(flipkart_product_link)
    except ValueError as e:
        print("Please enter valid Flipkart link!")
        return
    except Exception as e:
        print("Error while fetching data from Flipkart!")
        return

    if not amazon_product:
        print("No product found on Amazon")
    else:
        print("\nProduct on Amazon:")
        table = [["Product Name", "Price (in ₹)", "Link"], [amazon_product["product_name"], amazon_product["price"], amazon_product["link"]]]
        print(tabulate.tabulate(table, headers="firstrow", tablefmt="fancy_grid", maxcolwidths=[30, 10, 90]))
    if not flipkart_product:
        print("No product found on Flipkart")
    else:
        print("\nProduct on Flipkart:")
        table = [["Product Name", "Price (in ₹)", "Link"], [flipkart_product["product_name"], flipkart_product["price"], flipkart_product["link"]]]
        print(tabulate.tabulate(table, headers="firstrow", tablefmt="fancy_grid", maxcolwidths=[30, 10, 90]))

    print("\nComparison Results:")
    if amazon_product and flipkart_product:
        if amazon_product["price"] < flipkart_product["price"]:
            print("The price is cheaper at Amazon!")
        elif amazon_product["price"] > flipkart_product["price"]:
            print("The price is cheaper at Flipkart!")
        else:
            print("The price is the same in both Amazon and Flipkart!")

    else:
        print("Insufficient information to compare!")

def main_menu():
    print("WELCOME TO THE PRODUCT PRICES SCRAPER".center(100, "-"))
    print("This is a command line interface to compare prices of products on Amazon and Flipkart!")
    print()

    while True:
        print("\nMain Menu:")
        print("1. Search for products by name")
        print("2. Compare products by link")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            search_products_by_name()
        elif choice == '2':
            compare_products_by_link()
        elif choice == '3':
            print("Thank you for using our service!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()
