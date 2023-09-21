from googleplay.errors import GooglePatternError

def pattern(json, pattern):
    try:
        for p in pattern:
            json = json[p]
        return json
    except (IndexError, KeyError):
        raise GooglePatternError(f"incorrect pattern")

def name(json):
    return pattern(json, [0, 0])

def created_at(json):
    return pattern(json, [3, 0])

def downloads(json):
    return pattern(json, [4, 2])

def purchases(json):
    return pattern(json, [6, 0]).replace(" per item", "")

def rating(json):
    return pattern(json, [9, 0, 1])

def reviews(json):
    return pattern(json, [9, 2, 1])

def website(json):
    return pattern(json, [12, 0, -1, -1])

def email(json):
    return pattern(json, [12, 1, 0])

def address(json):
    return pattern(json, [12, 2, 0])

def description(json):
    return pattern(json, [13, 0, 1])

def id(json):
    return pattern(json, [16, 0])

def screenshots(json):
    return pattern(json, [17])

def category(json):
    return pattern(json, [18, 0, 0, 0])

def icon(json):
    return pattern(json, [20, 0, 3, 2])

def banner(json):
    return pattern(json, [21, 0, 3, 2])

def version(json):
    return pattern(json, [26, 0, 0, 0])