print('''
                       Bem vindo ao jogo Zero Cancela!! 
==============================================================================
------------------------------->>> Regras <<<---------------------------------      
==============================================================================
 * Ao digitar um número inteiro positivo, ele será adicionado à soma total.
 * Ao digitar um zero (0), o último item digitado será anulado da soma total.
 * É possível fazer somente três anulações consecutivas.
 * Ao digitar um número negativo, o programa encerrará.
==============================================================================
''')
soma = numConsiderados = numDesconsiderados = ult1 = ult2 = ult3 = zerosConsecutivos = 0
num = int(input('Digite um número para começar: '))
while (num >= 0):
    if (num == 0):
        if (zerosConsecutivos == 3):
            print('----->>> SÓ É PERMITIDO ATÉ 3 ANULAÇÕES CONSECUTIVAS!!! <<<-----')
        elif (ult1 > 0):
            zerosConsecutivos += 1
            numDesconsiderados += 1
            soma -= ult1
            ult1, ult2, ult3 = ult2, ult3, num
    else:
        zerosConsecutivos = 0
        numConsiderados += 1
        soma += num
        ult3, ult2, ult1 = ult2, ult1, num
    num = int(input('Digite um número: '))
print(f'''
====================================================
----------------->>> RESULTADOS <<<-----------------
====================================================
Soma total da sequência: {soma}
Números considerados na soma: {numConsiderados - numDesconsiderados}
Números desconsiderados: {numDesconsiderados}
====================================================
''')