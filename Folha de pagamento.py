def print_tabela_folha(chave, valor):
    nome, cod_funcao, faltas, bruto = valor
    print(f'''
FOLHA DE PAGAMENTO DE {nome}:
==================================================
Matrícula: {chave}
Código da função: {cod_funcao}
Numero de faltas: {faltas}
Salário bruto: R$ {bruto:.2f}
Imposto: {imposto(bruto)}%
Salário líquido: R$ {liquido(bruto, faltas, imposto(bruto)):.2f}
===================================================''')
#
def print_tabela_relatorio(chave, valor):
    nome, cod_funcao, faltas, bruto = valor
    print(f'''
===================================================
Matrícula: {chave}
Nome: {nome}
Código da função: {cod_funcao}
Salário bruto: R$ {bruto:.2f}
Salário líquido: R$ {liquido(bruto, faltas, imposto(bruto)):.2f}
===================================================''')
#      
def print_tabela_maior_salario(chave, valor):
    nome, cod_funcao, faltas, bruto = valor
    print(f'''
===================================================
Matrícula: {chave}
Nome: {nome}
Código da função: {cod_funcao}
Salário bruto: R$ {bruto:.2f}
Imposto: {imposto(bruto)}%
Salário líquido: R$ {liquido(bruto, faltas, imposto(bruto)):.2f}
===================================================''')
#
def print_tabela_maior_falta(chave, valor):
    nome, cod_funcao, faltas, bruto = valor
    print(f'''
===================================================
Matrícula: {chave}
Nome: {nome}
Código da função: {cod_funcao}
Numero de faltas: {faltas}
Desconto do salário: R$ {bruto - liquido(bruto, faltas, imposto(bruto)):.2f}
===================================================''')
# 
def liquido(bruto, faltas, imposto):
    liquido = bruto - (((bruto * imposto) / 100) + (faltas * (bruto / 30)))
    return liquido
def imposto(bruto):
    if (bruto < 2259.21):
        imposto = 0
    elif (2259.21 <= bruto <= 2828.65):
        imposto = 7.5
    elif (2828.66 <= bruto <= 3751.05):
        imposto = 15
    elif (3751.06 <= bruto <= 4664.68):
        imposto = 22.5
    else:
        imposto = 27.5
    #
    return imposto
#
BD = {}
#
MENU = int(input('[1].INSERIR FUNCIONARIO, [2].REMOVER FUNCIONARIO, [3].FOLHA DE PAGAMENTO, [4].RELATORIO, [5].MAIOR SALARIO, [6].MAIOR FALTAS: '))
#
while (MENU != 0):
    if (MENU == 1): #INSERIR FUNCIONARIO
        matricula = int(input('\nMATRICULA DO FUNCIONARIO: ')) #CODIGO DO FUNCIONARIO
        #
        if (matricula not in BD):
            nome = str(input('NOME DO FUNCIONARIO: ')).upper()
            cod_funcao = int(input('CÓDIGO DA FUNÇÃO: ')) #101(VENDEDOR) OU 102(ADMINISTRATIVO)
            #
            if cod_funcao in [101, 102]:
                faltas = int(input('FALTAS DO FUNCIONARIO: '))
                #
                if (cod_funcao == 101): #VENDEDOR
                    comissao = float(input('VOLUME DE VENDAS: '))
                    bruto = 1500 + ((comissao * 9) / 100)
                #
                else: #ADMINISTRATIVO
                    bruto = float(input('SALARIO BRUTO DO FUNCIONARIO: '))
                #
                BD[matricula] = [nome, cod_funcao, faltas, bruto] #INSERE NO DICIONARIO(BD) AS INFORMAÇÕES DO FUNCIONARIO
            else:
                print('--->>> CODIGO DA FUNÇÃO INVALIDO <<<---')
        #
        else:
            print('--->>> MATRICULA JÁ CADASTRADA <<<---')
    elif (MENU == 2): #REMOVER FUNCIONARIO
        matricula = int(input('\nMATRICULA DO FUNCIONARIO(DELETAR): '))
        #
        if (matricula not in BD):
            print('--->>> MATRICULA NÃO CADASTRADA <<<---')
        else:
            del BD[matricula] #APAGA O FUNCIONARIO DO DICIONARIO(BD) BASEADO EM SUA MATRICULA
    elif (MENU == 3): #FOLHA DE PAGAMENTO
        matricula = int(input('\nMATRICULA DO FUNCIONARIO(FOLHA DE PAGAMENTO): '))
        #
        if (matricula not in BD):
            print('--->>> MATRICULA NÃO CADASTRADA <<<---')
        else:
            valor = BD.get(matricula) #RETORNA OS VALORES DA MATRICULA ESPECIFICA
            print_tabela_folha(matricula, valor) #IMPRIME AS INFORMAÇOES DO FUNCIONARIO
    elif (MENU == 4): #RELATORIO
        for chave, valor in BD.items():
            print_tabela_relatorio(chave, valor)
    elif (MENU == 5): #MAIOR SALARIO
        maior = 0
        #
        for chave, valor in BD.items():
            faltas = valor[2]
            bruto = valor[3]
            #
            if (liquido(bruto, faltas, imposto(bruto)) > maior):
                maior = liquido(bruto, faltas, imposto(bruto))
                chaveM = chave
                valorM = valor
        #
        print_tabela_maior_salario(chaveM, valorM)
    elif (MENU == 6): #MAIOR FALTAS
        maior = 0
        #
        for chave, valor in BD.items():
            faltas = valor[2]
            #
            if (faltas > maior):
                maior = faltas
                chaveM = chave
                valorM = valor
        #
        print_tabela_maior_falta(chaveM, valorM)
    MENU = int(input('\n[1].INSERIR FUNCIONARIO, [2].REMOVER FUNCIONARIO, [3].FOLHA DE PAGAMENTO, [4].RELATORIO, [5].MAIOR SALARIO, [6].MAIOR FALTAS: '))