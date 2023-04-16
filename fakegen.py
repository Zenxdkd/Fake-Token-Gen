import random as lmao
import time as mucho
from pystyle import *
from pystyle import Colors, Colorate
import ctypes as retard
counter = 1
kernel32 = retard.windll.kernel32
kernel32.SetConsoleTitleW("Dork Token Gen")
banner = """







___________________________________________
| ╔╦╗╔═╗╦═╗╦╔═  ╔╦╗╔═╗╦╔═╔═╗╔╗╔  ╔═╗╔═╗╔╗╔ |
|  ║║║ ║╠╦╝╠╩╗   ║ ║ ║╠╩╗║╣ ║║║  ║ ╦║╣ ║║║ |
| ═╩╝╚═╝╩╚═╩ ╩   ╩ ╚═╝╩ ╩╚═╝╝╚╝  ╚═╝╚═╝╝╚╝ |
|        Developer > Synthetic#0679        |
|__________________________________________|

"""
print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(banner)))
int(input(f"                                   {Colors.purple} [+] Threads? (ONLY NUMBERS) > "))
int(input(f"                                   {Colors.purple} [+] Captcha Key? (ONLY NUMBERS) > "))
mucho.sleep(2)
words = ['tucans', 'lol', 'synthetic', 'daddy', 'pooron', 'loser', 'retard', 'easygen', 'real', 'tokenlover']
emails = [f"{word}{lmao.randint(0, 999)}@synthetic.com" for word in words]
while True:
    kernel32.SetConsoleTitleW(f"Tokens Generated: {counter}")
    counter += 1
    email = lmao.choice(emails)
    tokenretard = ''.join(lmao.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=6))
    tokenfatass = ''.join(lmao.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=39))
    tokenbruh = f"MzgwMTQ2Mzg4MTU3MzMzNTA0.{tokenretard}.{tokenfatass}"
    with open('tokens.txt', 'a') as f:
        f.write(f"Token > {tokenbruh}\n")
    print(f"Email: {email}\nToken: {tokenbruh}\n")
    mucho.sleep(5)
