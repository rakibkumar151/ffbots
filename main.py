# TELEGRAM : @lsahilxx
import requests, os, json, binascii, time, urllib3, base64, datetime, re, socket, ssl, asyncio, aiohttp, random, traceback
from protobuf_decoder.protobuf_decoder import Parser
from xDL import *
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from Pb2 import DEcwHisPErMsG_pb2, MajoRLoGinrEs_pb2, PorTs_pb2, MajoRLoGinrEq_pb2
import google.protobuf.json_format as json_format
from keep_alive import keep_alive

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Load emotes globally
def load_emotes_from_json():
    emotes_file = "emotes.json"
    try:
        if not os.path.exists(emotes_file): return {"numbers": {}, "names": {}}
        with open(emotes_file, 'r') as f:
            data = json.load(f)
        return {"numbers": data.get("EMOTES", {}).get("numbers", {}), "names": data.get("EMOTES", {}).get("names", {})}
    except: return {"numbers": {}, "names": {}}

def load_all_credentials():
    filename = "bot.txt"
    accounts = []
    try:
        if not os.path.exists(filename): return []
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line: continue
                try:
                    data = json.loads(line)
                    for uid, password in data.items():
                        accounts.append((uid, password))
                except: continue
        return accounts
    except: return []

EMOTES_DATA = load_emotes_from_json()
NUMBER_EMOTES = EMOTES_DATA["numbers"]
NAME_EMOTES = EMOTES_DATA["names"]

def get_random_color(): return "[00FF00]" # Fallback color

# --- PROXY & DNS CONFIGURATION ---
def get_random_proxy():
    proxy_host = "change4.owlproxy.com"
    proxy_port = "7778"
    proxy_pass = "2933445"
    random_sid = random.randint(10000000, 99999999)
    proxy_user = f"hr6ckDl06980_custom_zone_BR_st__city_sid_{random_sid}_time_5"
    return f"http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}"

def get_connector():
    # Simplified connector to allow OS to handle DNS resolution naturally
    return aiohttp.TCPConnector(ssl=False)

# --- GLOBAL CONFIG ---
LEVEL_UP = "NIKI BOT"
start_spam_duration = 18
wait_after_match = 5
start_spam_delay = 0.1
region = 'IN'
ACTIVE_BOTS = []
# Load credentials from environment variables for production (e.g., Vercel/Render)
ADMIN_USER = os.environ.get("ADMIN_USER", "admin")
ADMIN_PASS = os.environ.get("ADMIN_PASS", "NIKI-BOT-2026")

def check_auth(request):
    auth_header = request.headers.get('Authorization')
    # Using simple Bearer token for API authentication
    if not auth_header or auth_header != f"Bearer {ADMIN_PASS}":
        return False
    return True

async def AuToUpDaTE():
    while True:
        try:
            proxy = get_random_proxy()
            from google_play_scraper import app
            # Scraping Play Store through proxy
            result = app('com.dts.freefireth', lang="fr", country='fr')
            version = result['version']
            return "https://loginbp.ggblueshark.com/", "OB53", version
        except Exception as e:
            print(f"Update Check Retry (Proxy: {e})")
            await asyncio.sleep(2)

async def GeNeRaTeAccEss(uid, password):
    while True:
        try:
            proxy = get_random_proxy()
            url = "https://100067.connect.garena.com/oauth/guest/token/grant"
            headers = {"Host": "100067.connect.garena.com", "User-Agent": await Ua(), "Content-Type": "application/x-www-form-urlencoded", "Connection": "close"}
            data = {"uid": uid, "password": password, "response_type": "token", "client_type": "2", "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3", "client_id": "100067"}
            
            async with aiohttp.ClientSession(connector=get_connector()) as session:
                async with session.post(url, headers=headers, data=data, proxy=proxy, timeout=15) as response:
                    if response.status == 200:
                        data = await response.json()
                        return data.get("open_id"), data.get("access_token")
                    print(f"Access Failed ({response.status}), retrying...")
        except Exception as e:
            print(f"Retrying Access via Proxy... {e}")
        await asyncio.sleep(2)

async def encrypted_proto(encoded_hex):
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
    key = b'Yg&tc%DEuh6%Zc^8'; iv = b'6oyZDr22E3ychjM%'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(pad(encoded_hex, AES.block_size))

