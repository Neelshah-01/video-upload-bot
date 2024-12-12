import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
FLIC_TOKEN = os.getenv("FLIC_TOKEN")
VIDEO_FILE_PATH = os.getenv("VIDEO_FILE_PATH")
TITLE = os.getenv("TITLE")
CATEGORY_ID = os.getenv("CATEGORY_ID")
IS_PUBLIC = os.getenv("IS_PUBLIC")

# Validate environment variables
if not all([FLIC_TOKEN, VIDEO_FILE_PATH, TITLE, CATEGORY_ID, IS_PUBLIC]):
    raise ValueError("Missing required environment variables. Ensure all are set in the .env file.")

# Step 1: Generate Upload URL
def generate_upload_url():
    url = "https://api.socialverseapp.com/posts/generate-upload-url"
    headers = {"Flic-Token": FLIC_TOKEN}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data["url"], data["hash"]
    else:
        raise Exception(f"Failed to generate upload URL: {response.status_code} {response.text}")

# Step 2: Upload Video
def upload_video(upload_url):
    with open(VIDEO_FILE_PATH, "rb") as video_file:
        headers = {"Content-Type": "video/mp4"}
        response = requests.put(upload_url, headers=headers, data=video_file)

    if response.status_code == 200:
        print("Video uploaded successfully.")
    else:
        raise Exception(f"Video upload failed: {response.status_code} {response.text}")

# Step 3: Create Post
def create_post(video_hash):
    url = "https://api.socialverseapp.com/posts"
    headers = {
        "Flic-Token": FLIC_TOKEN,
        "Content-Type": "application/json",
    }
    payload = {
        "title": TITLE,
        "hash": video_hash,
        "category_id": CATEGORY_ID,
        "is_available_in_public_feed": IS_PUBLIC.lower() == "true",
    }
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print("Post created successfully.")
        print("Response:", response.json())
    else:
        raise Exception(f"Failed to create post: {response.status_code} {response.text}")

def main():
    try:
        print("Generating upload URL...")
        upload_url, video_hash  = generate_upload_url()

        print("Uploading video...")
        upload_video(upload_url)

        print("Creating post...")
        create_post(video_hash)

        print("All steps completed successfully.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
