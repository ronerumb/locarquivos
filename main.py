import os
from funcoes import formata_tamanho

caminho_procura = input('Digite um caminho')
termo_procura = input('Digite um termo')
contador = 0
for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                contador +=1
                caminho_completo = os.path.join(raiz,arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)
                print()
                print('Encontrei o arquivo : ',arquivo)
                print('Caminho :',caminho_completo)
                print('Nome do arquivo :',nome_arquivo)
                print('Extensão :',ext_arquivo)
                print('Tamanho :', tamanho)
                print('Tamanho formatado:', formata_tamanho(tamanho))
            except FileNotFoundError as e:
                print('Arquivo não encontrado')

print('Foram encontrados ',contador,' Arquivos')