async def EncRypTMajoRLoGin(open_id, access_token, version):
    major_login = MajoRLoGinrEq_pb2.MajorLogin()
    major_login.event_time = str(datetime.now())[:-7]
    major_login.game_name = "free fire"; major_login.platform_id = 1; major_login.client_version = version
    major_login.system_software = "Android OS 9 / API-28 (PQ3B.190801.10101846/G9650ZHU2ARC6)"
    major_login.system_hardware = "Handheld"; major_login.telecom_operator = "Verizon"; major_login.network_type = "WIFI"
    major_login.screen_width = 1920; major_login.screen_height = 1080; major_login.screen_dpi = "280"
    major_login.processor_details = "ARM64 FP ASIMD AES VMH | 2865 | 4"; major_login.memory = 3003
    major_login.gpu_renderer = "Adreno (TM) 640"; major_login.gpu_version = "OpenGL ES 3.1 v1.46"
    major_login.unique_device_id = "Google|34a7dcdf-a7d5-4cb6-8d7e-3b0e448a0c57"
    major_login.client_ip = "223.191.51.89"; major_login.language = "en"; major_login.open_id = open_id
    major_login.open_id_type = "4"; major_login.device_type = "Handheld"
    major_login.access_token = access_token; major_login.platform_sdk_id = 1; major_login.network_operator_a = "Verizon"
    major_login.network_type_a = "WIFI"; major_login.client_using_version = "7428b253defc164018c604a1ebbfebdf"
    major_login.external_storage_total = 36235; major_login.external_storage_available = 31335
    major_login.internal_storage_total = 2519; major_login.internal_storage_available = 703
    major_login.game_disk_storage_available = 25010; major_login.game_disk_storage_total = 26628
    major_login.external_sdcard_avail_storage = 32992; major_login.external_sdcard_total_storage = 36235
    major_login.login_by = 3; major_login.library_path = "/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/lib/arm64"
    major_login.reg_avatar = 1; major_login.library_token = "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/base.apk"
    major_login.channel_type = 3; major_login.cpu_type = 2; major_login.cpu_architecture = "64"
    major_login.client_version_code = "2019118695"; major_login.graphics_api = "OpenGLES2"; major_login.supported_astc_bitset = 16383
    major_login.login_open_id_type = 4; major_login.loading_time = 13564; major_login.release_channel = "android"
    major_login.android_engine_init_flag = 110009; major_login.if_push = 1; major_login.is_vpn = 1
    major_login.origin_platform_type = "4"; major_login.primary_platform_type = "4"
    string = major_login.SerializeToString()
    return await encrypted_proto(string)

async def MajorLogin(url, payload, Hr):
    while True:
        try:
            proxy = get_random_proxy()
            async with aiohttp.ClientSession(connector=get_connector()) as session:
                async with session.post(f"{url}MajorLogin", data=payload, headers=Hr, proxy=proxy, timeout=15) as response:
                    if response.status == 200: return await response.read()
                    print(f"MajorLogin Status: {response.status}, retrying...")
        except Exception as e:
            print(f"Retrying MajorLogin via Proxy... {e}")
        await asyncio.sleep(2)

async def GetLoginData(base_url, payload, token, Hr):
    while True:
        try:
            proxy = get_random_proxy()
            url = f"{base_url}/GetLoginData"
            Hr['Authorization'] = f"Bearer {token}"
            async with aiohttp.ClientSession(connector=get_connector()) as session:
                async with session.post(url, data=payload, headers=Hr, proxy=proxy, timeout=15) as response:
                    if response.status == 200: return await response.read()
                    print(f"GetLoginData Status: {response.status}, retrying...")
        except Exception as e:
            print(f"Retrying GetLoginData via Proxy... {e}")
        await asyncio.sleep(2)

async def SEndPacKeT(ChaT, OnLinE, TypE, PacKeT):
    if TypE == 'ChaT':
        if not ChaT: raise Exception("Chat server disconnected")
        ChaT.write(PacKeT); await ChaT.drain()
    elif TypE == 'OnLine':
        if not OnLinE: raise Exception("Online server disconnected")
        OnLinE.write(PacKeT); await OnLinE.drain()

