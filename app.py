import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Pizza Supreme', 'categoria': 'Pizza', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False}]


# Titulo
def exibir_nome_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)


# Informações Menu
def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alternar Estado do Restaurante')
    print('4. Sair\n')


def finalizar_app():
    exibir_subtitulo('Finalizando o app')


def voltar_ao_menu_principal():
    input('\n Digite uma tecla para voltar ao menu principal: ')
    main()


def opcao_invalida():
    print('opcao invalida \n')
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))

    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    '''Essa Função é responsavel por cadastrar um novo Restaurante

    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restuarante a lista de restaurantes

    '''

    exibir_subtitulo('Cadastro de novos restaurantes: ')

    nome_do_restaurante = input(
        'Digite o nome do restaurante que deseja cadastrar: ')

    categoria = input(
        f'Digite o nome da Categoria do restaurante {nome_do_restaurante}:  ')

    dados_do_restaurante = {'nome': nome_do_restaurante,
                            'categoria': categoria, 'ativo': False}

    restaurantes.append(dados_do_restaurante)

    print(
        f'\n O resutaurante {nome_do_restaurante} foi cadastrado com sucesso! \n')

    voltar_ao_menu_principal()


def listar_restaurantes():
    exibir_subtitulo('Listando os Restaurantes: ')

    # Em Portugues:
    # para cada restaurantes na lista restaurantes:
    # nome

    print(f'{'Nome do Restaurante:'.ljust(22)} | {'Categoria:'.ljust(20)} | {'Status:.'} ')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado do Restaurante')

    nome_restaurante = input(
        'digite o nome do restaurante que deseja alternar o estado: ')

    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante[
                'ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()


def escolher_opcao():
    try:

        opcao_escolhida = int(input('Escolha uma opção: '))

        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:
            alternar_estado_restaurante()

        elif opcao_escolhida == 4:
            finalizar_app()

        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
