from imagekitio import ImageKit
from config import IMAGEKIT_PRIVATE_KEY, IMAGEKIT_PUBLIC_KEY, IMAGEKIT_URL_ENDPOINT

imageKit = ImageKit(
    private_key=IMAGEKIT_PRIVATE_KEY,
)

def upload_file(file_bytes: bytes, file_name: str, folder: str, content_type: str = "image/jpeg"):
    """Uploads a file to ImageKit and returns the URL of the uploaded file."""
    try: 
        response = imageKit.files.upload(
            file=(file_bytes, file_name, content_type),
            file_name=file_name,
            folder=folder,
            is_private_file=False,
            use_unique_file_name=True
        )
        return response.url
    except Exception as e:
        print(f"Error uploading file: {e}")
        return None
    
def variants(base_url: str)->dict:
    """Returns a dictionary of 3 variant URLs using ImageKit's transformation parameters."""
    return {
        "small": f"{base_url}?tr=w-1280,h-720,c-maintain_ratio,fo-auto",
        "medium": f"{base_url}?tr=w-1080,h-1920,c-maintain_ratio,fo-auto",
        "large": f"{base_url}?tr=w-1080,h-1080,c-maintain_ratio,fo-auto"
    }