async def xAuThSTarTuP(TarGeT, token, timestamp, key, iv):
    uid_hex = hex(TarGeT)[2:]; uid_length = len(uid_hex); encrypted_timestamp = await DecodE_HeX(timestamp)
    encrypted_account_token = token.encode().hex(); encrypted_packet = await EnC_PacKeT(encrypted_account_token, key, iv)
    encrypted_packet_length = hex(len(encrypted_packet) // 2)[2:]
    headers = '0000000' if uid_length == 9 else '00000000' if uid_length == 8 else '000000' if uid_length == 10 else '000000000' if uid_length == 7 else '0000000'
    return f"0115{headers}{uid_hex}{encrypted_timestamp}00000{encrypted_packet_length}{encrypted_packet}"

# --- BOT COMMANDS ---
async def join_teamcode_packet(team_code, key, iv, region):
    fields = {1: 4, 2: {4: bytes.fromhex("01090a0b121920"), 5: str(team_code), 6: 6, 8: 1, 9: {2: 800, 6: 11, 8: "1.111.1", 9: 5, 10: 1}}}
    packet_type = '0514' if region.lower() == "ind" else "0519" if region.lower() == "bd" else "0515"
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)

async def start_auto_packet(key, iv, region):
    fields = {1: 9, 2: {1: 12480598706}}
    packet_type = '0514' if region.lower() == "ind" else "0519" if region.lower() == "bd" else "0515"
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)

async def leave_squad_packet(key, iv, region):
    fields = {1: 7, 2: {1: 12480598706}}
    packet_type = '0514' if region.lower() == "ind" else "0519" if region.lower() == "bd" else "0515"
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)

async def auto_start_loop(team_code, uid, chat_id, chat_type, key, iv, region, state, bot_state):
    while not state['stop_auto']:
        try:
            join_pkt = await join_teamcode_packet(team_code, key, iv, region)
            await SEndPacKeT(bot_state['whisper_writer'], bot_state['online_writer'], 'OnLine', join_pkt)
            await asyncio.sleep(2)
            start_pkt = await start_auto_packet(key, iv, region)
            end_time = time.time() + start_spam_duration
            while time.time() < end_time and not state['stop_auto']:
                await SEndPacKeT(bot_state['whisper_writer'], bot_state['online_writer'], 'OnLine', start_pkt)
                await asyncio.sleep(start_spam_delay)
            if state['stop_auto']: break
            await asyncio.sleep(wait_after_match)
            if state['stop_auto']: break
            leave_pkt = await leave_squad_packet(key, iv, region)
            await SEndPacKeT(bot_state['whisper_writer'], bot_state['online_writer'], 'OnLine', leave_pkt)
            await asyncio.sleep(2)
        except: break
    state['running'] = False; state['stop_auto'] = False

async def safe_send_message(chat_type, message, target_uid, chat_id, key, iv, region, bot_state, max_retries=3):
    for _ in range(max_retries):
        try:
            P = await SEndMsG(chat_type, message, target_uid, chat_id, key, iv, region)
            await SEndPacKeT(bot_state['whisper_writer'], bot_state['online_writer'], 'ChaT', P)
            return True
        except: await asyncio.sleep(0.5)
    return False

# --- TCP HANDLERS ---
async def TcPOnLine(ip, port, auth_token, bot_state, reconnect_delay=0.5):
    while True:
        try:
            reader, writer = await asyncio.open_connection(ip, int(port))
            bot_state['online_writer'] = writer; writer.write(bytes.fromhex(auth_token)); await writer.drain()
            while True:
                if not await reader.read(9999): break
            bot_state['online_writer'].close(); await bot_state['online_writer'].wait_closed(); bot_state['online_writer'] = None
        except:
            if bot_state['online_writer']: bot_state['online_writer'].close(); await bot_state['online_writer'].wait_closed(); bot_state['online_writer'] = None
        await asyncio.sleep(reconnect_delay)

