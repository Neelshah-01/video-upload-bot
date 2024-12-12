# Socialverse Video Upload and Post Creation

This project demonstrates the process of uploading a video to Socialverse (Empow"erverse) and creating a post linked to the uploaded video using the Socialverse API.

---

## Requirements

### 1. Libraries and Tools
- **Python 3.x**
- Required Python libraries (install via `pip`):
  - `requests`
  - `python-dotenv`

### 2. Environment Variables
Create a `.env` file in the project directory with the following variables:

| Variable          | Description                                                     |
|-------------------|-----------------------------------------------------------------|
| `FLIC_TOKEN`      | Your unique Socialverse API token for authentication.           |
| `VIDEO_FILE_PATH` | Full path to the video file you wish to upload.                 |
| `TITLE`           | Title of the post to be created.                                |
| `CATEGORY_ID`     | ID of the category under which the post will be created.        |
| `IS_PUBLIC`       | Whether the post should be publicly available (`true` or `false`). |

Example `.env` file:
```env
FLIC_TOKEN=your_flic_token_here
VIDEO_FILE_PATH="/path/to/your/video.mp4"
TITLE="Sample Title"
CATEGORY_ID=25
IS_PUBLIC=False
```

## How to get FLIC_TOKEN?

#### Enter `https://api.socialverseapp.com/user/token?username=<your_username>&password=<your_password>` in your browser after replacing <your_username> with your empowerverse username and <your_password> with your empowerverse password.

## Installation
### 1. Clone this repository to your local machine.
Using Git Bash in your project directory, enter command:

```
git clone https://github.com/Neelshah-01/video-upload-bot.git
```

### 2. Create a virtual environment (optional but good practice)

```
python -m venv <env_name>
```

### 3. Install the required libraries using requirements.txt
```
pip install -r requirements.txt
```

## Usage

### Run the main.py file
```
python main.py
```

# Output
### If successful, the script will output:

- Confirmation of the video upload.
- Confirmation of the post creation with details from the API, e.g.:
```
  {
    'message': 'Post was created! :D',
    'identifier': 'ABCD34-',
    'slug': '<a-very-big-value-here>',
    'status': 'success'
  }
```
### If any step fails, the script will raise an error with the relevant details. e.g.:

```
Error: Failed to create post: 404 {"status":"error","message":"Category not found"}
```