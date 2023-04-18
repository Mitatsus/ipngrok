import requests
import socket
import json


def ip():
    """ 
    :return: Domain Gir Lutfen.
    """

    try:
        data = requests.get('http://localhost:4040/api/tunnels')
        unicode = data.content.decode('utf-8')
        gjson = json.loads(unicode)

        do = gjson['tunnels'][0]['public_url']
        do = do.replace('tcp://', '')
        do = do.split(':')
        ipadresi = socket.gethostbyname(str(do[0]))
        ipadresi = f'{ipadresi}:{do[1]}'
        return ipadresi

    except (requests.exceptions.ConnectionError, requests.exceptions.JSONDecodeError):
        return None
