from os import system as sys
from time import sleep

sys('cls')

def set_ipdns():
    sys('netsh interface ip set address "Wireless Network Connection" static 10.13.160.150 255.255.255.0 10.13.160.5')
    sys('netsh interface ipv4 set dns "Wireless Network Connection" static 10.13.2.20 primary')
    sys('netsh interface ipv4 add dns "Wireless Network Connection" 10.13.2.21 index=2')
def del_ipdns():
    sys('netsh interface ipv4 set address name="Wireless Network Connection" source=dhcp')
    sys('netsh interface ipv4 set dnsserver name="Wireless Network Connection" source=dhcp')

print('''ipdns changer [Version 1.2]
Copyright (c) 2022 OmarFatahi.  All rights reserved.
''')
delorset = input('Set(1) IpDns or Del(2) >> ')

if delorset == '1':
    print('OK!\nplease 2sec wait')
    sleep(2)
    set_ipdns()
    sys('cls')
    print("it's end...")
    sleep(1)
elif delorset == '2':
    print('OK!\nplease 2sec wait')
    sleep(2)
    del_ipdns()
    sys('cls')
    print("it's end...")
    sleep(1)
else:
    quit()
