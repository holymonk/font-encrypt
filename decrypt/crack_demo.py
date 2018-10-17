import requests
from bs4 import BeautifulSoup as BS

CIPHER_BOOK = {
    '\ue800': '0',
    '\ue801': '1',
    '\ue802': '2',
    '\ue803': '3',
    '\ue804': '4',
    '\ue805': '5',
    '\ue806': '6',
    '\ue807': '7',
    '\ue808': '8',
    '\ue809': '9'
}
URL = 'http://127.0.0.1:5000'

sess = requests.Session()
resp = sess.get(URL).text
bs = BS(resp, 'lxml')
string = bs.select_one('.demo-icon b').text
guess = ''.join(CIPHER_BOOK[c] if c in CIPHER_BOOK else c
                for c in string)
print('guess:', guess)
resp = sess.get(URL, params={'guess': guess}).text
assert 'Congratulations' in resp
