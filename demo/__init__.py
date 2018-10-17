from flask import Flask, render_template, request, session
import time, random

app = Flask(__name__)
app.secret_key = \
    'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

CIPHER_BOOK = {
    '0': '\uE800',
    '1': '\uE801',
    '2': '\uE802',
    '3': '\uE803',
    '4': '\uE804',
    '5': '\uE805',
    '6': '\uE806',
    '7': '\uE807',
    '8': '\uE808',
    '9': '\uE809'
}


def _encrypt_secret(secret):
    return ''.join(CIPHER_BOOK[c] for c in secret)


@app.route('/')
def index():
    if 'guess' in request.values:
        ts = session['ts'] if 'ts' in session else 0
        secret = session['secret'] if 'secret' in session else None
        if time.time() - ts < 2 and request.values['guess'] == secret:
            return render_template('index.html', success=True)
    secret = ''.join([random.choice('0123456789') for _ in range(20)])
    s = _encrypt_secret(secret)
    session['secret'] = secret
    session['ts'] = time.time()
    return render_template("index.html", string=s)


if __name__ == '__main__':
    app.run(port=5000)
