import re

class Regex:
    SCRIPT = re.compile("AF_initDataCallback[\s\S]*?<\/script")
    KEY = re.compile("(ds:.*?)'")
    VALUE = re.compile("data:([\s\S]*?), sideChannel: {}}\);<\/")