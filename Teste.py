#Import das dependencias do Flask
from flask import Flask, request, make_response, jsonify
#Inicializa a app do flash
app = Flask(__name__)
#Rota default
@app.route('/')
def index():
  return 'Hello World'
#Funcao de Respostas
def results():
  #Constroi o objeto de respostas
  req=request.get_json(force=True)
  #Pega a acao do json
  action=req.get('queryResult').get('action')
  #retorna o fulfillment do response
  return {'fulfillmentText': 'This is a response from webhook.'}
# cria uma rota para o webhook
@app.route('/webhook', methods=['GET','POST'])
def webhook():
  #retorno da resposta
  return make_response(jsonify(results()))
#Executa a aplicacao
if __name__=='__main__':
   app.run(host='0.0.0.0',port=5000)
