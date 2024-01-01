nome = 'Erick'
altura = 1.75
peso = 80
imc = peso / (altura * altura)

print(nome, ' tem ', altura, ' de altura.')
print('Pesa ', peso, ' quilos e seu IMC ', imc)
print()

# Formataçao de string
linha_1 = f'{nome} tem {altura} de altura.'
linha_2 = f'Pesa {peso}, quilos e seu IMC {imc:.3f}'

print(linha_1)
print(linha_2)