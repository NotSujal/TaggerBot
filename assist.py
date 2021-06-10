import json,os

verified_tags = "verified_tags"
unverified_tags = "unverified_tags"
tagmanagers = "tagmanagers"
requested_tags = "requested_tags"



def savedata(file, key, value):
    with open(f"{file}.json", 'r') as f:
        data = json.load(f)

    data[key]= value
    with open(f"{file}.json", 'w') as f:
        json.dump(data, f,indent=4, sort_keys=True)


def createdata(file,key):
    if os.path.getsize(f"{file}.json") > 0:
        with open(f"{file}.json", 'r') as f:
            data = json.load(f)
    else:
        data = {}
    data[key] = 0
    with open(f"{file}.json", 'w') as f:
        json.dump(data, f,indent=4, sort_keys=True)


def deletedata(file,key):
    with open(f"{file}.json", 'r') as f:
        data = json.load(f)

    del data[key]
    with open(f"{file}.json", 'w') as f:
        json.dump(data, f,indent=4, sort_keys=True)


def getdata(file,key):
    with open(f"{file}.json", 'r') as f:
        data = json.load(f)

        value = data[key]
    return value

def isTagmanager(user):
    all_current_tagmanagers = getdata(tagmanagers,"list")
    user_is_tagmanager = False
    for a_tagmanager in all_current_tagmanagers:
        if a_tagmanager == user:
            user_is_tagmanager = True
    return user_is_tagmanager
