from .users import user_data
from .arguments import parser
from .language import lang
from uuid import uuid5, NAMESPACE_OID
import subprocess
import os

_ = lang.gettext

accPath = ("%s/../data/mfbot_accounts/") % os.path.dirname(os.path.realpath(__file__))
session_name = "MfBot_%s"

def startbots(ids):
    for id in ids:
        if id < len(user_data["accounts"]) and id > 0:
            userHash = uuid5(NAMESPACE_OID, user_data["accounts"][id-1]["username"])
            sessName = session_name % userHash
            response = subprocess.run(("sudo tmux has-session -t %s" % sessName).split(" "), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if response.returncode == 1:
                subprocess.run(("sudo tmux new-session -d -s %s" % sessName), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                subprocess.run(("sudo tmux send-keys -t %s 'cd %s%s'" % (sessName, accPath, userHash)), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                subprocess.run(("sudo tmux send-keys -t %s ./MFBot_Konsole_ARMRasp" % sessName), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            parser.error(_("Account with given id doesn't exist"))

def stopbots(ids):
    for id in ids:
        if id < len(user_data["accounts"]) and id > 0:
            userHash = uuid5(NAMESPACE_OID, user_data["accounts"][id-1]["username"])
            sessName = session_name % userHash
            response = subprocess.run(("sudo tmux list-sessions").split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(response.stdout)
        else:
            parser.error(_("Account with given id doesn't exist"))