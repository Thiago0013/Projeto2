from time import sleep
def Reboot(arq):
    import os
    print('Você digitou o numero secreto 1010! A maquina irá fazer um Reboot nos dados da lista...')
    sleep(3) 
    try:
        os.remove(arq)
    except FileNotFoundError:
        print('ERRO! Arquivo já está excluido...')
        sleep(3)
    except:
        print('Erro no reboot dos dados...')
        sleep(3)
    else:
        print('Reboot feito com sucesso!')
        sleep(3)
        print('Reiniciando o programa...')
        sleep(2)
def LeiaInt(txt):
    while True:
        try:
            numero = int(input(txt))
        except:
            print('Digite um numero inteiro!')
        else:
            return numero
def LeiaFloat(txt):
    while True:
        try:
            numero = float(input(txt))
        except:
            print('Digite um numero válido!')
        else:
            return numero
def Linha(txt):
    txt = str(txt)
    linha = '=' * 42
    print(linha)
    print(txt.center(42))
    print(linha)
def Menu(nome):
    for n in nome:
        print(n)
def ArquivoExiste(arq):
    try:
        with open(arq, 'r') as file:
            file.close()
    except:
        return True
def CriarArquivo(arq):
    try:
        with open(arq,'wt+') as file:
            file.close()
    except:
        print('Erro ao tentar criar arquivo!')
    else:
        print('Arquivo criado com sucesso!')
def AdicionarArq(arq,nome,preço):
    with open(arq, 'a') as file:
        file.write(f' {nome};{preço}\n')

def VerArquivo(arq):
    with open(arq, 'rt+') as file:
        ver = file.read().replace('\n', '')
        ver = ver.split(';')
        ver = ' '.join(ver)
        ver = ver.split()
        ver
        num = 0
        for n in range(0,len(ver)):
            if n % 2 == 0:
                print(f'[{num + 1}] {ver[n].replace("_", " "):<30} R${float(ver[n+1]):.2f}')
                num += 1
    sleep(5)

def RemoverLista(arq,remover):
    with open(arq, 'rt+') as file:
        ver = file.read().replace('\n', '')
        ver = ver.split(';')
        ver = ' '.join(ver)
        ver = ver.split()
        while True:
            try:
                posição = ver.index(remover)
                
            except:
                return 'O item não foi encontrado!'
            else:
                print('=' * 42)
                print(f'Você deseja remover para sempre o item: {ver[posição]} R${ver[posição+1]}? [s/n]')
            perg = input('Digite [s/n]: ').lower()
            if perg == 's':
                del ver[posição], ver[posição]
                with open(arq, 'w+') as file:
                    file.write('')
                for i in range(0,len(ver)):
                    with open(arq, 'a') as file:
                        if i % 2 == 0:
                            file.write(f' {ver[i]};{ver[i+1]}\n')
                print('Item removido com sucesso!')
                return True
            elif perg == 'n':
                return False
            else:
                print(f'Entrada invalida! Digite s/n...')