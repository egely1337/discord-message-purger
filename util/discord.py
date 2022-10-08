from requests import get,post,delete

DEBUG = 1

status_codes = {
    "success" : "204",
    "error" : "429"
}

class DMessage:
    def __init__(self,id) -> None:
        self.id = id



discord_api = {
    "DISCORD_GET_MESSAGES" : "https://discord.com/api/v9/channels/{}/messages?limit=50",
    "DISCORD_DELETE_MESSAGE" : "https://discord.com/api/v9/channels/{}/messages/{}"
}



def get_discord_messages(token,cid) -> dict:
    auth = {"authorization" : token,\
    "User-Agent" : "Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320"}
    messages = get(url=discord_api["DISCORD_GET_MESSAGES"].format(cid),headers=auth)
    return messages.json()

def delete_discord_message(token,cid,id) -> bool:
    auth = {"authorization" : token,\
        "User-Agent" : "Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320"}
    s = delete(url=discord_api["DISCORD_DELETE_MESSAGE"].format(cid,id)\
        ,headers=auth)
    if DEBUG == 0: print(s.status_code)
    if s.status_code == int(status_codes["success"]): 
        return True 
    else:
        return False



def parse_discord_messages(messages,uid) -> list:
    dList = []
    for i in range(len(messages)):
        if messages[i]["author"]["id"] == uid: dList.append(DMessage(messages[i]["id"]))
    return dList