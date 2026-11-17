import os, secrets
from flask import Flask, request, Response, send_from_directory
app = Flask(__name__)
@app.before_request
def protect():
    user=os.environ.get('APP_USERNAME','fontanges'); password=os.environ.get('APP_PASSWORD','')
    if not password: return 'Configuration APP_PASSWORD manquante',503
    auth=request.authorization
    if not auth or not secrets.compare_digest(auth.username or '',user) or not secrets.compare_digest(auth.password or '',password):
        return Response('Identification requise',401,{'WWW-Authenticate':'Basic realm="Fontanges", charset="UTF-8"'})
@app.after_request
def headers(response):
    response.headers['Cache-Control']='no-store'
    response.headers['X-Content-Type-Options']='nosniff'
    response.headers['X-Frame-Options']='DENY'
    return response
@app.get('/')
def home(): return send_from_directory('templates','index.html')
@app.get('/ordinateur')
def desktop(): return send_from_directory('templates','ordinateur.html')
@app.get('/mobile')
def mobile(): return send_from_directory('templates','mobile.html')
