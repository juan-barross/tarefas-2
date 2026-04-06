import requests
import json 

endereco_do_servidor = "http://127.0.0.1:5000/csv"

print("1. Criando banco de dados com 20 filmes")
lista_dos_20_filmes = [
    {"Nome": "A Origem", "Rating": 8.8, "Duração": 148, "Ano": 2010, "Gênero": "Ficção Científica"},
    {"Nome": "O Senhor dos Anéis", "Rating": 9.0, "Duração": 201, "Ano": 2003, "Gênero": "Fantasia"},
    {"Nome": "Vingadores: Ultimato", "Rating": 8.4, "Duração": 181, "Ano": 2019, "Gênero": "Ação"},
    {"Nome": "Matrix", "Rating": 8.7, "Duração": 136, "Ano": 1999, "Gênero": "Ficção Científica"},
    {"Nome": "O Poderoso Chefão", "Rating": 9.2, "Duração": 175, "Ano": 1972, "Gênero": "Crime"},
    {"Nome": "Interestelar", "Rating": 8.6, "Duração": 169, "Ano": 2014, "Gênero": "Ficção Científica"},
    {"Nome": "Gladiador", "Rating": 8.5, "Duração": 155, "Ano": 2000, "Gênero": "Ação"},
    {"Nome": "Parasita", "Rating": 8.5, "Duração": 132, "Ano": 2019, "Gênero": "Suspense"},
    {"Nome": "O Cavaleiro das Trevas", "Rating": 9.0, "Duração": 152, "Ano": 2008, "Gênero": "Ação"},
    {"Nome": "Forrest Gump", "Rating": 8.8, "Duração": 142, "Ano": 1994, "Gênero": "Drama"},
    {"Nome": "Cidade de Deus", "Rating": 8.6, "Duração": 130, "Ano": 2002, "Gênero": "Crime"},
    {"Nome": "O Rei Leão", "Rating": 8.5, "Duração": 89, "Ano": 1994, "Gênero": "Animação"},
    {"Nome": "De Volta para o Futuro", "Rating": 8.5, "Duração": 116, "Ano": 1985, "Gênero": "Aventura"},
    {"Nome": "Clube da Luta", "Rating": 8.8, "Duração": 139, "Ano": 1999, "Gênero": "Drama"},
    {"Nome": "Pulp Fiction", "Rating": 8.9, "Duração": 154, "Ano": 1994, "Gênero": "Crime"},
    {"Nome": "Toy Story", "Rating": 8.3, "Duração": 81, "Ano": 1995, "Gênero": "Animação"},
    {"Nome": "A Viagem de Chihiro", "Rating": 8.6, "Duração": 125, "Ano": 2001, "Gênero": "Animação"},
    {"Nome": "Jurassic Park", "Rating": 8.2, "Duração": 127, "Ano": 1993, "Gênero": "Aventura"},
    {"Nome": "O Iluminado", "Rating": 8.4, "Duração": 146, "Ano": 1980, "Gênero": "Terror"},
    {"Nome": "Alien", "Rating": 8.5, "Duração": 117, "Ano": 1979, "Gênero": "Ficção Científica"}
]
resposta_do_servidor_ao_criar = requests.post(endereco_do_servidor, json=lista_dos_20_filmes)
print(resposta_do_servidor_ao_criar.text, "\n") 

print("2. Adicionando filmes extras...")
lista_de_filmes_extras = [
    {"Nome": "O Exterminador do Futuro 2", "Rating": 8.5, "Duração": 137, "Ano": 1991, "Gênero": "Ação"},
    {"Nome": "Shrek", "Rating": 7.9, "Duração": 90, "Ano": 2001, "Gênero": "Animação"}
]
resposta_do_servidor_ao_editar = requests.put(endereco_do_servidor, json=lista_de_filmes_extras)
print(resposta_do_servidor_ao_editar.text, "\n") 

print("3. Lendo o Top 3 da nossa lista...")
informacoes_do_corte = {"linha_inicial": 0, "linha_final": 3}
resposta_da_leitura_do_pedaco = requests.post(f"{endereco_do_servidor}/intervalo", json=informacoes_do_corte)

dados_do_pedaco = resposta_da_leitura_do_pedaco.json()
print(json.dumps(dados_do_pedaco, indent=4, ensure_ascii=False), "\n")

print("4. Filtrando filmes com menos de 100 minutos...")
informacoes_do_filtro = {"coluna": "Duração", "valor": 100}
resposta_do_filtro = requests.post(f"{endereco_do_servidor}/filtro", json=informacoes_do_filtro)

dados_do_filtro = resposta_do_filtro.json()
print(json.dumps(dados_do_filtro, indent=4, ensure_ascii=False), "\n")

print("5. Resumo estatístico do catálogo...")
resposta_das_estatisticas = requests.get(f"{endereco_do_servidor}/estatisticas")

dados_das_estatisticas = resposta_das_estatisticas.json()
print(json.dumps(dados_das_estatisticas, indent=4, ensure_ascii=False), "\n")
