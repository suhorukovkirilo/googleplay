from urllib.error import HTTPError, URLError
from http.client import InvalidURL

class GooglePatternError(Exception):
    pass