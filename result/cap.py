import requests
import os
import time

URL = "https://examweb.ggsipu.ac.in/web/CaptchaServlet"   # your image endpoint
SAVE_DIR = "images"

os.makedirs(SAVE_DIR, exist_ok=True)

session = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "image/*",
    "Referer": "https://example.com"
}

for i in range(1, 501):
    r = session.get(URL, headers=headers, stream=True)

    if r.status_code == 200:
        filename = f"{SAVE_DIR}/img_{i:03}.png"
        with open(filename, "wb") as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)
        print(f"Saved {filename}")
    else:
        print(f"Failed at {i}")

    time.sleep(0.2)  # 🔴 IMPORTANT: avoid blocking
