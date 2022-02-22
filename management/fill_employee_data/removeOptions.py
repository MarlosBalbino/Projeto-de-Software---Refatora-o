from management.extraModules.findInSyndicate import FindSyndicate
from dataBase import data
from os import system


class Remove:

    @staticmethod
    def employeeData(Id):
        """remove empregado do banco de dados"""
        try:
            data.dynamicDataBase.pop(Id)
            data.DataBaseManager.writeDB('employees')
            # data.DataBaseManager.writeDataBase()
        except:
            print(f"Erro: não foi possível remover o empregado\n")
            system('pause')

    @staticmethod
    def timeCardsData(Id):
        """remove cartões de ponto, caso existam"""
        try:
            data.dynamicTimeCards.pop(Id)
            data.DataBaseManager.writeDB('timecards')
            # data.DataBaseManager.writeTimeCard()
        except KeyError:
            pass

    @staticmethod
    def sellResultsData(Id):
        """remove os resultados de venda, caso existam"""
        try:
            data.dynamicSellResults.pop(Id)
            data.DataBaseManager.writeDB('sellresults')
            # data.DataBaseManager.writeSellResults()
        except KeyError:
            pass

    @staticmethod
    def syndicateData(Id):
        """remove empregado do sindicato, caso pertença"""
        try:
            find = FindSyndicate()
            find.search(Id)
            if find.found() == 1:
                data.dynamicSyndicateDB.pop(find.getSyndicateId())
                data.DataBaseManager.writeDB('syndicate')
                # data.DataBaseManager.writeSyndicateDB()
        except:
            pass

    @staticmethod
    def scheduleData(Id):
        try:
            data.scheduleDB.pop(Id)
            data.DataBaseManager.writeDB('syndicate')
            # data.DataBaseManager.writeScheduleDB()
        except KeyError:
            pass