import Pyro5.api


c=Pyro5.api.Proxy("PYRONAME:calc")

print('Operações:\n Para adição digite => +\n Para subtração digite => -\n Para multiplicação digite => *\n Para exponenciação digite => **\n Para divisão digite => /\n ')

op=input('Digite a operação desejada: ')

if (op == '+'):
    v1 = int(input('Valor 1: '))
    v2 = int(input('Valor 2: '))
    print(c.soma(v1, v2))

elif (op == '-'):
    v1 = int(input('Valor 1: '))
    v2 = int(input('Valor 2: '))
    print(c.sub(v1, v2))

elif (op == '*'):
    v1 = int(input('Valor 1: '))
    v2 = int(input('Valor 2: '))
    print(c.mult(v1, v2))

elif (op == '**'):
    v1 = int(input('Valor 1: '))
    v2 = int(input('Valor 2: '))
    print(c.expo(v1, v2))

elif (op == '/'):
    v1 = int(input('Valor 1: '))
    v2 = int(input('Valor 2: '))
    print(c.div(v1 ,v2))

else:
    print('Operação inválida!')



