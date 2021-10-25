import random, string
import time
import requests

print("""                                                                                
 ██▓███   ▒█████    ██████  ██▓▓█████▄ ▓█████  ███▄    █   ██████      ▄████ ▓█████  ███▄    █ 
▓██░  ██▒▒██▒  ██▒▒██    ▒ ▓██▒▒██▀ ██▌▓█   ▀  ██ ▀█   █ ▒██    ▒     ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
▓██░ ██▓▒▒██░  ██▒░ ▓██▄   ▒██▒░██   █▌▒███   ▓██  ▀█ ██▒░ ▓██▄      ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
▒██▄█▓▒ ▒▒██   ██░  ▒   ██▒░██░░▓█▄   ▌▒▓█  ▄ ▓██▒  ▐▌██▒  ▒   ██▒   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
▒██▒ ░  ░░ ████▓▒░▒██████▒▒░██░░▒████▓ ░▒████▒▒██░   ▓██░▒██████▒▒   ░▒▓███▀▒░▒████▒▒██░   ▓██░
▒▓▒░ ░  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓   ▒▒▓  ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░    ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
░▒ ░       ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░ ░ ▒  ▒  ░ ░  ░░ ░░   ░ ▒░░ ░▒  ░ ░     ░   ░  ░ ░  ░░ ░░   ░ ▒░
░░       ░ ░ ░ ▒  ░  ░  ░   ▒ ░ ░ ░  ░    ░      ░   ░ ░ ░  ░  ░     ░ ░   ░    ░      ░   ░ ░ 
             ░ ░        ░   ░     ░       ░  ░         ░       ░           ░    ░  ░         ░ 
                                ░                                                                                                                  
                                                                                
                                                                                
Nitro Checker""")
print("Creator  >>>  Blank.666k ")
print("Links  >>>  https://github.com/blank666k   \n")

num=input('Please enter how many codes to generate: ')

f=open("Nitro Codes.txt","w", encoding='utf-8')


print("Wait, Generating for you!")
time.sleep(0.5)
for n in range(int(num)):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
   f.write('https://discord.gift/')
   f.write(y)
   f.write("\n")

f.close()

#=============Checker=========================


with open("Nitro Codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)
        valid = open("Valid Codes.txt","w", encoding='utf-8')

        if r.status_code == 200:
            print(" Valid | {} ".format(line.strip("\n")))
            valid.write("Valid | {} ".format(line.strip("\n")))
            break
        else:
        	print(" Invalid | {} ".format(line.strip("\n")))
