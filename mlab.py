import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds163034.mlab.com:63034/gamingweb

host = "ds163034.mlab.com"
port = 63034
db_name = "gamingweb"
user_name = "gamingwebuser"
password = "badmeets3vil"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
