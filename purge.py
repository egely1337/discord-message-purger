from requests import *
from json import *
from time import sleep
from hcfg import *

db = hcfgdb('config.hcfg')
id = input('Enter the ID : ')
url = f'https://discord.com/api/v9/channels/{id}/messages'
author = db.getValue('author')

header = {
    "authorization" : db.getValue('token')
}

def getMessages(id):
    jsonObject = get(url=url,headers=header)
    object = loads(jsonObject.content)
    return object


def deleteMessages(id):
    obj = getMessages(id)
    ids = []
    message = []
    count = 0
    for object in obj:
        if int(object['author']['id']) == int(author):
            ids.append(object['id'])
            message.append(object['content'])
    for i in ids:
        try:
            count += 1
            sleep(0.5)
            deleteUrl = f"https://discord.com/api/v9/channels/{id}/messages/{i}"
            delete(url=deleteUrl,headers=header)
            print(f'MESSAGE: {message[count]} : ID: {i} HAS DELETED')
        except:
            print("Finished")
    


if __name__ == "__main__":
    deleteMessages(id)
    