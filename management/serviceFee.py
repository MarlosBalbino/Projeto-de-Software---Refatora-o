from management.extraModules.verifyEmployee import verifyEmployee
from management.extraModules.findInSyndicate import FindSyndicate
from employee import *
from dataBase import data
from os import system


class Service:

    @staticmethod
    def setServiceFee():
        print(f"{16 * '='} Taxa de serviço {16 * '='}")

        Id = verifyEmployee()
        if Id != -1:
            find = FindSyndicate()
            find.search(Id)

            if find.found() == 1:
                syndicateId = find.getSyndicateId()
                syndicateEmp = data.dynamicSyndicateDB[syndicateId]
                while True:
                    try:
                        serviceFee = eval(input('\nDigite a taxa de serviço:\n'))
                        syndicateEmp.setServiceFee(serviceFee)
                        break
                    except:
                        print('\nDigite um número inteiro ou ponto flutuante\n')
                data.dynamicSyndicateDB[syndicateId] = syndicateEmp
                data.DataBaseManager.writeDB('syndicate')
                print('\nTaxa de serviço cadastrada.\n')
                data.done = 1
            else:
                print('Empregado não possui vinculo com o sindicato\n')
        system('pause')

