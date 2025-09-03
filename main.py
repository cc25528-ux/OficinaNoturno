idade = int(input())

def verificaidade (idade):  
    if idade < 18:
        print('Menó')
    else: 
        print('Maió')

print(verificaidade(idade))