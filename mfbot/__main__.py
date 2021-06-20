from mfbot import *

_ = lang.gettext

if __name__ == "__main__":

    if not args.on_range == None:
        startbots(get_range(args.on_range))
    if not args.off_range == None:
        stopbots(get_range(args.off_range))
    if args.add:
        if not args.username == None and not args.password == None and not args.server == None:
            add_account(args.username, args.password, args.server, args.type, args.status)
        else:
            parser.error(_("You need to specify -u USERNAME, -p PASSWORD and -se SERVER to add a account"))
    if args.delete:
        if not args.id == None:
            del_account(args.id)
        elif not args.username == None and not args.sever == None:
            del_account_s(args.username, args.server)
        else:
            parser.error(_("You need to specify -i ID or -u USERNAME and -se SERVER to delete a account"))
    if args.change:
        if not args.id == None:
            change_account_type(args.id, args.type)
        elif not args.username == None and not args.sever == None:
            change_account_type_s(args.username, args.server, args.type)
        else:
            parser.error(_("You need to specify -i ID or -u USERNAME and -se SERVER to change account type"))
    if args.status:
        if not args.id == None:
            change_account_status(args.id, args.active)
        elif not args.username == None and not args.sever == None:
            change_account_status_s(args.username, args.server, args.active)
        else:
            parser.error(_("You need to specify -i ID or -u USERNAME and -se SERVER to disable or enable a account"))