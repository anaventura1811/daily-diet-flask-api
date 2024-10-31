from flask import Flask, request, jsonify
from database import db

'''
  Regras da aplicação
    1. Deve ser possível registrar uma refeição feita,
    com as seguintes informações:
      - Nome
      - Descrição
      - Data e hora
      - Está dentro ou não da dieta
    2. Deve ser possível editar uma refeição,
    podendo alterar todos os dados acima
    3. Deve ser possível apagar uma refeição
    4. Deve ser possível listar todas as refeições de um usuário
    5. Deve ser possível visualizar uma única refeição
    6. As informações devem ser salvas em um banco de dados
'''
