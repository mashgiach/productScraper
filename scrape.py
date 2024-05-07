from bs4 import BeautifulSoup
import pandas as pd
import os
import requests
from download import download
from upload import upload_image
from product import create_product
import time


def scrape(index, type):
    df = pd.read_csv('./products.csv')
    df.columns = df.columns.str.strip()

    product_info = {
        "name": df.loc[index, 'txt_title'].strip(),
        "category": df.loc[index, 'catalog_num'],
        "id": df.loc[index, 'cs']
    }

    base_url = 'http://www.magickingdom.co.il/'
    product_slug = product_info['name'].replace(" ", "-")
    product_url = f"{base_url}{product_slug}"

    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    response = None
    # Fetch product page
    if type=="normal":
        response = requests.get(product_url, headers=headers)
    # print(f"{base_url}index.php?dir=site&page=catalog&op=item&cs={product_info['id']}")
    elif type=="special":
        response = requests.get(
            f"{base_url}index.php?dir=site&page=catalog&op=item&cs={product_info['id']}",
            headers=headers
        )
    

    soup = BeautifulSoup(response.content, 'html.parser')
    description_div = soup.find('div', class_='product-item-description__text')

    product_info.update({
        "title": soup.find(class_='catalog-title').text.strip(),
        "description": ' '.join(p.get_text(strip=True) for p in description_div.find_all('p')),
        "price": soup.find('div', class_='price__new').text.strip(),
        "images": [img['src'] for img in soup.select('a.prod-gallery__img-big img')]
    })

    images_path = "./images/"
    os.makedirs(images_path, exist_ok=True)

    for i, img_url in enumerate(product_info['images']):
        local_path = download(f"{base_url}{img_url}", f"{images_path}{product_slug}_{i}.jpg")
        time.sleep(0.2)
        new_path = upload_image(local_path)

        product_info['images'][i] = new_path  # Use local path for demo; in practice, use URL of uploaded image


    product_data = {
        "name": product_info['title'],
        "type": "simple",
        "regular_price": product_info['price'].replace(',', '').replace('₪', '').replace(' ', ''),
        "description": product_info['description'],
        "categories": [{"id": product_info['category']}],
        "images": [{"src": img} for img in product_info['images']]
    }

    print(product_data) # For debugging
    create_product(product_data)