async def TcPChaT(ip, port, auth_token, key, iv, ready_event, region, bot_state, reconnect_delay=0.5):
    auto_start_state = {'running': False, 'stop_auto': False, 'task': None}
    
    while True:
        try:
            reader, writer = await asyncio.open_connection(ip, int(port))
            bot_state['whisper_writer'] = writer; writer.write(bytes.fromhex(auth_token)); await writer.drain(); ready_event.set()
            while True:
                data = await reader.read(9999)
                if not data: break
                if data.hex().startswith("120000"):
                    try:
                        proto = DEcwHisPErMsG_pb2.DecodeWhisper()
                        proto.ParseFromString(bytes.fromhex(data.hex()[10:]))
                        uid = proto.Data.uid; chat_id = proto.Data.Chat_ID; inPuTMsG = proto.Data.msg.strip().lower()
                        print(f"Msg: {inPuTMsG} from {uid}")
                        
                        if inPuTMsG.startswith('/me'):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                await safe_send_message(proto.Data.chat_type, "[B][C][FF0000]❌ Usage: /me [TeamCode] [Emote/Num] or [TeamCode] [UID] [Emote/Num]", uid, chat_id, key, iv, region, bot_state)
                                continue
                            
                            try:
                                team_code = parts[1]
                                last_part = parts[-1].lower()
                                emote_id = (NUMBER_EMOTES.get(last_part) or NAME_EMOTES.get(last_part))
                                target_uid = int(parts[2]) if len(parts) == 4 else int(uid)
                                
                                if not emote_id:
                                    await safe_send_message(proto.Data.chat_type, f"[B][C][FF0000]❌ Invalid emote: {last_part}", uid, chat_id, key, iv, region, bot_state)
                                    continue
                                
                                # High-Speed 100% Guarantee: 0.2s Delay + Triple Send
                                initial_leave = await leave_squad_packet(key, iv, region)
                                await SEndPacKeT(bot_state['whisper_writer'], bot_state['online_writer'], 'OnLine', initial_leave)
                                await asyncio.sleep(0.05)

                                join_pkt = await GenJoinSquadsPacket(team_code, key, iv)
                                await SEndPacKeT(bot_state['whisper_writer'], bot_state['online_writer'], 'OnLine', join_pkt)
                                await asyncio.sleep(0.2) # Adjusted to 0.2s for balanced speed
                                
                                emote_pkt = await Emote_k(target_uid, int(emote_id), key, iv, region)
                                # Send 4 times instantly for maximum guarantee
                                await SEndPacKeT(bot_state['whisper_writer'], bot_state['online_writer'], 'OnLine', emote_pkt)
                                await SEndPacKeT(bot_state['whisper_writer'], bot_state['online_writer'], 'OnLine', emote_pkt)
                                await SEndPacKeT(bot_state['whisper_writer'], bot_state['online_writer'], 'OnLine', emote_pkt)
                                await SEndPacKeT(bot_state['whisper_writer'], bot_state['online_writer'], 'OnLine', emote_pkt)
                                await asyncio.sleep(0.2) # Adjusted to 0.2s before leaving
                                
                                final_leave = await leave_squad_packet(key, iv, region)
                                # Send leave 3 times for 100% guarantee
                                await SEndPacKeT(bot_state['whisper_writer'], bot_state['online_writer'], 'OnLine', final_leave)
                                await SEndPacKeT(bot_state['whisper_writer'], bot_state['online_writer'], 'OnLine', final_leave)
                                await SEndPacKeT(bot_state['whisper_writer'], bot_state['online_writer'], 'OnLine', final_leave)
                                
                                await safe_send_message(proto.Data.chat_type, f"[B][C][00FF00]✅ Done! Joined {team_code} and sent emote.", uid, chat_id, key, iv, region, bot_state)
                            except:
                                await safe_send_message(proto.Data.chat_type, "[B][C][FF0000]❌ Execution Error!", uid, chat_id, key, iv, region, bot_state)

                        elif inPuTMsG.startswith('/e'):
                            parts = inPuTMsG.strip().split()
                            if len(parts) == 1 or (len(parts) == 2 and parts[1].lower() == 'list'):
                                msg = f"[B][C][00FF00]🎭 EMOTE SYSTEM\n• Numbers: 1-{len(NUMBER_EMOTES)}\n• Names: {len(NAME_EMOTES)} names\nUsage:\n/e [name/num]\n/e [uid] [name/num]"
                                await safe_send_message(proto.Data.chat_type, msg, uid, chat_id, key, iv, region, bot_state)
                                continue
                            
                            try:
                                last_part = parts[-1].lower()
                                is_direct = last_part.isdigit() and len(last_part) == 9 and last_part.startswith("9090")
                                emote_id = int(last_part) if is_direct else (NUMBER_EMOTES.get(last_part) or NAME_EMOTES.get(last_part))
                                
                                if not emote_id:
                                    await safe_send_message(proto.Data.chat_type, f"[B][C][FF0000]❌ Invalid emote: {last_part}", uid, chat_id, key, iv, region, bot_state)
                                    continue
                                
                                target_uids = [int(parts[1])] if len(parts) == 3 else [int(uid)]
                                for t_uid in target_uids:
                                    pkt = await Emote_k(t_uid, int(emote_id), key, iv, region)
                                    await SEndPacKeT(bot_state['whisper_writer'], bot_state['online_writer'], 'OnLine', pkt)
                                    await asyncio.sleep(0.1)
                                await safe_send_message(proto.Data.chat_type, f"[B][C][00FF00]✅ Emote Sent!", uid, chat_id, key, iv, region, bot_state)
                            except:
                                await safe_send_message(proto.Data.chat_type, "[B][C][FF0000]❌ Format Error!", uid, chat_id, key, iv, region, bot_state)

                        elif inPuTMsG in ('/3', '/4', '/5', '/6'):
                            limit = int(inPuTMsG[1:])
                            initial_message = f"[B][C][00FFFF]\n\nCreating {limit}-Player Group...\n\n"
                            await safe_send_message(proto.Data.chat_type, initial_message, uid, chat_id, key, iv, region, bot_state)
                            
                            try:
                                PAc = await OpEnSq(key, iv, region)
                                await SEndPacKeT(bot_state['whisper_writer'], bot_state['online_writer'], 'OnLine', PAc)
                                
                                C = await cHSq(limit, uid, key, iv, region)
                                await asyncio.sleep(0.3)
                                await SEndPacKeT(bot_state['whisper_writer'], bot_state['online_writer'], 'OnLine', C)
                                
                                V = await SEnd_InV(limit, uid, key, iv, region)
                                await asyncio.sleep(0.3)
                                await SEndPacKeT(bot_state['whisper_writer'], bot_state['online_writer'], 'OnLine', V)
                                
                                E = await leave_squad_packet(key, iv, region)
                                await asyncio.sleep(3.5)
                                await SEndPacKeT(bot_state['whisper_writer'], bot_state['online_writer'], 'OnLine', E)
                                
                                success_message = f"[B][C][00FF00]✅ SUCCESS! {limit}-Player Group invitation sent successfully to {uid}!\n"
                                await safe_send_message(proto.Data.chat_type, success_message, uid, chat_id, key, iv, region, bot_state)
                            except Exception as e:
                                await safe_send_message(proto.Data.chat_type, f"[B][C][FF0000]❌ ERROR: {str(e)}", uid, chat_id, key, iv, region, bot_state)

                        elif inPuTMsG.startswith('/lw '):
                            team_code = inPuTMsG.split()[1]
                            if auto_start_state['running']: continue
                            auto_start_state['stop_auto'] = False; auto_start_state['running'] = True
                            await safe_send_message(proto.Data.chat_type, f"[B][C][00FF00]Auto started for {team_code}", uid, chat_id, key, iv, region, bot_state)
                            auto_start_state['task'] = asyncio.create_task(auto_start_loop(team_code, uid, chat_id, proto.Data.chat_type, key, iv, region, auto_start_state, bot_state))
                        elif inPuTMsG == '/stop_auto':
                            auto_start_state['stop_auto'] = True; auto_start_state['running'] = False
                            if auto_start_state['task']: auto_start_state['task'].cancel()
                            await safe_send_message(proto.Data.chat_type, "[B][C][00FF00]Stopped", uid, chat_id, key, iv, region, bot_state)
                        elif inPuTMsG in ('/help', 'help', '/menu'):
                            help_msg = (
                                f"[B][C][00FFFF]🌟 NIKI BOT - COMMAND MENU 🌟\n"
                                f"[FFFFFF]────────────────────\n"
                                f"[00FF00]🎮 MATCH BOT:\n"
                                f"• /lw [Code] -> Auto Start Match\n"
                                f"• /stop_auto -> Stop Match Bot\n\n"
                                f"[FFFF00]👥 GROUP COMMANDS:\n"
                                f"• /3, /4, /5, /6 -> Set Group Limit\n"
                                f"• /exit -> Leave Group\n\n"
                                f"[FF00FF]🎭 EMOTE COMMANDS:\n"
                                f"• /e [name] -> Send Emote Self\n"
                                f"• /e [uid] [name] -> Send to UID\n"
                                f"• /me [Code] [name] -> Fast Attack\n\n"
                                f"[00FFFF]⚡ SYSTEM:\n"
                                f"• /e list -> View All Emotes\n"
                                f"[FFFFFF]────────────────────\n"
                                f"[00FF00]Developed by NIKI BOT 👑"
                            )
                            await safe_send_message(proto.Data.chat_type, help_msg, uid, chat_id, key, iv, region, bot_state)
                    except: pass
            bot_state['whisper_writer'].close(); await bot_state['whisper_writer'].wait_closed(); whisper_writer = None
        except:
            if bot_state['whisper_writer']: bot_state['whisper_writer'].close(); await bot_state['whisper_writer'].wait_closed(); whisper_writer = None
        await asyncio.sleep(reconnect_delay)

