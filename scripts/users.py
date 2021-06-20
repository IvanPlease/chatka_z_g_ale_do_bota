import os
import tarfile
from uuid import uuid5, NAMESPACE_OID
from distutils import util
import json

dirPath = os.path.dirname(os.path.realpath(__file__))
dataPath = f"{dirPath}/../data/"
with open(f"{dirPath}/../data/exp-placeholder.txt", "r") as eC:
    expConf = "".join(eC.readlines())
with open(f"{dirPath}/../data/gold-placeholder.txt", "r") as gC:
    goldConf = "".join(gC.readlines())

def unpack(username, path):
    tar = tarfile.open(f"{dataPath}MfBot_Template.tar", "r:")
    hashName = uuid5(NAMESPACE_OID, username)
    tar.extractall(f"{path}{hashName}")
    tar.close()

def __init__():
    if not os.path.exists(f"{dataPath}mfbot_accounts"):
        os.mkdir(f"{dataPath}mfbot_accounts")

def load_json():
    with open(f"{dirPath}/../data/users.json") as f:
        data = json.load(f)
    return data

def save_json(data):
    with open(f"{dirPath}/../data/users.json", "w") as f:
        json.dump(data, f)
    f.close()

def change_config(row, path):
        ini_append = ""
        if row['type'] == "Gold":
            ini_append = goldConf
        else:
            ini_append = expConf
        hashName = uuid5(NAMESPACE_OID, row['username'])
        ini_append = ini_append.replace("${username}.upper", row['username'].upper()).replace("${username}", row['username']).replace("${server}.upper", row['server'].upper()).replace("${server}", row['server']).replace("${password}", row['password'])
        ini = open(f"{path}{hashName}/Acc.ini", "w")
        ini.write("\n")
        ini.write(ini_append)
        ini.close()

def create_acc_folders(row):
    accPath = f"{dataPath}mfbot_accounts/"
    hashName = uuid5(NAMESPACE_OID, row['username'])
    if not row['disabled']:
        if not os.path.exists(f"{accPath}{hashName}"):
            os.mkdir(f"{accPath}{hashName}")
        if len(os.listdir(f"{accPath}{hashName}")) == 0:
            unpack(row['username'], accPath)
            change_config(row, accPath)

def add_account(username, password, server, type, active):

    if type == None:
        type = "Experience"
    if active == None:
        active = True
    data = {"id": len(user_data["accounts"])+1,
        "server": server,
        "username": username,
        "type": type,
        "password": password,
        "disabled": active}
    
    for a in user_data["accounts"]:
        if a.get("username") == data.get("username") and a.get("server") == data.get("server"):
            break
        else:
            if a.get("id") == len(user_data):
                user_data["accounts"].append(data)

    save_json(user_data)
    
    
def del_account(id):

    for a in user_data["accounts"]:
        if a.get("id") == int(id):
            user_data["accounts"].remove(a)

    for a in user_data["accounts"]:
        if a.get("id") >= int(id):
            a["id"] = a["id"]-1
            user_data["accounts"][a["id"]-1] = a

    save_json(user_data)

def del_account_s(username, server):

    id = 0

    for a in user_data["accounts"]:
        if a.get("username") == username and a.get("server") == server:
            id = a.get("id")
            user_data["accounts"].remove(a)

    for a in user_data["accounts"]:
        if a.get("id") >= int(id):
            a["id"] = a["id"]-1
            user_data["accounts"][a["id"]-1] = a

    save_json(user_data)

def change_account_type(id, type):

    for a in user_data["accounts"]:
        if a.get("id") == int(id):
            a["type"] = type
            user_data["accounts"][a["id"]-1] = a

    save_json(user_data)

def change_account_type_s(username, server, type):

    for a in user_data["accounts"]:
        if a.get("username") == username and a.get("server") == server:
            a["type"] = type
            user_data["accounts"][a["id"]-1] = a

    save_json(user_data)

def change_account_status(id, status):

    for a in user_data["accounts"]:
        if a.get("id") == int(id):
            a["disabled"] = not util.strtobool(status)
            user_data["accounts"][a["id"]-1] = a

    save_json(user_data)

def change_account_status_s(username, server, status):

    for a in user_data["accounts"]:
        if a.get("username") == username and a.get("server") == server:
            a["disabled"] = not util.strtobool(status)
            user_data["accounts"][a["id"]-1] = a

    save_json(user_data)

__init__()

user_data = load_json()