a = 'AAAA'
b = 'BBBB'
c = 1.1

# string = 'a={} b={} c={:.2f}'
# string = 'b={1} a={0} a={1} c={2:.2f}'
string = 'a={nome1} b={nome2} c={nome3:.2f}'

# - Baseiam-se pela posição das variáveis informadas em 'format'
# formato = string.format(a, b, c) 
# formato = string.format(a, b, c)

# - Baseiam-se pelo 'parâmetro nomeado'
formato = string.format(nome1=a, nome2=b, nome3=c)

print(formato)