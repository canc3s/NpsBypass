"""
Usage:

    mitmproxy -s npsbypass.py
"""
from mitmproxy import ctx
import hashlib
import time

def gen_authkey(time=int(time.time())):
    mdf = hashlib.md5()
    mdf.update(str(time).encode("utf8"))
    auth_key = mdf.hexdigest()
    return auth_key

class NpsBypass:
    def __init__(self):
        self.num = 0

    def request(self, flow):
        self.num = self.num + 1
        now = int(time.time())
        flow.request.query["auth_key"] = gen_authkey(now)
        flow.request.query["timestamp"] = str(now)

addons = [NpsBypass()]
