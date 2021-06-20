import re

def get_by_id(lst, id):
    for d in lst:
        if d['id'] == id:
            return d
    return None

def get_range(string):
    rg = re.findall('\d\-\d|\d+', string);
    ids = []

    for r in rg:
        if len(r)==3: 
            for i in range(int(r[0]), int(r[2])+1):
                ids.append(i)
        else:
            ids.append(int(r))

    ids.sort()

    return list(dict.fromkeys(ids))