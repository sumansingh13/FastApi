from dotenv import load_dotenv
from imagekitio import ImageKit
import os

load_dotenv()

imagekit = ImageKit(
    private_key=os.getenv("imagekit_Private_key"),
)

URL_ENDPOINT = os.getenv("imagekit_Url_endpoint")