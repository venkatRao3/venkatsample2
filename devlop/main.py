import requests


def call_pylenin(events=None,context=None):
    r = requests.get("https://www.pylenin.com")
    if r.status_code == 200:
        print("it is successful!")
call_pylenin()


