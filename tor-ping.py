import requests
import time
from stem import Signal
from stem.control import Controller

x=0
def renew_connection():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="QWER1234asdf")
        controller.signal(Signal.NEWNYM)
def get_tor_session():
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http': 'socks5://127.0.0.1:9050',
                           'https': 'socks5://127.0.0.1:9050'}
    return session

while True:
    session = get_tor_session()
    session.get("https://vigneshnin.wordpress.com")
    x=x+1
    print(x)
    time.sleep(5)
    renew_connection()


