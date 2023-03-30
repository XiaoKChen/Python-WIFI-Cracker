#!/usr/bin/python3'
import sys
sys.path.append('./src')
from dotenv import load_dotenv

load_dotenv()

import os
from find_channel import findChannel

findChannel(os.environ['BSSID'])
