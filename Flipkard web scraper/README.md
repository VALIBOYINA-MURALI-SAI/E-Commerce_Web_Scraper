# Flipkart Product Scraper

This project is a web scraper designed to extract product details from the Flipkart website. The scraper uses Selenium to automate web interactions, BeautifulSoup to parse HTML content, and saves the collected data into a CSV file.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction
Flipkart Product Scraper allows users to extract detailed information about products listed on the Flipkart website. The information includes product names, prices, exchange offers, special offers, descriptions, and the date and time of extraction.

## Features
- **Search for Products**: Users can input a product name to search for relevant products.
- **Extract Product Details**: Scrapes product images, names, prices, exchange offers, special offers, and descriptions.
- **Save to CSV**: Saves the extracted data into a CSV file for easy access and analysis.

## Installation
To set up the Flipkart Product Scraper, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/MURALISAIVALIBOINA/flipkart-product-scraper.git
   cd flipkart-product-scraper
   ```

2. Install the required dependencies:
   ```bash
   pip install selenium beautifulsoup4
   ```

3. Download the appropriate ChromeDriver version for your version of Chrome and ensure it is accessible in your PATH or in the project directory.

## Usage
1. Run the script:
   ```bash
   python main.py
   ```

2. Enter the product name when prompted.

3. The script will open the Flipkart website, search for the product, and extract details for each listing.

4. The extracted data will be saved in a CSV file named `productsFKE.csv` in the project directory.

## Requirements
- **Python 3.x**
- **Google Chrome**: Ensure that you have the latest version of Google Chrome installed.
- **ChromeDriver**: Download the version of ChromeDriver that matches your installed version of Chrome. [Download ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- **Hardware**:
  - **CPU**: Intel i5 or higher
  - **RAM**: 4GB or more
  - **Storage**: At least 500MB free space for storing data and dependencies

## Technologies Used
- **Selenium**: For automating web browser interaction.
- **BeautifulSoup**: For parsing HTML and extracting information.
- **Python CSV**: For writing data to a CSV file.

## Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/tebeka/selenium/blob/master/LICENSE) file for details.

## Acknowledgements
- Inspired by various web scraping projects and tutorials.
- Special thanks to the developers of Selenium, BeautifulSoup, and other libraries used in this project.