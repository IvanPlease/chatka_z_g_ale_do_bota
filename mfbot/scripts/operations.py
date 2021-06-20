import re

def get_by_id(lst, id):
    for d in lst:
        if d['id'] == id:
            return d
    return None

def get_range(string):
    rg = re.findall('\d+\-\d+|\d+', string);
    ids = []

    for r in rg:
        c = r.split("-")
        print(c)
        if len(c) == 2: 
            for i in range(int(c[0]), int(c[1])+1):
                ids.append(i)
        else:
            ids.append(int(c[0]))

    ids.sort()

    return list(dict.fromkeys(ids))