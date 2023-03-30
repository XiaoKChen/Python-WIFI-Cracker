#!/usr/bin/python3'
import subprocess
import csv


def findChannel(BSSID):
    cleanData()

    dataList = []

    airodump = 'sudo -S timeout 1 airodump-ng -w ./wifi_data/WifiData --output-format csv wlan0'.split()
    subprocess.run(airodump)

    createEditData()

    editData = open('./wifi_data/WifiData.csv', 'r')
    editData_reader = csv.DictReader(editData)

    for data in editData_reader:
        if data['BSSID'] == BSSID:
            return int(data[' channel'])


def createEditData():
    data = open('./wifi_data/WifiData-01.csv', 'r')
    data_reader = csv.reader(data)
    next(data_reader)
    data_rows = list(data_reader)

    createEditData = open('./wifi_data/WifiData.csv', 'w')
    createEditData_writer = csv.writer(createEditData)
    for data_row in data_rows:
        createEditData_writer.writerow(data_row)


def cleanData():
    subprocess.call(['rm', '-rf', './wifi_data/'])
    subprocess.call(['mkdir', './wifi_data'])
    print('Data Cleaned')
