import csv
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

# Initialize WebDriver
driver = webdriver.Chrome()

# Query to search
#query = "Samsung"
query = input("Enter your the product name : ")
# Dictionary to store product details
products = {}

# Open Flipkart website
driver.get('https://www.flipkart.com')

# Maximize window
driver.maximize_window()

# Find search input and search button, then search for the query
input_search = driver.find_element(By.XPATH, '//input[@class="Pke_EE"]')
search_button = driver.find_element(By.XPATH, '//button[@class="_2iLD__"]')
input_search.send_keys(query)
search_button.click()

# Wait for Mobiles category link to be clickable and click on it
mobiles_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@title="Mobiles"]')))
mobiles_button.click()

# Wait for product links to appear
WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.XPATH , '//a[@class="CGtC98"]')))

# Parse the first page
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')
Block = soup.find("div", class_="DOjaWF gdgoEp")
product_links = Block.find_all("a", class_="CGtC98") 

# Parse each product
for product_link in product_links:
    product_url = "https://www.flipkart.com" + product_link.get("href")
    try:
        driver.get(product_url)
        sleep(2)

        details = {}

        # Get product image URL
        image_url_element = driver.find_element(By.XPATH, "//img[@class='DByuf4 IZexXJ jLEJ7H']")
        image_url = image_url_element.get_attribute("src")
        details["image_url"] = image_url if image_url else "Image not available"

        # Get product name
        product_name_element = driver.find_element(By.XPATH, "//span[@class='VU-ZEz']")
        product_name = product_name_element.text
        details["name"] = product_name if product_name else "Name not available"

        # Get product price
        try:
            product_price_element = driver.find_element(By.XPATH, "//div[@class='Nx9bqj CxhGGd']")
            product_price = product_price_element.text
            details["price"] = product_price if product_price else "Price not available"
        except:
            details["price"] = "Price not available"

        exoffers = driver.find_elements(By.XPATH, "//div[@class='BRgXml']")
        unique_exoffers = [exoffer.text.strip() for exoffer in exoffers]
        details["exchange_offer"] = unique_exoffers if unique_exoffers else "Exchange Offer not available"

        # Click on 'Show more' button to reveal more details if available
        try:
            show_more_button = driver.find_element(By.XPATH, "//button[@class='_0+FGxP']")
            show_more_button.click()
            sleep(2)
        except:
            pass

        # Get product offers
        offers = driver.find_elements(By.XPATH, "//li[@class='kF1Ml8 col']")
        unique_offers = [offer.text.strip() for offer in offers]
        details["offers"] = unique_offers if unique_offers else "Offers not available"

        # Get product description
        diss = driver.find_elements(By.XPATH, "//li[@class='_7eSDEz']")
        unique_diss = [dis.text.strip() for dis in diss]
        details["description"] = unique_diss if unique_diss else "Description not available"
        
        # Get current date and time
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        details["DT"] = now

        # Add product details to dictionary
        products[product_name] = details
    except Exception as e:
        print(f"Error processing product: {product_url}, Exception: {e}")

# Write data to CSV file
with open("productsFKE.csv", "w", encoding='utf-8', newline="") as csvfile:
    fieldnames = ["Image", "Name", "Price", "Exchange offer", "Offers", "Description", "Date & Time"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for product_name, details in products.items():
        writer.writerow({
            "Image": details["image_url"],
            "Name": details["name"],
            "Price": details["price"],
            "Exchange offer": ", \n".join(details["exchange_offer"]),
            "Offers": ", \n".join(details["offers"]),
            "Description": ", \n".join(details["description"]),
            "Date & Time": details["DT"],
        })

print("Products saved to productsFK.csv")
driver.quit()
