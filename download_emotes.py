import requests
import json
import os
from concurrent.futures import ThreadPoolExecutor

def download_emotes():
    # Load emotes.json
    try:
        with open('emotes.json', 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error loading emotes.json: {e}")
        return

    # Extract all unique emote IDs
    emote_ids = set()
    numbers = data.get("EMOTES", {}).get("numbers", {})
    names = data.get("EMOTES", {}).get("names", {})
    
    for eid in numbers.values():
        emote_ids.add(str(eid))
    for eid in names.values():
        emote_ids.add(str(eid))

    # Output directory
    out_dir = "frontend/public/emotes"
    os.makedirs(out_dir, exist_ok=True)
    
    base_url = "https://cdn.jsdelivr.net/gh/ShahGCreator/icon@main/PNG/{}.png"

    def download_image(eid):
        file_path = f"{out_dir}/{eid}.png"
        if os.path.exists(file_path):
            return "Exists"
        
        try:
            res = requests.get(base_url.format(eid), timeout=10)
            if res.status_code == 200:
                with open(file_path, "wb") as f:
                    f.write(res.content)
                return "Downloaded"
        except:
            pass
        return "Failed"

    print(f"Downloading {len(emote_ids)} emotes...")
    downloaded = 0
    with ThreadPoolExecutor(max_workers=20) as executor:
        results = executor.map(download_image, emote_ids)
        for r in results:
            if r == "Downloaded":
                downloaded += 1

    print(f"✅ Downloaded {downloaded} new emotes to frontend/public/emotes/")

if __name__ == "__main__":
    download_emotes()
