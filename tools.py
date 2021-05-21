#Untuk pencury kontol kalian anjing

import os, sys, time, datetime, random

os.system("pip install -r requirements")

def menu1():
    os.system('clear')
    print('''

 ████████╗██████╗  ██████╗      ██╗ █████╗ ███╗   ██╗
 ╚══██╔══╝██╔══██╗██╔═══██╗     ██║██╔══██╗████╗  ██║
    ██║   ██████╔╝██║   ██║     ██║███████║██╔██╗ ██║
    ██║   ██╔══██╗██║   ██║██   ██║██╔══██║██║╚██╗██║
    ██║   ██║  ██║╚██████╔╝╚█████╔╝██║  ██║██║ ╚████║
    ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝

    ''')
    x = datetime.datetime.now()
    print(f'{x.strftime("%A %d %m %Y")}')
    print('CONTOH = 08123456789')
    trojan1 = input('MASUKAN NOMOR TELFON: ')
    try:
        float(trojan1)
    except ValueError:
        print("NOMOR SALAH, MASUKAN NOMOR YANG BENAR!")
        time.sleep(3)
        os.system('clear')
        menu1()
    trojan2 = int(input('Masukan jumlah trojan: '))
    
    try:
        float(trojan2)
    except ValueError:
        print('JUMLAH TROJAN SALAH! MASUKAN ANGKA!!!')
        time.sleep(3)
        os.system('clear')
        menu1()

    input('TEKAN ENTER UNTUK MENYERANG!')
    os.system('clear')
    angka = 0
    for i in range(trojan2):
        time.sleep(0.05)
        angka = angka + 1
        print(f'Package[{random.randrange(1000, 9999)}] DOMINO MENYERANG {trojan1} {angka}')



def menu2():
    os.system('clear')
    print('''
██████╗ ██████╗  ██████╗ ███████╗
██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██║  ██║██║  ██║██║   ██║███████╗
██║  ██║██║  ██║██║   ██║╚════██║
██████╔╝██████╔╝╚██████╔╝███████║
╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
    ''')
    x = datetime.datetime.now()
    print(f'{x.strftime("%A %d %m %Y")}')
    print('Gunakanlah sebijak mungkin')
    dos1 = input('ALAMAT IP / WEBSITE: ')
    dos2 = input('Masukan jumlah thread: ')
    print("""
    [1] UDP
    [2] TCP
    [3] HTTP
    [4] OVERLOAD
    [5] SOCKS
    """)
    dos3 = input('Masukan metode: ')
    if dos3 == '1' or dos3 == '2' or dos3 == '3' or dos3 == '4' or dos3 == '5':
        input("ENTER UNTUK MENYERANG!")
        os.system('clear')
        angka = 0
        while True:
            time.sleep(0.05)
            angka = angka + 1
            print(f"{angka} MENYERANG {dos1} [{dos2}] {random.randrange(1000, 9999)} ")
    else:
        print('METODE SALAH! MASUKAN DENGAN BENAR!')
        time.sleep(3)
        os.system('clear')
        menu2()




os.system('clear')
print('''
▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
    ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
  ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
             ░ ░      ░ ░      ░  ░      ░      
MADE BY DOMINO
+62 878508089018                                                    
''')
x = datetime.datetime.now()
print(f'{x.strftime("%A %d %m %Y")}')
print("=====MENU=====")
print("[1] TROJAN NOMOR TELFON")
print("[2] SERANGAN DDOS KE WEBSITE")
mens = input("PILIH: ")
if mens == '1':
    menu1()
elif mens == '2':
    menu2()
else:
    print('ERROR! SILAHKAN ULANG MULAI LAGI!')
    time.sleep(2)
