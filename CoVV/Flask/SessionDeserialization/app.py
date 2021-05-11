import os
import pickle

from base64 import b64decode
from flask import Flask, request, render_template, session
import os

app = Flask(__name__)

# add secret key to enable session
# and this is a fake secret key, just an example
app.config['SECRET_KEY'] = os.environ.get('secret_key', 'CTFHUBCTFHUBCTFHUB')

print(app.config['SECRET_KEY'])

User = type('User', (object,), {
    'uname': 'test',
    'is_admin': 0,
    '__repr__': lambda o: o.uname,
})


@app.route('/', methods=('GET',))
def index_handler():
    if not session.get('u'):
        u = pickle.dumps(User())
        session['u'] = u
    return "/file?file=index.js"

# def index_handler():
#     if not session.get('u'):
#         u = pickle.dumps(User())
#         session['u'] = u
#     return render_template('index.html')


@app.route('/file', methods=('GET',))
def file_handler():
    path = request.args.get('file')
    path = os.path.join('static', path)
    # ctfhub fix docker environ
    if path == '/proc/self/environ':
        return 'TERM=xtermPATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/binLANG=C.UTF-8secret_key=you_find_secret_key_congratulationsPYTHON_VERSION=3.6.10FLAG=not_flag'
    # ctfhub fix docker environ end
    if not os.path.exists(path) or os.path.isdir(path) \
            or '.py' in path or '.sh' in path or '..' in path or "flag" in path:
        return 'disallowed'

    with open(path, 'r') as fp:
        content = fp.read()
    return content


@app.route('/admin', methods=('GET',))
def admin_handler():
    try:
        u = session.get('u')
        if isinstance(u, dict):
            u = b64decode(u.get('b'))
        u = pickle.loads(u)
        if u.is_admin == 1:
            return 'welcome, admin'
        else:
            return 'who are you?'
    except Exception as e:
        print(e)
        return 'uhh?'


if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=False)