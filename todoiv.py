from ast import If
from itertools import count
from msvcrt import kbhit
import re

#declaração de variaveis 
quantidade_curriculos= {}
count_analista = 0
count_cientista = 0
count_analista_match= 0
count_cientista_match= 0
id = 1
lista_dict = []
opcao = True

# Dicionário com requisitos 
requisitos ={
    'analista de dados': ['python', 'powerbi', 'sql', 'boa comunicação'],
    'cientista de dados' : ['python', 'banco de dados', 'machine learning', 'resolução de problemas'], 
}

print('Bem vindo ao Contratando Resilia!!!\n')

while opcao:
    print('~'*100)
    opcao = int(input('[1] Adicionar candidato\n[2]Fazer comparação\nDigite a opção desejada : '))
    print('~'*100)
    # Recebendo o nome do candidado

    if opcao == 1:
        quantidade_curriculos= {}
        nome_canditado = input('Digite o nome do candidato :').lower()

        #Rebebendo a  vaga para que esse cargo esta se candidatando 
        vaga_candidato = input('Digite a vaga para qual esta se inscrevendo :').lower()

        #Dicionáriio relacionando nome e vaga
        quantidade_curriculos['nome']= nome_canditado
        quantidade_curriculos['vaga']= vaga_candidato

        #cria um arquivo .txt com o nome e id do usuário
        arquivo_candidato = open( nome_canditado +str(id) + '.txt','w')
        #insere um conteudo dentro do .txt criado acima
        arquivo_candidato.write(input('Digite um pequeno texto com o resumo do currículo :'))
        arquivo_candidato= open(nome_canditado + str(id) + '.txt','r', encoding="utf8")
        # Faz a contagem do id para duferenciar arquivos caso possuam candidatos com o mesmmo nome
        
        with open(nome_canditado +str(id) + '.txt', 'r') as arquivo: # abrindo o arquivo com modo de leitura
            conteudo_curriculo = arquivo.readlines() 

    # concatena o resumo,tranformando quebras de linhas em espaços
        concatena_string = ''
        for valor in conteudo_curriculo:
            concatena_string = concatena_string + valor.replace('\n','') 

        quantidade_curriculos['resumo']= concatena_string  # insere o resumo no dicionário quantidade curriculos
            # lista dic seria a lista com o resumo concatenado
        lista_dict.append(quantidade_curriculos) # cria um dicionário de listas
        
        id+=1
    if opcao == 2:  
            opcao = False

# lista dic seria a lista com o resumo concatenado
for chave, valor in enumerate(lista_dict):
    count = 0
    #concatena string possue o valor das chaves resumo
    concatena_string = valor.get('resumo')
    
    if valor['vaga']== 'analista de dados':
        print(concatena_string)
        for requisito in requisitos['analista de dados']:
            if requisito in concatena_string:
                count_analista = count_analista + 1 # conta os requisitos
        if count_analista > 0:
        # conta quem tem mais de um requisito e soma
            count_analista_match = count_analista_match + 1
            print('~'*100)

    if valor['vaga']== 'cientista de dados':
        print(concatena_string)
        for requisito in requisitos['cientista de dados']:
            if requisito in concatena_string:
                count_cientista = count_cientista + 1 # conta os requisitos
        if count_cientista > 0:
        # conta quem tem mais de um requisito e soma
            count_cientista_match = count_cientista_match + 1
            print('~'*100)

print(f'{count_cientista_match} cientista(s) de dados que possuem os requisito os requisitos minimos')
print(f'{count_analista_match} analista(s) de dados que possuem os requisito os requisitos minimos ')

