# Web Scraper for Product Creation

## Overview
This Python script extracts product data from a website, processes it, and uploads it to an e-commerce platform.

## How It Works
1. **CSV Input**: Extracts basic product information from `products.csv` based on the given index.
2. **Web Scraping**: Uses `BeautifulSoup` and `requests` to collect detailed product data (title, description, price, images) from a product webpage.
3. **Image Processing**:
   - Downloads images with a custom `download` function.
   - Uploads images using the `upload_image` function.
4. **Product Creation**:
   - Assembles the data into a structured product object.
   - Calls `create_product` to upload this data to the e-commerce platform.

## Requirements
- **External Libraries**: `BeautifulSoup`, `pandas`, `requests`
- **Custom Modules**: `download`, `upload`, `product`
