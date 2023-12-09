import requests
import os
import time

R = '\033[31m'
G = '\033[32m'
W = '\033[0m'

def banner():     
    print(G+"███╗   ██╗ ██████╗ ██╗     ███████╗██████╗  █████╗ ███╗   ███╗\n████╗  ██║██╔════╝ ██║     ██╔════╝██╔══██╗██╔══██╗████╗ ████║\n██╔██╗ ██║██║  ███╗██║     ███████╗██████╔╝███████║██╔████╔██║\n██║╚██╗██║██║   ██║██║     ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║\n██║ ╚████║╚██████╔╝███████╗███████║██║     ██║  ██║██║ ╚═╝ ██║\n╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝\n                Created by N3RG0")

def nglspam():

    os.system('cls' if os.name == 'nt' else 'clear') 
    nglusernames = []
    banner()
    numusers = int(input(W+"Ingresa el numero de usuarios a spamear: "))

    for i in range(numusers):
        nglusernames.append(input("Ingresa el usuario {} sin @: ".format(i+1)))
    
    message = input("Ingresa el mensaje: ")
    numbersend = int(input("Ingresa el numero de mensajes totales a enviar: "))

    print("**********************************************************")
    os.system('cls' if os.name == 'nt' else 'clear') 
    banner()
    i=0
    value =0
    notsend =0
    count = 0
    while count < numbersend:
        nglusername=nglusernames[i% len(nglusernames)]
        i+=1
        headers = {
            'Host': 'ngl.link',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'origin': 'https://ngl.link',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': f'https://ngl.link/{nglusername}',
            'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = {
            'username': f'{nglusername}',
            'question': f'{message}',
            'deviceId': '0',
            'gameSlug': '',
            'referrer': '',
        }

        if value == 10 or notsend==5:
            os.system('cls' if os.name == 'nt' else 'clear')
            banner()
            value=0

        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            count += 1
            print(G+"[+] Enviado"+W+" Usuario => {}".format(nglusername)+W+" total enviados=> {}".format(count)+W)
        else:
            notsend += 1
            print(R+"[-]"+W+"No enviado")
        if notsend == 10:
            print(R+"[!]"+W+"Espeare 5 seg")
            time.sleep(5)
            notsend = 0
       
nglspam()
