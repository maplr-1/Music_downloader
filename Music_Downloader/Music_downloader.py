import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
webpage_url = input("Enter the page URL: ").strip()
save_location = input("Enter the folder to save MP3s: ").strip()
os.makedirs(save_location, exist_ok=True)
response = requests.get(webpage_url)
response.raise_for_status()
soup = BeautifulSoup(response.content, "html.parser")
a_tags = soup.find_all("a")
for tag in a_tags:
    href = tag.get("href")
    if href and href.endswith(".mp3"):
        if response.status_code == 404:
            print("Link's Wrong, .mp3 not found!")
        mp3_url = urljoin(webpage_url, href)
        filename = os.path.join(save_location, mp3_url.split("/")[-1])
        print(f"Downloading: {mp3_url}")
        with requests.get(mp3_url, stream=True) as r:
            with open(filename, "wb") as f:
                for chunk in r.iter_content(8192):
                    f.write(chunk)
        print(f"Saved: {filename}")
