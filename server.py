from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Texto(Resource):
    def post(self):
        #Pega o texto recebido e insere em data
        data = request.json['data']
        #cria um array, quebrando o texto por meio dos espaços
        palavras=data.split(" ")
        #cria um array vazio
        result=[]
        #para cada item dentro do array palavras, insere no array result uma cor, o item e o significado
        for x in palavras:
            result.append(dict(palavras=x,cor="blue",significado="banana"))

        #retorna os dados em json
        return jsonify(result)



api.add_resource(Texto, '/texto') 

if __name__ == '__main__':
    app.run()

