# Music Downloader

## About
This project is a **Python-based music downloader**.  
It allows you to provide:
1. A website URL that contains multiple `.mp3` files.  
2. A destination folder on your system.  

The program will then scan the website, find all the available `.mp3` files, and download them into the selected folder.  

###  Features
- Accepts a website URL containing `.mp3` files.
- Lets you specify where to save the downloaded files.
- Automatically downloads **all available `.mp3` files** from the site.
- Lightweight and beginner-friendly.
- Great for learning about **web scraping** and **file handling** in Python.

This project was created for **educational purposes** but can also be used for **personal music archiving**.

---

##  Requirements
- Python **3.7+**
- Libraries:
  - `requests` – for making HTTP requests
  - `beautifulsoup4` – for parsing the website and finding `.mp3` links
  - `os` (built-in) – for managing file paths
  - `urllib` (built-in) – for downloading files

Install dependencies with:
```bash
pip install requests beautifulsoup4
