# PixelHarvester

PixelHarvester is a personal desktop live wallpaper utility for discovering, downloading, organizing, and rotating public community media as local wallpapers.

The app is designed for low-volume personal use. It helps users collect suitable images, GIFs, and videos from selected public communities, then organizes them by media type and aspect ratio for wallpaper use.

## Planned features

- Desktop GUI for selecting communities and scan options
- Reddit API integration through PRAW
- Minimum score filtering
- Sort modes such as hot, new, top, rising, and controversial
- Media organization by type:
  - image
  - gif
  - video
- Media organization by aspect ratio:
  - portrait
  - landscape
  - square
  - unknown
- Duplicate tracking with SQLite
- Conservative request throttling and local caching
- Optional live wallpaper rotation support

## What the app does on Reddit

PixelHarvester reads publicly available posts from user-selected communities through Reddit's API. It does not post, comment, vote, message users, moderate communities, or collect private user data.

The application only downloads public media selected by user-defined filters and stores it locally on the user's device for personal wallpaper use.

## Status

Early development.

## Local development

```powershell
python -m venv .venv
.\\.venv\\Scripts\\python.exe -m pip install -r requirements.txt
.\\.venv\\Scripts\\python.exe src\\pixelharvester_app.py
```

## Configuration

Create a local `reddit_config.json` file from `reddit_config.example.json` and add your own Reddit API credentials.

Do not commit real credentials.