async def run_bot_instance(uid, password):
    print(f"🚀 Starting Bot Instance: {uid}")
    while True:
        try:
            # Login Process
            # Note: Assuming helper functions return dictionaries/values as described in instruction flow
            open_id, access_token = await GeNeRaTeAccEss(uid, password)
            if not open_id:
                print(f"❌ Login Failed for {uid}, retrying in 10s...")
                await asyncio.sleep(10); continue
            
            login_url, ob, version = await AuToUpDaTE()
            Hr = {'User-Agent': Uaa(), 'Connection': "Keep-Alive", 'Accept-Encoding': "gzip", 'Content-Type': "application/x-www-form-urlencoded", 'X-Unity-Version': "2018.4.11f1", 'X-GA': "v1 1", 'ReleaseVersion': ob}
            payload = await EncRypTMajoRLoGin(open_id, access_token, version)
            
            login_resp = await MajorLogin(login_url, payload, Hr)
            if not login_resp:
                print(f"❌ MajorLogin Failed for {uid}, retrying..."); await asyncio.sleep(5); continue
            
            auth = MajoRLoGinrEs_pb2.MajorLoginRes(); auth.ParseFromString(login_resp)
            login_data_resp = await GetLoginData(auth.url, payload, auth.token, Hr)
            if not login_data_resp:
                print(f"❌ LoginData Failed for {uid}, retrying..."); await asyncio.sleep(5); continue
            
            ports = PorTs_pb2.GetLoginData(); ports.ParseFromString(login_data_resp)
            chat_ip, chat_port = ports.AccountIP_Port.split(":")
            online_ip, online_port = ports.Online_IP_Port.split(":")
            auth_token = await xAuThSTarTuP(int(auth.account_uid), auth.token, int(auth.timestamp), auth.key, auth.iv)
            
            ready = asyncio.Event()
            bot_state = {'online_writer': None, 'whisper_writer': None}
            bot_info = {'uid': uid, 'key': auth.key, 'iv': auth.iv, 'region': getattr(auth, 'region', 'IND'), 'state': bot_state}
            ACTIVE_BOTS.append(bot_info)
            print(f"✅ Bot {uid} is now Online!")
            
            tasks = [
                asyncio.create_task(TcPChaT(chat_ip, chat_port, auth_token, auth.key, auth.iv, ready, getattr(auth, 'region', 'IND'), bot_state)),
                asyncio.create_task(TcPOnLine(online_ip, online_port, auth_token, bot_state))
            ]
            
            try:
                await asyncio.gather(*tasks)
            finally:
                if bot_info in ACTIVE_BOTS: ACTIVE_BOTS.remove(bot_info)
                
            print(f"⚠️ Bot {uid} connection lost, reconnecting...")
            await asyncio.sleep(5)
        except Exception as e:
            print(f"🔥 Error in Bot {uid}: {e}, auto-recovering...")
            await asyncio.sleep(5)

