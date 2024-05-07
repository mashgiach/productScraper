import requests
import os

USER = os.getenv('USER')
APPLICATION_PASSWORD = os.getenv('APPLICATION_PASSWORD')
URL = os.getenv('URL')

def upload_image(photo_data):
    print(photo_data)
    photo_data = {'file': open(f'{photo_data}', 'rb')}
    response = requests.post(url=f'{URL}/wp-json/wp/v2/media',
                             auth=(USER, APPLICATION_PASSWORD),
                             files=photo_data)
    response_json = response.json()
    photo_url = response_json.get('source_url', 'URL not found')
    print(photo_url)
    return photo_url

# upload_image('./images/ערכת-יצירה-גן-פיות-בקופסה_0.jpg')