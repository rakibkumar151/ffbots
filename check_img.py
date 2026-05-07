import requests

urls = [
    "https://ffemote.com/img/{}.png",
    "https://ffemote.com/images/{}.png",
    "https://ffemote.com/assets/{}.png",
    "https://ffemote.com/assets/images/{}.png",
    "https://ffemote.com/emotes/{}.png",
    "https://ffemote.com/images/emotes/{}.png",
    "https://ffemote.com/assets/emotes/{}.png"
]

emote_id = "909000063"

for url in urls:
    try:
        r = requests.head(url.format(emote_id), timeout=3)
        if r.status_code == 200:
            print(f"Found: {url}")
            break
        print(f"Failed: {url} ({r.status_code})")
    except:
        pass
