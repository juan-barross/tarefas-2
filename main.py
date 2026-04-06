from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

nome_do_banco_de_dados = "dados.csv"

@app.route('/csv', methods=['POST'])
def cria():
    filmes_recebidos = request.json
    
    tabela_nova = pd.DataFrame(filmes_recebidos) 
    tabela_nova.to_csv(nome_do_banco_de_dados, index=False)
    
    return "Criou o arquivo"


@app.route('/csv', methods=['PUT'])
def edita():
    filmes_novos_recebidos = request.json
    
    tabela_antiga = pd.read_csv(nome_do_banco_de_dados)
    
    tabela_de_acrescimo = pd.DataFrame(filmes_novos_recebidos)
    
    tabela_juntada = pd.concat([tabela_antiga, tabela_de_acrescimo]) 
    tabela_juntada.to_csv(nome_do_banco_de_dados, index=False)
    
    return "Editou o arquivo"


@app.route('/csv/intervalo', methods=['POST'])
def ler_linhas():
    regras_de_corte = request.json
    linha_de_inicio = regras_de_corte['linha_inicial']
    linha_de_fim = regras_de_corte['linha_final']
    
    tabela_completa = pd.read_csv(nome_do_banco_de_dados)
    pedaco_cortado = tabela_completa.iloc[linha_de_inicio : linha_de_fim]
    
    return jsonify(pedaco_cortado.to_dict('records'))


@app.route('/csv/filtro', methods=['POST'])
def filtro():
    regras_do_filtro = request.json
    nome_da_coluna = regras_do_filtro['coluna']
    valor_limite = regras_do_filtro['valor']
    
    tabela_completa = pd.read_csv(nome_do_banco_de_dados)
    tabela_filtrada = tabela_completa[ tabela_completa[nome_da_coluna] < valor_limite ]
    
    return jsonify(tabela_filtrada.to_dict('records'))


@app.route('/csv/estatisticas', methods=['GET'])
def stats():
    tabela_completa = pd.read_csv(nome_do_banco_de_dados)
    resumo_matematico = tabela_completa.describe()
    
    return jsonify(resumo_matematico.to_dict())

if __name__ == '__main__':
    app.run(port=5000)