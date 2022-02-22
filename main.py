################################################################################
## Projeto de Software - Refatorado - 2021.1
##
## FOLHA DE PAGAMENTO
##
################################################################################

from commands.Invoker import Invoker
from management.undoRedo import UndoRedo
from dataBase import data
from os import system


class Main:

    @staticmethod
    def menu():

        option = True
        invoke = Invoker()
        data.DataBaseManager.readDataBase()
        UndoRedo.saveState()
        while option != '0':
            system('cls')
            option = input('1 - Adicionar empregado\n'
                           '2 - Remover empregado\n'
                           '3 - Lançar cartão de ponto\n'
                           '4 - Lançar um resultado de venda\n'
                           '5 - Lançar taxa de serviço\n'
                           '6 - Alterar os dados do empregado\n'
                           '7 - Rodar folha de pagamento\n'
                           '8 - Escolher agenda de pagamento\n'
                           '9 - Criar uma nova agenda de pagamento\n'
                           '10 - Listar todos os empregados\n'
                           '11 - Listar cartões de ponto\n'
                           '12 - Listar resultados de vendas\n'
                           '13 - Listar empregados associados ao sindicato\n'
                           '14 - Listar agenda de pagamento dos empregados\n'
                           '15 - Listar agendas\n'
                           '16 - Listar contracheques\n'
                           '17 - Desfazer\n'
                           '18 - Refazer\n'
                           '0 - sair\n')
            system('cls')
            invoke.run(option)
            UndoRedo.saveState()


if __name__ == '__main__':
    Main.menu()
