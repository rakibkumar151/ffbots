
import asyncio
import aiohttp
import json
import os
import sys

# Add backend to path
sys.path.append(os.path.abspath("backend"))

from main import GetPlayerInfo, get_connector, get_random_proxy, encrypted_proto
from xDL import GenPlayerInfoPacket, DecodePlayerInfo, DEc_AEs

async def test_single_info(target_uid):
    print(f"[*] Testing info for UID: {target_uid}")
    
    from main import GeNeRaTeAccEss, AuToUpDaTE, EncRypTMajoRLoGin, MajorLogin, Uaa, load_all_credentials
    
    accounts = load_all_credentials()
    if not accounts:
        print("[!] No bot accounts found!")
        return

    for bot_uid, bot_pwd in accounts:
        print(f"[*] Attempting with bot {bot_uid}...")
        try:
            open_id, access_token = await GeNeRaTeAccEss(bot_uid, bot_pwd)
            if not open_id: continue
                
            login_url, ob, version = await AuToUpDaTE()
            Hr = {'User-Agent': Uaa(), 'Connection': "Keep-Alive", 'Accept-Encoding': "gzip",
                  'Content-Type': "application/x-www-form-urlencoded", 'X-Unity-Version': "2018.4.11f1",
                  'X-GA': "v1 1", 'ReleaseVersion': ob}
            payload = await EncRypTMajoRLoGin(open_id, access_token, version)
            
            login_resp = await MajorLogin(login_url, payload, Hr)
            if not login_resp: continue
                
            from Pb2 import MajoRLoGinrEs_pb2
            auth = MajoRLoGinrEs_pb2.MajorLoginRes()
            auth.ParseFromString(login_resp)
            
            from main import GetLoginData
            # Prepare payload for GetLoginData
            login_data_payload = await EncRypTMajoRLoGin(open_id, access_token, version)
            login_data_resp = await GetLoginData(auth.url, login_data_payload, auth.token, Hr)
            
            if not login_data_resp:
                print(f"[!] GetLoginData failed for bot {bot_uid}")
                continue
                
            print(f"[OK] Session fully established for bot {bot_uid}")
            
            info = await GetPlayerInfo(auth.url, target_uid, auth.token, Hr)
            
            # Simulate Full Profile Logic from main.py
            try:
                import sys, os
                scraper_dir = os.path.join(os.getcwd(), "..", "New folder")
                if scraper_dir not in sys.path: sys.path.append(scraper_dir)
                from ff_info_api import get_player_info_from_site
                scraped = get_player_info_from_site(target_uid)
                if scraped and scraped.get('account'):
                    acc = scraped['account']
                    def find_val(label): return next((x.split(':', 1)[1].strip() for x in acc if label in x), "N/A")
                    
                    if not info: info = {}
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
            except Exception as e:
                print(f"[!] Scraper Error: {e}")

            if info:
                print(f"\n[PLAYER FULL PROFILE: {target_uid}]")
                print("--------------------")
                print(f"Name: {info.get('name', 'N/A')}")
                print(f"UID: {target_uid}")
                print(f"Level: {info.get('level', 'N/A')} [Exp: {info.get('exp', 'N/A')}]")
                print(f"Likes: {info.get('likes', 'N/A')}")
                print(f"Honor Score: {info.get('honor', 'N/A')}")
                print(f"BR Rank: {info.get('br_rank', 'N/A')} ({info.get('br_points', 'N/A')})")
                print(f"CS Points: {info.get('cs_points', 'N/A')}")
                print(f"Created: {info.get('created', 'N/A')}")
                print(f"Last Login: {info.get('last_login', 'N/A')}")
                print(f"BP Level: {info.get('bp_level', 'N/A')} ({info.get('bp_status', 'N/A')})")
                print(f"Language: {info.get('lang', 'N/A')}")
                print(f"Bio: {info.get('bio', 'N/A')}")
                print("--------------------")
                return 
            else:
                print(f"[!] Info fetch failed for this bot, trying next...")
                
        except Exception as e:
            print(f"[!] Error with bot {bot_uid}: {e}")
            continue
    
    print("\n[!] All bots failed to fetch info. This is likely a proxy or IP block issue.")

if __name__ == "__main__":
    asyncio.run(test_single_info("3043982550"))

if __name__ == "__main__":
    asyncio.run(test_single_info("2545042710"))
