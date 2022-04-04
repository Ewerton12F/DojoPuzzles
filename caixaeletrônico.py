# https://dojopuzzles.com/problems/caixa-eletronico/
#
# Caixa Eletrônico
#
# Desenvolva um programa que simule a entrega de notas quando um cliente efetuar
# um saque em um caixa eletrônico. Os requisitos básicos são os seguintes:
# Entregar o menor número de notas;
# É possível sacar o valor solicitado com as notas disponíveis;
# Saldo do cliente infinito;
# Quantidade de notas infinito (pode-se colocar um valor finito de cédulas para 
# aumentar a dificuldade do problema);
# Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00
# Exemplos:
# Valor do Saque: R$ 30,00 – Resultado Esperado: Entregar 1 nota de R$20,00 e 
# 1 nota de R$ 10,00.
# Valor do Saque: R$ 80,00 – Resultado Esperado: Entregar 1 nota de R$50,00 
# 1 nota de R$ 20,00 e 1 nota de R$ 10,00.


saque = int(input('Valor do Saque: R$ '))

n100 = saque // 100
n50 = (saque % 100) // 50
n20 = ((saque % 100) % 50) // 20
n10 = (((saque % 100) % 50) % 20) // 10

print(f'Entregar:')
print(f'{n100} nota de R$100,00')
print(f'{n50} nota de R$50,00')
print(f'{n20} nota de R$20,00')
print(f'{n10} nota de R$10,00')