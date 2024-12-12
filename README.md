# Socialverse Video Upload and Post Creation

This project demonstrates the process of uploading a video to Socialverse and creating a post linked to the uploaded video using the Socialverse API.

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
CATEGORY_ID=1
IS_PUBLIC=False

