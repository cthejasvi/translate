# LibreTranslate Web App

This is a simple web application built with Flask that consumes the LibreTranslate API to translate text between languages. It supports auto-detection of source language and stores translation history in an SQLite database.

## Features

- Translate text using the LibreTranslate API
- Auto-detect source language
- Store translation history in SQLite
- Display the last 5 translations

## Project Structure

```
project/
├── main.py
├── libretranslate_api.py
├── db.py
├── translations.db
└── templates/
    └── index.html
```

## Setup Instructions

1. Install dependencies:

```
pip install flask requests
```

2. Start the LibreTranslate server (local/self-hosted):

```
libretranslate
```

3. Run the Flask app:

```
python main.py
```

Visit: `http://127.0.0.1:5001`

## File Descriptions

- `main.py`: Handles routing and integration
- `libretranslate_api.py`: Handles API calls to LibreTranslate
- `db.py`: Manages SQLite database and translation history
- `index.html`: Frontend interface

