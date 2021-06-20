import argparse
from .language import lang

argparse._ = lang.gettext
argparse.ngettext = lang.gettext

parser = argparse.ArgumentParser(prog="mfbot")

control = parser.add_argument_group(argparse._('program controls'))
control.add_argument("-r", "--run", dest="on_range", help=argparse._("run bots for accounts with given ids"))
control.add_argument("-s", "--stop", dest="off_range", help=argparse._("stop bots for accounts with given ids"))

account = parser.add_argument_group(argparse._('account controls'))
account.add_argument("-a", "--add", action='store_true', help=argparse._("add account to existing list"))
account.add_argument("-d", "--delete", action='store_true', help=argparse._("delete account to existing list"))
account.add_argument("-c", "--change", action='store_true', help=argparse._("change account type"))
account.add_argument("-st", "--status", action='store_true', help=argparse._("change account status"))
account.add_argument("-u", "--username", dest="username", help=argparse.SUPPRESS)
account.add_argument("-p", "--password", dest="password", help=argparse.SUPPRESS)
account.add_argument("-se", "--server", dest="server", help=argparse.SUPPRESS)
account.add_argument("-i", "--identifier", dest="id", help=argparse.SUPPRESS)
account.add_argument("-t", "--type", dest="type", choices=["Experience", "Gold"], help=argparse.SUPPRESS)
account.add_argument("-ac", "--active", dest="active", choices=['True', 'False'], help=argparse.SUPPRESS)

args = parser.parse_args()