from flask import Flask, Response, request
import requests
import hashlib
import redis
import html

app = Flask(__name__)
cache = redis.StrictRedis(host='redis', port=6379, db=0)
salt = "UNIQUE_SALT"
default_name = 'Joe Bloggs'

@app.route('/', methods=['GET', 'POST'])
def main_page():
    name = default_name
    name_hash = hashlib.sha256((salt + name).encode()).hexdigest()  # 初期化を追加
    if request.method == 'POST':
        name = html.escape(request.form['name'], quote=True)
        salted_name = salt + name
        name_hash = hashlib.sha256(salted_name.encode()).hexdigest()

    header = '<html><head><title>IdentiDock</title></head><body>'
    body = '''<form method="POST">
                Hello <input type="text" name="name" value="{}">
                <input type="submit" value="submit">
                </form>
                <p>You look like a:
                <img src="/monster/{}"/>
                '''.format(name, name_hash)
    footer = '</body></html>'

    return header + body + footer

@app.route('/monster/<name>')
def get_monster(name):
    image = cache.get(name)
    if image is None:
        print("Cache miss", flush=True)
        r = requests.get('http://dnmonster:8
