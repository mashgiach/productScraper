import requests

# Headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Content-Type': 'application/json'
}

def download(url, path):
    try:
        # Send a GET request with custom headers
        response = requests.get(url, headers=headers, stream=True)

        # Check if the request was successful
        if response.status_code == 200:
            # Open the file in binary write mode and save the image
            with open(path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Image downloaded successfully and saved to {path}")
        else:
            print(f"Failed to download image. HTTP Status Code: {response.status_code}")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
    
    return path