from aiohttp import web

async def handle_ping(request):
    return web.Response(text="Bot is alive!")

async def handle_emote(request):
    if not check_auth(request):
        return web.json_response({"error": "Unauthorized Access"}, status=401, headers={"Access-Control-Allow-Origin": "*"})
    try:
        data = await request.json()
        team_code = data.get('team_code')
        emote_id = data.get('emote_id')
        target_uids = data.get('target_uids', [])
        
        if not ACTIVE_BOTS:
            return web.json_response({"error": "No bots online to send emote"}, status=400, headers={"Access-Control-Allow-Origin": "*"})
            
        bot = ACTIVE_BOTS[0]
        
        # Initial Leave to ensure clean state
        initial_leave = await leave_squad_packet(bot['key'], bot['iv'], bot['region'])
        await SEndPacKeT(bot['state']['whisper_writer'], bot['state']['online_writer'], 'OnLine', initial_leave)
        await asyncio.sleep(0.05)

        # Join Squad
        join_pkt = await GenJoinSquadsPacket(team_code, bot['key'], bot['iv'])
        await SEndPacKeT(bot['state']['whisper_writer'], bot['state']['online_writer'], 'OnLine', join_pkt)
        await asyncio.sleep(0.2)
        
        # If no target UIDs provided, default to bot's own UID
        uids_to_emote = target_uids if target_uids else [bot['uid']]
        
        for uid in uids_to_emote:
            if not uid: continue
            try:
                t_uid = int(uid)
                emote_pkt = await Emote_k(t_uid, int(emote_id), bot['key'], bot['iv'], bot['region'])
                # Send 4 times for maximum guarantee
                for _ in range(4):
                    await SEndPacKeT(bot['state']['whisper_writer'], bot['state']['online_writer'], 'OnLine', emote_pkt)
                await asyncio.sleep(0.1) # Small delay between targets
            except: pass
            
        await asyncio.sleep(0.2)
        
        # Final Leave
        final_leave = await leave_squad_packet(bot['key'], bot['iv'], bot['region'])
        for _ in range(3):
            await SEndPacKeT(bot['state']['whisper_writer'], bot['state']['online_writer'], 'OnLine', final_leave)

        return web.json_response({"success": True, "message": f"Emote sent to {len(uids_to_emote)} targets"}, headers={"Access-Control-Allow-Origin": "*"})
    except Exception as e:
        return web.json_response({"error": str(e)}, status=500, headers={"Access-Control-Allow-Origin": "*"})

