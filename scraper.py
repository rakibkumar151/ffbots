import requests
import json
import os
import re

def scrape_emotes():
    print("Starting scraper...")
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    })
    
    # Try to access the dashboard or login page
    res = session.get("https://ffemote.com/")
    print(f"Init GET status: {res.status_code}")
    
    # Let's try to post login if there's a login form. Often it's simple POST
    login_data = {"username": "B25", "password": "B25"}
    
    # Post to /login or /api/login
    res = session.post("https://ffemote.com/login.php", data=login_data)
    if res.status_code == 404:
        res = session.post("https://ffemote.com/login", data=login_data)
    
    # Access dashboard
    res = session.get("https://ffemote.com/dashboard.php")
    if res.status_code == 404:
        res = session.get("https://ffemote.com/index.php")
    if res.status_code == 404:
        res = session.get("https://ffemote.com/")
        
    html = res.text
    print(f"Fetched HTML size: {len(html)}")
    
    # Find image paths
    # usually <img src="images/emotes/909000063.png">
    img_urls = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
    print(f"Found {len(img_urls)} image tags.")
    
    emotes_dir = "frontend/public/emotes"
    os.makedirs(emotes_dir, exist_ok=True)
    
    downloaded = 0
    for img_url in set(img_urls):
        if "9090" in img_url:
            if not img_url.startswith("http"):
                full_url = "https://ffemote.com/" + img_url.lstrip('/')
            else:
                full_url = img_url
            
            # Extract ID
            match = re.search(r'(9090\d+)', full_url)
            if match:
                eid = match.group(1)
                try:
                    img_res = session.get(full_url, stream=True)
                    if img_res.status_code == 200:
                        with open(f"{emotes_dir}/{eid}.png", 'wb') as f:
                            for chunk in img_res.iter_content(1024):
                                f.write(chunk)
                        downloaded += 1
                except Exception as e:
                    pass

    print(f"Successfully downloaded {downloaded} emotes to frontend/public/emotes/")

if __name__ == "__main__":
    scrape_emotes()
