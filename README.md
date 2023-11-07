# Product Price Comparison Tool

## Overview
The Product Price Comparison Tool is a Python command-line application that allows users to compare the prices of products on Amazon and Flipkart. It provides a convenient way to find the best deals on your desired products across these popular e-commerce platforms.

This README file provides an overview of the project, its features, and instructions on how to use it.

## Features
- Search for Products: You can search for products on both Amazon and Flipkart by providing the product name. The tool will fetch the results and display the product name, price, and a link to the product page.

- Compare Products: You can compare the prices of two products, one from Amazon and one from Flipkart. Simply provide the links to the product pages, and the tool will display the product details and inform you which platform offers a better price.

- Internet Connection Check: The tool checks for an internet connection before making requests to the e-commerce websites. If there is no internet connection, it will inform the user.

- Error Handling: The tool includes error handling to provide clear messages when there are issues with fetching data from Amazon or Flipkart.

## Installation
1. Clone the repository to your local machine:
   ```
   git clone https://github.com/arthurW1935/product-price-scraper
   ```

2. Navigate to the project directory:
   ```
   cd product-price-scraper
   ```

3. Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

## Usage
To use the Product Price Comparison Tool, follow these steps:

1. Run the main.py file:
   ```
   python main.py
   ```

2. The tool will display a menu with the following options:
   - **Search for products by name**: Enter '1' to search for products on both Amazon and Flipkart by providing the product name.
   - **Compare products by link**: Enter '2' to compare the prices of two products, one from Amazon and one from Flipkart, by providing their links.
   - **Quit**: Enter '3' to exit the tool.

3. Follow the on-screen instructions to input the required information and view the results.

## Sample Usage
Here's a sample of how you can use the tool:

1. Select option 1 to search for products by name.
2. Enter the product name, e.g., "laptop."
3. Enter the maximum number of products to display.
4. The tool will fetch and display the search results from both Amazon and Flipkart.

## Notes
- The tool uses web scraping to fetch data from Amazon and Flipkart. Make sure to use it responsibly and be aware of the website's terms of service.
- The tool relies on external Python libraries for web scraping. If you encounter issues with web scraping, make sure to update the libraries to the latest versions.

## Contributions
Contributions and improvements to this project are welcome. If you'd like to contribute, please follow the [Contributing Guidelines](CONTRIBUTING.md).
