from art.art import line
from discord_webhook import *
from colorama import init
from termcolor import colored
from art import *

init()

tprint("Discord - Webhook")

url = input("Webhook URL >>> ")
print(colored('Webhook succesfully linked!', 'green'))
print(colored('---', 'grey'))
print(colored('[1] Send message', 'blue'))
print(colored('[2] Send embed', 'blue'))
print(colored('[3] Log out', 'red'))
print(colored('---', 'grey'))

menu = int(input(">>> "))

if menu == 1:
    print(colored('---', 'grey'))
    msg = input('Message >>> ')
    webhook = DiscordWebhook(url=url, content=msg)
    print(colored('Message succesfully sent!', 'green'))
if menu == 2:
    print(colored('---', 'grey'))
    title = input("Title >>> ")
    desc = input("Description >>> ")
    color = input("Color (Hex without #) >>> ")
    webhook = DiscordWebhook(url=url)
    embed = DiscordEmbed(title=title, description=desc, color=color)
    webhook.add_embed(embed)
if menu == 3:
    print(colored('---', 'grey'))
    print(colored('Succesfully logged out!', 'green'))
elif menu >= 3 or menu <= 0:
    print(colored('---', 'grey'))
    print(colored("Gebe eine Zahl zwischen 1 und 2 ein!", 'red'))

response = webhook.execute()


