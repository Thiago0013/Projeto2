from Funções import *
arquivo = 'Dados.txt'
if ArquivoExiste(arquivo):
        CriarArquivo(arquivo)
while True:
    Linha('MENU DO SISTEMA')
    Menu(['1 - Ver Lista','2 - Adicionar na Lista','3 - Remover Lista','4 = Sair do sistema'])
    print('=' * 42)
    opc = LeiaInt('Escolha a opção: ')
    if opc == 1:
        Linha('LISTA')
        VerArquivo(arquivo)
    elif opc == 2:
        Linha('ADICIONAR ITEM A LISTA')
        nome = input('Nome do item: ').lstrip(' ').replace(' ', '_')
        preço = LeiaFloat('Preço: ')
        AdicionarArq(arquivo,nome,preço)
    elif opc == 3:
        while True:
            Linha('EXCLUIR ITEM DA LISTA')
            VerArquivo(arquivo)
            valor = RemoverLista(arquivo,input('Remover o item: ') )
            if valor:
                break
    elif opc == 4:
        print('Saindo do sistema... Até logo!!!')
        break
    elif opc == 1010:
        Reboot(arquivo)
        break
    else:
        print('Entrada Incorreta! Digite um valor que apresenta no menu')