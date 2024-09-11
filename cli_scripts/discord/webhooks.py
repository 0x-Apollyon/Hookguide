from urllib.request import Request, urlopen
import urllib.error
import json
import os


def ensure_webhook(webhook):
    if r"https://" not in webhook and r"http://" not in webhook:
        webhook = r"https://" + webhook

    must_be_webhook = "https://discord.com/api/webhooks/"
    if must_be_webhook not in webhook:
        print("[X] Not a valid webhook URL")
        return False
    if len(webhook.split("/")) != 7:
        print("[X] Not a valid webhook URL")
        return False
    return webhook

def error_handler(e):
    match str(e):
        case "HTTP Error 401: Unauthorized":
            print("[X] Malformed webhook token")
        case "HTTP Error 404: Not Found":
            print("[X] Webhook does not exist or was deleted")
        case "HTTP Error 400: Bad Request":
            print("[X] Malformed webhook ID")
        case "HTTP Error 429: Too Many Requests":
            print("[X] You are being ratelimited. Try again later")
        case _:
            print("[X] Unknown error occured")

def send_message(webhook , message , new_name , new_pfp):
    
    message = {"content": message}

    if new_name:
        message["username"] = new_name

    if new_pfp:
        if r"https://" not in new_pfp and r"http://" not in new_pfp:
            new_pfp = r"https://" + new_pfp
        message["avatar_url"] = new_pfp

    req = Request(webhook , json.dumps(message).encode())
    req.add_header('Content-Type', 'application/json')
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')

    try:
        response = urlopen(req)
        response.read()
        print("[*] Sent the message")
    except urllib.error.HTTPError as e:
        error_handler(e)
    except:
        print("[X] An unknown error occured")

def get_webhook_info(webhook):
    req = Request(webhook)


    req.add_header('Content-Type', 'application/json')
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')

    try:
        response = urlopen(req)
        response_json = json.loads(response.read().decode())
        for key in response_json:
            print(f"{key} --> {response_json[key]}")


    except urllib.error.HTTPError as e:
        error_handler(e)
    except:
        print("[X] An unknown error occured")

def delete_hook(webhook_url):
    req = Request(webhook_url, method="DELETE")
    req.add_header('Content-Type', 'application/json')
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')

    try:
        response = urlopen(req)
        print("[*] DELETED WEBHOOK")
    except urllib.error.HTTPError as e:
        error_handler(e)
    except:
        print("[X] An unknown error occured")

def display_options():
    print("(1)Get webhook info \n(2)Send a message through the webhook \n(3)Delete webhook \n(4)Clear screen \n(5)Quit\n")

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

webhook = ensure_webhook(webhook)

def display_banner():
    print("===============|-| HooksGuide |-|===============")
    print("Discord webhook utils")
    print("By: Apollyon\n")

clear_screen()
display_banner()  
display_options()

while True:
    user_input = input("> ").strip().lower()
    match user_input:
        case "1" | "info" | "get webhook info" | "webhook info":
            webhook_url = input("Enter webhook URL | > ").strip()
            if ensure_webhook(webhook_url):
                get_webhook_info(webhook_url)
        case "2" | "send a message through the webhook" | "send message":
            webhook_url = input("Enter webhook URL | > ").strip()
            if ensure_webhook(webhook_url):
                new_name = input("Enter the name for the webhook (Leave blank for default) | > ").strip()
                new_pfp = input("Enter the URL for the webhooks profile picture (Leave blank for default) | > ").strip()
                message = input("Enter message to send | > ").strip()
                if len(message) <= 2000:
                    send_message(webhook_url , message , new_name , new_pfp)
        case "3" | "delete webhook" | "delete":
            webhook_url = input("Enter webhook URL | > ").strip()
            if ensure_webhook(webhook_url):
                delete_hook(webhook_url)
        case "4" | "clear screen" | "clear" | "cls":
            clear_screen()
            display_banner()  
            display_options()
        case "5" | "quit" | "exit" | "close":
            quit()
        case _:
            print("[X] INVALID OPTION")
    

    

