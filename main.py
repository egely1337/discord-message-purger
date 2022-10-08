from curses import COLOR_GREEN
import json

from numpy import append
from util.discord import get_discord_messages, DMessage, parse_discord_messages,delete_discord_message
from time import sleep
from colorama import * 

cannotDeleted = []
config = json.load(open("./config.json"))
count = 0
sleepc = 1

while count < config["purge_message_count"]:
    messages = get_discord_messages(token=config["token"],cid=config["cid"])
    dList = parse_discord_messages(messages=messages,uid=config["uid"])
    print("{}Requested {} messages!".format(Fore.GREEN,len(dList)))
    for i in dList:
        if count > config["purge_message_count"]: break
        s = delete_discord_message(token=config["token"], \
            cid=config["cid"]\
            , id=i.id)
        if s == True: 
            print("{}[{}] Deleted message: {}".format(Fore.GREEN,count,i.id))
            count = (count + 1)
        if s == False: 
            print("{}[{}] Cannot delete message: {}".format(Fore.RED,count,i.id))
            cannotDeleted.append(i)
        sleep(1)
    while len(cannotDeleted) != 0:
        for i in cannotDeleted:
            if count > config["purge_message_count"]: break
            s = delete_discord_message(token=config["token"], \
                cid=config["cid"]\
                , id=i.id)
            if s == True: 
                print("{}[{}] Deleted message: {}".format(Fore.GREEN,count,i.id))
                count = (count + 1)
                cannotDeleted.remove(i)
            if s == False: 
                print("{}[{}] Cannot delete message: {}".format(Fore.RED,count,i.id))
                sleep(30)



