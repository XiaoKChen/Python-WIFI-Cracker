#!/usr/bin/python3'
import subprocess


def decrypt_cap(WORD_LIST):
    aircrack = f'sudo aircrack-ng ./capture_data/WPACracking-01.cap -w {WORD_LIST}'.split()
    subprocess.run(aircrack)
