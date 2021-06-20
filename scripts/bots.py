from .users import user_data, create_acc_folders
from .arguments import parser
from .language import lang
from uuid import uuid5, NAMESPACE_OID
import subprocess
import time
import os

_ = lang.gettext
dirPath = os.path.dirname(os.path.realpath(__file__))
accPath = (f"{dirPath}/../data/mfbot_accounts/")

def startbots(ids):
    for id in ids:
        print(user_data["accounts"][id-1])
        create_acc_folders(user_data["accounts"][id-1])
        if id < len(user_data["accounts"]) and id > 0:
            userHash = uuid5(NAMESPACE_OID, user_data["accounts"][id-1]["username"])
            sessName = f"MfBot-{userHash}"
            response = subprocess.run(f"sudo tmux has-session -t {sessName}".split(" "), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if response.returncode == 1:
                subprocess.run(f"sudo tmux new-session -d -s {sessName}".split(" "), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                subprocess.run(["sudo","tmux","send-keys","-t",f"{sessName}","cd ",f"{accPath}",f"{userHash}","C-m"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                subprocess.run(f"sudo tmux send-keys -t {sessName} ./MFBot_Konsole_ARMRasp C-m".split(" "), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                time.sleep(1)
        else:
            parser.error(_("Account with given id doesn't exist"))

def stopbots(ids):
    for id in ids:
        if id < len(user_data["accounts"]) and id > 0:
            userHash = uuid5(NAMESPACE_OID, user_data["accounts"][id-1]["username"])
            sessName = f"MfBot-{userHash}"
            response = subprocess.run(("sudo tmux list-sessions").split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            sessions = response.stdout.decode("utf-8").split("\n")
            sessions.pop()
            for s in sessions:
                if s.split(":")[0] == sessName:
                    subprocess.run((f"sudo tmux kill-session -t {sessName}").split(" "), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            parser.error(_("Account with given id doesn't exist"))