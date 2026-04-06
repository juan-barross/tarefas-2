**Sistema para gerenciamento de dados de filmes via API REST utilizando Flask para o servidor e Pandas para manipulação de arquivos CSV.**

**Arquitetura**

O projeto é dividido em dois scripts:

    main.py (Servidor): Processa requisições HTTP e gerencia o arquivo dados.csv.

    cliente.py (Cliente): Realiza chamadas para testar as funcionalidades da API.

**Requisitos de Instalação**

O projeto utiliza um ambiente virtual. Para instalar as dependências exatas, utilize o arquivo requirements.txt.

    Crie e ative o ambiente virtual:

        Windows: python -m venv venv e venv\Scripts\activate

        Linux/Mac: python -m venv venv e source venv/bin/activate

    Instale as bibliotecas:
    Bash

    pip install -r requirements.txt

**Como Executar**

    Inicie o servidor:
    Bash

    python main.py

    Em outro terminal, execute o cliente:
    Bash

    python cliente.py
    
