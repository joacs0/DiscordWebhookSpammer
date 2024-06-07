from colorama import Fore
from datetime import datetime
import requests, os, time, ctypes

asciiText = """
█     █░▓█████  ▄▄▄▄    ██░ ██  ▒█████   ▒█████   ██ ▄█▀
▓█░ █ ░█░▓█   ▀ ▓█████▄ ▓██░ ██▒▒██▒  ██▒▒██▒  ██▒ ██▄█▒ 
▒█░ █ ░█ ▒███   ▒██▒ ▄██▒██▀▀██░▒██░  ██▒▒██░  ██▒▓███▄░ 
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀  ░▓█ ░██ ▒██   ██░▒██   ██░▓██ █▄ 
░░██▒██▓ ░▒████▒░▓█  ▀█▓░▓█▒░██▓░ ████▓▒░░ ████▓▒░▒██▒ █▄
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒
  ▒ ░ ░   ░ ░  ░▒░▒   ░  ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░
  ░   ░     ░    ░    ░  ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░ 
    ░       ░  ░ ░       ░  ░  ░    ░ ░      ░ ░  ░  ░   
                      ░
██████  ██▓███▄▄▄           ███▄ ▄███▓ ███▄ ▄███▓▓█████  ██▀███  
▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░▓██    ▓██░▒███   ▓██ ░▄█ ▒
  ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░
░  ░  ░  ░░         ░   ▒   ░      ░   ░      ░      ░     ░░   ░ 
      ░                 ░  ░       ░          ░      ░  ░   ░                                                                                                                                                       

"""
divider = ""



class WebHook:
    def __init__(self, url: str):
        self.url = url

    def sendRequest(self, message: str):
        requests.post(self.url, json={'content': message})

    def deleteWebhook(self):
        requests.delete(self.url)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def main():

    now = datetime.now()
    current = now.strftime("%H:%M:%S")

    cls()
    ctypes.windll.kernel32.SetConsoleTitleW('Webhook Spammer By: joacs0')

    print(f"{Fore.RED}{asciiText}")
    print(f"{Fore.RED}{divider}{Fore.RESET}")
    print(f"{Fore.RED}{divider}{Fore.RESET}")
    url = input(f"{Fore.RED}Enter webhook url:{Fore.RESET} ")
    print(f"{Fore.RED}{divider}{Fore.RESET}")
    webhook = WebHook(url)

    while True:
        print(f"{Fore.RED}{divider}{Fore.RESET}")
        print(f"\n{Fore.RED}[{Fore.RESET}1{Fore.RED}] Spam Webhook")
        print(f"{Fore.RED}[{Fore.RESET}2{Fore.RED}] Delete Webhook")
        print(f"{Fore.RED}[{Fore.RESET}3{Fore.RED}] Exit")
        print(f"{Fore.RED}{divider}{Fore.RESET}")
        
        option = int(input(f"\n{Fore.RED}>>>{Fore.RESET} "))

        if option > 3:
            cls()
            print(f"[{Fore.RED}ERROR{Fore.RESET}] {Fore.RED}Pick A Number between {Fore.RESET}1 {Fore.RED}- {Fore.RESET}3\n")
            continue

        match option:
            case 1:
                cls()
                message = input(f"{Fore.RED}Enter a message for spamming:{Fore.RESET} ")
                amount = int(input(f"{Fore.RED}Enter amount of messages to send:{Fore.RESET} "))
                delay = int(input(f"{Fore.RED}Enter delay for message sending:{Fore.RESET} "))

                for i in range(amount + 1):
                    print(f"{Fore.RED}[{Fore.RESET}{current}{Fore.RED}] Message {Fore.RED}[{Fore.RESET}{i}{Fore.RED}] sent to Webhook")
                    webhook.sendRequest(message)
                time.sleep(delay)
                
                cls()
                print(f"{Fore.RED}Task Done {Fore.RESET}[{Fore.RED}{amount}{Fore.RESET}]{Fore.RED} messages have been sent to {Fore.RESET}[{Fore.RED}{url}{Fore.RESET}]{Fore.RED}\n")

            case 2:
                cls()
                print(f"{Fore.RED}Webhook {Fore.RESET}{url}{Fore.RED} has been deleted")
                webhook.deleteWebhook()

            case 3:
                cls()
                break

if __name__ == "__main__":
    main()
    