async def handle_group_invite(request):
    if not check_auth(request):
        return web.json_response({"error": "Unauthorized Access"}, status=401, headers={"Access-Control-Allow-Origin": "*"})
    try:
        data = await request.json()
        limit = int(data.get('limit', 4))
        target_uid = data.get('target_uid')
        
        if not ACTIVE_BOTS:
            return web.json_response({"error": "No bots online"}, status=400, headers={"Access-Control-Allow-Origin": "*"})
            
        bot = ACTIVE_BOTS[0]
        t_uid = int(target_uid) if target_uid else int(bot['uid'])
        
        PAc = await OpEnSq(bot['key'], bot['iv'], bot['region'])
        await SEndPacKeT(bot['state']['whisper_writer'], bot['state']['online_writer'], 'OnLine', PAc)
        
        C = await cHSq(limit, t_uid, bot['key'], bot['iv'], bot['region'])
        await asyncio.sleep(0.3)
        await SEndPacKeT(bot['state']['whisper_writer'], bot['state']['online_writer'], 'OnLine', C)
        
        V = await SEnd_InV(limit, t_uid, bot['key'], bot['iv'], bot['region'])
        await asyncio.sleep(0.3)
        await SEndPacKeT(bot['state']['whisper_writer'], bot['state']['online_writer'], 'OnLine', V)
        
        async def delayed_leave():
            await asyncio.sleep(3.5)
            E = await leave_squad_packet(bot['key'], bot['iv'], bot['region'])
            await SEndPacKeT(bot['state']['whisper_writer'], bot['state']['online_writer'], 'OnLine', E)
        
        asyncio.create_task(delayed_leave())
        return web.json_response({"success": True, "message": f"Group invitation ({limit}) sent to {t_uid}"}, headers={"Access-Control-Allow-Origin": "*"})
    except Exception as e:
        return web.json_response({"error": str(e)}, status=500, headers={"Access-Control-Allow-Origin": "*"})

WEB_AUTO_START_STATE = {'running': False, 'stop_auto': False, 'task': None, 'team_code': None}

async def handle_auto_start(request):
    if not check_auth(request):
        return web.json_response({"error": "Unauthorized Access"}, status=401, headers={"Access-Control-Allow-Origin": "*"})
    try:
        data = await request.json()
        action = data.get('action')
        team_code = data.get('team_code')
        
        if action == 'stop':
            WEB_AUTO_START_STATE['stop_auto'] = True
            WEB_AUTO_START_STATE['running'] = False
            if WEB_AUTO_START_STATE['task']:
                WEB_AUTO_START_STATE['task'].cancel()
                WEB_AUTO_START_STATE['task'] = None
            return web.json_response({"success": True, "message": "Auto start stopped"}, headers={"Access-Control-Allow-Origin": "*"})
            
        if not team_code:
            return web.json_response({"error": "Team Code required"}, status=400, headers={"Access-Control-Allow-Origin": "*"})

        if not ACTIVE_BOTS:
            return web.json_response({"error": "No bots online"}, status=400, headers={"Access-Control-Allow-Origin": "*"})
            
        if WEB_AUTO_START_STATE['running']:
            return web.json_response({"error": "Auto start already running"}, status=400, headers={"Access-Control-Allow-Origin": "*"})

        bot = ACTIVE_BOTS[0]
        WEB_AUTO_START_STATE['stop_auto'] = False
        WEB_AUTO_START_STATE['running'] = True
        WEB_AUTO_START_STATE['team_code'] = team_code
        
        async def web_auto_start_loop():
            try:
                while not WEB_AUTO_START_STATE['stop_auto']:
                    join_pkt = await join_teamcode_packet(team_code, bot['key'], bot['iv'], bot['region'])
                    await SEndPacKeT(bot['state']['whisper_writer'], bot['state']['online_writer'], 'OnLine', join_pkt)
                    await asyncio.sleep(2)
                    start_pkt = await start_auto_packet(bot['key'], bot['iv'], bot['region'])
                    end_time = time.time() + start_spam_duration
                    while time.time() < end_time and not WEB_AUTO_START_STATE['stop_auto']:
                        await SEndPacKeT(bot['state']['whisper_writer'], bot['state']['online_writer'], 'OnLine', start_pkt)
                        await asyncio.sleep(start_spam_delay)
                    if WEB_AUTO_START_STATE['stop_auto']: break
                    await asyncio.sleep(wait_after_match)
                    if WEB_AUTO_START_STATE['stop_auto']: break
                    leave_pkt = await leave_squad_packet(bot['key'], bot['iv'], bot['region'])
                    await SEndPacKeT(bot['state']['whisper_writer'], bot['state']['online_writer'], 'OnLine', leave_pkt)
                    await asyncio.sleep(2)
            except Exception as e:
                print(f"Web Auto Start Error: {e}")
            finally:
                WEB_AUTO_START_STATE['running'] = False
                WEB_AUTO_START_STATE['task'] = None

        WEB_AUTO_START_STATE['task'] = asyncio.create_task(web_auto_start_loop())
        return web.json_response({"success": True, "message": f"Auto start initiated for {team_code}"}, headers={"Access-Control-Allow-Origin": "*"})
    except Exception as e:
        return web.json_response({"error": str(e)}, status=500, headers={"Access-Control-Allow-Origin": "*"})

