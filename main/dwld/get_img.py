import requests
from PIL import Image
from io import BytesIO #pip install requests pillow

def download_image(url, path_to_save):
    # Send a HTTP request to the URL of the image
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Get the content of the response
        image_data = response.content

        # Open the image
        image = Image.open(BytesIO(image_data))

        # Save the image
        image.save(path_to_save)
        print(f"Image downloaded successfully and saved at: {path_to_save}")
    else:
        print(f"Unable to download image. HTTP response code: {response.status_code}")

