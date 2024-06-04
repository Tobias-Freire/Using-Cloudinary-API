import cloudinary
import cloudinary.uploader
import cloudinary.api
import requests

# Configuração
cloudinary.config( 
    cloud_name = "YOUR CLOUD NAME", 
    api_key = "YOUR API KEY", 
    api_secret = "YOUR API SECRET", 
    secure=True
)

# Ask the user the path to the image and the path to store the download
path = str(input('Type the path to the image: '))
save_path = str(input('Type the desired path to store the download (including the desired name of the archive and extension .png): '))

# Upload the image and remove the background using Cloudinary AI
response = cloudinary.uploader.upload(f"{path}", background_removal="cloudinary_ai", format="png")
print("No background image url:", response['secure_url'], "\n")

# Function wich automatically downloads the image with no background
def download_image(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as archive:
            for chunk in response:
                archive.write(chunk)
    else:
        print('Error!\nStatus code: ', response.status_code)

download_image(response['secure_url'], save_path)