async def handle_bots(request):
    if not check_auth(request):
        return web.json_response({"error": "Unauthorized Access"}, status=401, headers={"Access-Control-Allow-Origin": "*"})
    try:
        bots = [{"uid": b['uid'], "region": b['region']} for b in ACTIVE_BOTS]
        return web.json_response({"bots": bots}, headers={"Access-Control-Allow-Origin": "*"})
    except Exception as e:
        return web.json_response({"error": str(e)}, status=500, headers={"Access-Control-Allow-Origin": "*"})

async def handle_login(request):
    try:
        data = await request.json()
        user = data.get('username')
        pwd = data.get('password')
        if user == ADMIN_USER and pwd == ADMIN_PASS:
            return web.json_response({"success": True, "token": ADMIN_PASS}, headers={"Access-Control-Allow-Origin": "*"})
        else:
            return web.json_response({"error": "Invalid Username or Password"}, status=401, headers={"Access-Control-Allow-Origin": "*"})
    except Exception as e:
        return web.json_response({"error": str(e)}, status=500, headers={"Access-Control-Allow-Origin": "*"})

async def handle_options(request):
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST, GET, OPTIONS, HEAD",
        "Access-Control-Allow-Headers": "Content-Type",
    }
    return web.Response(headers=headers)

async def start_web_server():
    app = web.Application()
    app.router.add_get('/', handle_ping)
    app.router.add_post('/api/emote', handle_emote)
    app.router.add_post('/api/group_invite', handle_group_invite)
    app.router.add_post('/api/auto_start', handle_auto_start)
    app.router.add_get('/api/bots', handle_bots)
    app.router.add_post('/api/login', handle_login)
    app.router.add_options('/api/emote', handle_options)
    app.router.add_options('/api/group_invite', handle_options)
    app.router.add_options('/api/auto_start', handle_options)
    app.router.add_options('/api/login', handle_options)
    
    port = int(os.environ.get("PORT", 8080))
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"🌐 Web API Server started on port {port}")

async def MaiiiinE():
    asyncio.create_task(start_web_server())
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"--- {LEVEL_UP} MULTI-ID SYSTEM ---")
            accounts = load_all_credentials()
            if not accounts: 
                print("❌ No accounts found in bot.txt! Retrying in 10s...")
                await asyncio.sleep(10)
                continue
            print(f"📝 Loaded {len(accounts)} accounts.")
            bot_tasks = [run_bot_instance(uid, pwd) for uid, pwd in accounts]
            await asyncio.gather(*bot_tasks)
        except Exception as e:
            print(f"🔥 Critical Main Error: {e}. Auto-recovering in 5s...")
            await asyncio.sleep(5)

if __name__ == '__main__':
    try:
        asyncio.run(MaiiiinE())
    except KeyboardInterrupt:
        print("\nStopping bot...")
    except Exception as e:
        print(f"CRITICAL ERROR: {e}")
        traceback.print_exc()
        input("Press Enter to exit...") # Keeps the window open if it crashes
