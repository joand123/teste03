from flask import Flask
from waitress import serve
from flask import render_template
from flask import request,url_for,redirect,flash,session
import logging

app = Flask(__name__)

logging.basicConfig(filename='/flask/app.log', filemode='w', format='%(asctime)s %(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)

@app.route('/')
def root():
    app.logger.debug(‘acesso a página principal’)
    return ("Ola mundo!")

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=80, url_prefix='/app')
    
@app.route('/cadastrar_chave')
def cadastrar_chave():
   return ("Em implementacao")

@app.route('/listar_chaves')
def listar_chaves():
   return ("Em implementacao")


