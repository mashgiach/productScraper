import os
import requests
from requests.auth import HTTPBasicAuth

def create_product(product_info):
    """
    Uploads a new product to WooCommerce using credentials and URL from environment variables.
    
    Expects the following environment variables:
    - WOOCOMMERCE_URL: Base URL of the WooCommerce website
    - WOOCOMMERCE_CONSUMER_KEY: Consumer Key for the WooCommerce API
    - WOOCOMMERCE_CONSUMER_SECRET: Consumer Secret for the WooCommerce API

    Parameters:
    - product_info (dict): Dictionary containing fully-formed product data to be uploaded.
    """
    # Retrieve environment variables
    url = os.getenv('URL')
    consumer_key = os.getenv('CONSUMER_KEY')
    consumer_secret = os.getenv('CONSUMER_SECRET')

    # Check if any credentials or URL are missing
    if not all([url, consumer_key, consumer_secret]):
        raise ValueError("Missing required environment variables: "
                         "WOOCOMMERCE_URL, WOOCOMMERCE_CONSUMER_KEY, or WOOCOMMERCE_CONSUMER_SECRET.")

    # Set the full API endpoint for products
    endpoint = f"{url.rstrip('/')}/wp-json/wc/v3/products"

    # Make the POST request with authentication
    response = requests.post(
        endpoint,
        auth=HTTPBasicAuth(consumer_key, consumer_secret),
        json=product_info  # Directly use the passed-in product data
    )

    # Check for a successful response
    if response.status_code == 201:
        print("Product created successfully!")
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None
