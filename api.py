
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import os
import sys

# Add current dir to path to import main and xDL
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import GetPlayerInfo, load_all_credentials, GeNeRaTeAccEss, AuToUpDaTE, EncRypTMajoRLoGin, MajorLogin, Uaa, GetLoginData
from Pb2 import MajoRLoGinrEs_pb2

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/info/{uid}")
async def get_uid_info(uid: str):
    accounts = load_all_credentials()
    if not accounts:
        raise HTTPException(status_code=500, detail="No bot accounts available")

    # Try each bot
    for bot_uid, bot_pwd in accounts:
        try:
            open_id, access_token = await GeNeRaTeAccEss(bot_uid, bot_pwd)
            if not open_id: continue
            
            login_url, ob, version = await AuToUpDaTE()
            Hr = {'User-Agent': Uaa(), 'Connection': "Keep-Alive", 'Accept-Encoding': "gzip",
                  'Content-Type': "application/x-form-urlencoded", 'X-Unity-Version': "2018.4.11f1",
                  'X-GA': "v1 1", 'ReleaseVersion': ob}
            payload = await EncRypTMajoRLoGin(open_id, access_token, version)
            
            login_resp = await MajorLogin(login_url, payload, Hr)
            if not login_resp: continue
            
            auth = MajoRLoGinrEs_pb2.MajorLoginRes()
            auth.ParseFromString(login_resp)
            
            # Establish session
            login_data_payload = await EncRypTMajoRLoGin(open_id, access_token, version)
            await GetLoginData(auth.url, login_data_payload, auth.token, Hr)
            
            # Fetch Info
            info = await GetPlayerInfo(auth.url, uid, auth.token, Hr)
            
            if info:
                # Add extra fields from scraper
                try:
                    scraper_dir = os.path.join(os.getcwd(), "..", "New folder")
                    if scraper_dir not in sys.path: sys.path.append(scraper_dir)
                    from ff_info_api import get_player_info_from_site
                    scraped = get_player_info_from_site(uid)
                    if scraped and scraped.get('account'):
                        acc = scraped['account']
                        def find_val(label): return next((x.split(':', 1)[1].strip() for x in acc if label in x), "N/A")
                        info.update({
                            'honor': find_val('Honor Score'),
                            'br_rank': find_val('Current BR Rank'),
                            'br_points': find_val('BR Rank Point'),
                            'cs_points': find_val('CS Rank Point'),
                            'created': find_val('Account Created On'),
                            'last_login': find_val('Last Login'),
                            'bio': find_val('Bio'),
                            'bp_level': find_val('Booyah Pass Level'),
                            'bp_status': find_val('Booyah Pass Premium'),
                            'lang': find_val('Language')
                        })
                except: pass
                
                return info
        except Exception as e:
            print(f"Bot {bot_uid} failed: {e}")
            continue

    raise HTTPException(status_code=404, detail="UID not found or service unavailable")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
