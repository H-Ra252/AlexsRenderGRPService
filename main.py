import os 
import threading
import requests, random
from dhooks import Webhook

import time



time.sleep(5)

def groupfinder():
    id = random.randint(1, 115000000) #Change this to the range you want to scan
    r = requests.get(f"https://www.roblox.com/groups/group.aspx?gid={id}") 
    if 'owned' not in r.text:
        re = requests.get(f"https://groups.roblox.com/v1/groups/{id}")
        if 'isLocked' not in re.text and 'owner' in re.text:
            if re.json()['publicEntryAllowed'] == True and re.json()['owner'] == None:
                hook.send(f'Hit: https://www.roblox.com/groups/group.aspx?gid={id}')
                print(f"[+] Hit: {id}")
            else:
                print(f"[-] No Entry Allowed: {id}")
        else:
            print(f"[-] Group Locked: {id}")
    else:
        print(f"[-] Group Already Owned: {id}")


print("""
____ _    ____ _  _ ____    ____ ____ ____ _  _ ___  
|__| |    |___ |_/  [__     | __ |__/ |  | |  | |__] 
|  | |___ |___ | \_ ___]    |__] |  \ |__| |__| |    
                                                     
____ _ _  _ ___  ____ ____ 
|___ | |\ | |  \ |___ |__/ 
|    | | \| |__/ |___ |  \ 
                           
""")

hook = https://discord.com/api/webhooks/1290266507170811936/e1PWsLjm-7-ugVPCLZOBizuj-f-dPSG2ZfG9u6D7vSOjE4dr0Ga_-9qLBvnejAxSeQqo
threads = 10000

while True:
    if threading.active_count() <= threads:
        threading.Thread(target=groupfinder).start()
