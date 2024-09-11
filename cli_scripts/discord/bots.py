from urllib.request import Request, urlopen
import urllib.error
import json
import os
import base64
import datetime

discord_api_version = 10
discord_api_base_url = f"https://discord.com/api/v{discord_api_version}"

        


def get_token_info(type , token):
    #type | 2 --> user token | 1 --> bot token
    match type:
        case 1 | "1":
            token = "Bot " + token

            req = Request(f"{discord_api_base_url}/oauth2/applications/@me")
            req.add_header('Content-Type', 'application/json')
            req.add_header('User-Agent', 'Hooksguide/1.0')
            req.add_header("Authorization" , token)

            try:
                response = urlopen(req)
                bot_info = json.loads(response.read())
                print(bot_info)
                token_info = bot_info["bot"]
                owner_info = bot_info["owner"]
                

                print("Token type: Discord Bot")
                print("======= Bot Info =======")
                print(f"Bot ID: {token_info["id"]}")
                print(f"Bot Username: {token_info["username"].encode('unicode_escape').decode()}#{token_info["discriminator"]}")
                print(f"Bot Description: {bot_info["description"].encode('unicode_escape').decode()}")
                print(f"Profile Picture: https://cdn.discordapp.com/avatars/{token_info["id"]}/{token_info["avatar"]}.png?size=1024")
                print(f"Bot Banner: {token_info["banner"]}")
                print(f"Bot Banner Colour: {token_info["banner_color"]}")
                print(f"Guild Count: {bot_info["approximate_guild_count"]}")
                print(f"User Install Count: {bot_info["approximate_user_install_count"]}")
                print(f"Is verified : {bot_info["is_verified"]}")
                print(f"Is monetized : {bot_info["is_monetized"]}")
                print(f"Is public : {bot_info["bot_public"]}")
                print(f"Requires code grant : {bot_info["bot_require_code_grant"]}")
                print(f"Has a storefront : {bot_info["storefront_available"]}")
                print(f"Redirect URIs: {bot_info["redirect_uris"]}")
                print(f"Verify key: {bot_info["verify_key"]}")
                print("======= Owner Info =======")
                print(f"Owner ID: {owner_info["id"]}")
                print(f"Owner Username: {owner_info["id"].encode('unicode_escape').decode()}")
                print(f"Owner Globalname: {owner_info["id"].encode('unicode_escape').decode()}")
                print(f"Owner PFP: {owner_info["id"]}")
                print(f"Owner Banner: {owner_info["id"]}")
                print(f"Owner Banner Colour: {owner_info["id"]}")
                print(f"Owner PFP Decoration: {owner_info["id"]}")

            except urllib.error.HTTPError as e:
                print("[X] Token is invalid or not a bot token")
                print(f"[X] Error code {e}")
                print("Data recovered from the token itself ...")
                token_id_part = token[4::].split(".")[0].encode() + b'=='
                token_id_part = int(base64.b64decode(token_id_part).decode())
                discord_epoch = 1420070400000
                timestamp = (token_id_part >> 22) + discord_epoch
                creation_time = datetime.datetime.fromtimestamp(timestamp / 1000 , datetime.UTC)
                print("======= Token Info =======")
                print(f"ID: {token_id_part}")
                print(f"Creation time: {creation_time}")
            except:
                print("[X] An unknown error occured")
                print("Data recovered from the token itself ...")
                token_id_part = token[4::].split(".")[0].encode() + b'=='
                token_id_part = int(base64.b64decode(token_id_part).decode())
                discord_epoch = 1420070400000
                timestamp = (token_id_part >> 22) + discord_epoch
                creation_time = datetime.datetime.fromtimestamp(timestamp / 1000 , datetime.UTC)
                print("======= Token Info =======")
                print(f"ID: {token_id_part}")
                print(f"Creation time: {creation_time}")

        case 2 | "2":
            req = Request(f"{discord_api_base_url}/users/@me")
            req.add_header('Content-Type', 'application/json')
            req.add_header('User-Agent', 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36')
            req.add_header("Authorization" , token)

            try:
                response = urlopen(req)
                user_info = json.loads(response.read())
                print("Token type: Discord User")
                print("======= User Info =======")
                print(f"User ID: {user_info["id"]}")
                print(f"Username: {user_info["global_name"].encode('unicode_escape').decode()}")
                print(f"Global Name: {user_info["username"].encode('unicode_escape').decode()}")
                print(f"Profile Picture: https://cdn.discordapp.com/avatars/{user_info["id"]}/{user_info["avatar"]}.png?size=1024")
                print(f"PFP Decoration: {user_info["avatar_decoration_data"]}")
                print(f"Email ID: {user_info["email"]}")
                print(f"Phone number: {user_info["phone"]}")
                print(f"Multifactor enabled: {user_info["mfa_enabled"]}")
                print(f"Email verified: {user_info["verified"]}")
                print(f"Bio: {user_info["bio"].encode('unicode_escape').decode()}")
                print(f"Is 18+ : {user_info["nsfw_allowed"]}")
                print(f"Language: {user_info["locale"]}")
                print(f"Has nitro ?: {user_info["premium_type"]}")
            except urllib.error.HTTPError as e:
                print("[X] Token is invalid or not a user token")
                print(f"[X] Error code {e}")
                print("Data recovered from the token itself ...")
                token_id_part = token.split(".")[0].encode() + b'=='
                token_id_part = int(base64.b64decode(token_id_part).decode())
                discord_epoch = 1420070400000
                timestamp = (token_id_part >> 22) + discord_epoch
                creation_time = datetime.datetime.fromtimestamp(timestamp / 1000 , datetime.UTC)
                print("======= Token Info =======")
                print(f"ID: {token_id_part}")
                print(f"Creation time: {creation_time}")
            except:
                print("[X] An unknown error occured")
                print("Data recovered from the token itself ...")
                token_id_part = token.split(".")[0].encode() + b'=='
                token_id_part = int(base64.b64decode(token_id_part).decode())
                discord_epoch = 1420070400000
                timestamp = (token_id_part >> 22) + discord_epoch
                creation_time = datetime.datetime.fromtimestamp(timestamp / 1000 , datetime.UTC)
                print("======= Token Info =======")
                print(f"ID: {token_id_part}")
                print(f"Creation time: {creation_time}")
        case _:
            print("[X] Did you mess with the code ???")
            quit()


def display_banner():
    print("===============|-| HooksGuide |-|===============")
    print("Discord bot and user token utils")
    print("By: Apollyon\n")

def display_options():
    print("(1)Get info from user token \n(2)Get info from bot token \n(3)Clear screen \n(4)Quit\n")

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear_screen()
display_banner()  
display_options()

while True:
    user_input = input("> ").strip().lower()
    match user_input:
        case "1" | "user" | "user token" | "get info from user token":
            token = input("Enter user token | > ").strip()
            get_token_info(2 , token)
        case "1" | "bot" | "bot token" | "get info from bot token":
            token = input("Enter bot token | > ").strip()
            get_token_info(1 , token)
        case "3" | "clear screen" | "clear" | "cls":
            clear_screen()
            display_banner()  
            display_options()
        case "4" | "quit" | "exit" | "close":
            quit()
        case _:
            print("[X] INVALID OPTION")