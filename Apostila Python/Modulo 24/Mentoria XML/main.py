import xmltodict


def ler_xml_danfe(nota):
    with open(nota, 'rb') as arquivo:
        documento = xmltodict.parse(arquivo)

    dic_notafical = documento['nfeProc']['NFe']['infNFe']
    valor_total = dic_notafical['total']['ICMSTot']['vNF']
    cnpj_vendeu = dic_notafical['emit']['CNPJ']
    nome_vendeu = dic_notafical['emit']['xNome']
    cpf_comprou = dic_notafical['dest']['CPF']
    nome_comprou = dic_notafical['dest']['xNome']
    produtos = dic_notafical['det']
    lista_produtos = []

    for produto in produtos:
        valor_produto = produto['prod']['vProd']
        nome_produto = produto['prod']['xProd']
        lista_produtos.append((nome_produto, valor_produto))

    resposta ={
        'Valor Total': [valor_total],
        'CNPJ do Vendedor': [cnpj_vendeu],
        'Nome do Vendedor': [nome_vendeu],
        'CPF do Comprador': [cpf_comprou],
        'Nome do Comprador': [nome_comprou],
        'lista_produtos': [lista_produtos]
    }

    return resposta


def ler_xml_servico(nota):
    with open(nota, 'rb') as arquivo:
        documento = xmltodict.parse(arquivo)

    dic_notafical = documento['ConsultarNfseResposta']['ListaNfse']['CompNfse']['Nfse']['InfNfse']
    
    valor_total = dic_notafical['Servico']['Valores']['ValorServicos']
    cnpj_vendeu = dic_notafical['PrestadorServico']['IdentificacaoPrestador']['Cnpj']
    nome_vendeu = dic_notafical['PrestadorServico']['RazaoSocial']
    cpf_comprou = dic_notafical['TomadorServico']['IdentificacaoTomador']['CpfCnpj']['Cnpj']
    nome_comprou = dic_notafical['TomadorServico']['RazaoSocial']
    produtos = dic_notafical['Servico']['Discriminacao']
    
    resposta ={
        'Valor Total': [valor_total],
        'CNPJ do Vendedor': [cnpj_vendeu],
        'Nome do Vendedor': [nome_vendeu],
        'CPF do Comprador': [cpf_comprou],
        'Nome do Comprador': [nome_comprou],
        'lista_produtos': [produtos],
    }

    return resposta

import os

lista_arquivos = os.listdir(r'NFS Finais')

for arquivo in lista_arquivos:
    if 'xml' in arquivo:
        if 'DANFE' in arquivo:
            print(ler_xml_danfe(os.path.join(r'NFS Finais', arquivo)))
        else:
            print(ler_xml_servico(os.path.join(r'NFs Finais', arquivo)))
            


#import pandas as pd

#tabela = pd.DataFrame.from_dict(resposta)
#tabela.to_excel('resposta.xlsx', index=False)