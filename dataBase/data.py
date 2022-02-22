from employee import *
from management.paycheck.paycheck import Paycheck
import os

dynamicDataBase = {}
dynamicTimeCards = {}
dynamicSellResults = {}
dynamicSyndicateDB = {}
scheduleDB = {}
scheduleList = {1: ['toda sexta-feira', 1, 4],
                2: ['ultimo dia do mês', 2, 31],
                3: ['a cada duas sextas-feiras', 3, 24]}
paycheckDB = {}

paths = {'employees': 'dynamicDataBase',
         'timecards': 'dynamicTimeCards',
         'sellresults': 'dynamicSellResults',
         'syndicate': 'dynamicSyndicateDB',
         'schedule': 'scheduleDB',
         'schedule_list': 'scheduleList',
         'paychecks': 'paycheckDB'}

done = 1


class DataBaseManager:

    @staticmethod
    def readDataBase():

        try:
            # LÊ OS DADOS DOS PESSOAIS DOS EMPREGADOS
            file = open(f'dataBase\\database\\employees.db', 'r', encoding='utf8')
            global dynamicDataBase
            dynamicDataBase = eval(file.read())
            file.close()

            # LÊ OS CARTÕES DE PONTO DOS HORISTAS
            try:
                global dynamicTimeCards
                file = open(f'dataBase\\database\\timecards.db', 'r', encoding='utf8')
                dynamicTimeCards = eval(file.read())
                file.close()
            except FileNotFoundError:
                pass

            # LÊ OS RESULTADOS DE VENDAS DOS COMISSIONADOS
            try:
                global dynamicSellResults
                file = open(f'dataBase\\database\\sellresults.db', 'r', encoding='utf8')
                dynamicSellResults = eval(file.read())
                file.close()
            except FileNotFoundError:
                pass

            # Lê OS DADOS SINDICAIS
            try:
                global dynamicSyndicateDB
                file = open(f'dataBase\\database\\syndicate.db', 'r', encoding='utf8')
                dynamicSyndicateDB = eval(file.read())
                file.close()
            except FileNotFoundError:
                pass

            # Lê A LISTA DE AGENDAS
            try:
                global scheduleList
                file = open(f'dataBase\\database\\schedule_list.db', 'r', encoding='utf8')
                dbSchedule = eval(file.read())
                file.close()
                for key in dbSchedule:
                    scheduleList[key] = dbSchedule[key]
            except FileNotFoundError:
                pass

            # LÊ AS AGENDAS DOS EMPREGADOS
            try:
                global scheduleDB
                file = open(f'dataBase\\database\\schedule.db', 'r', encoding='utf8')
                scheduleDB = eval(file.read())
                file.close()
            except FileNotFoundError:
                pass

            # LÊ OS CONTRACHEQUES DOS EMPREGADOS
            try:
                global paycheckDB
                file = open(f'dataBase\\database\\paychecks.db', 'r', encoding='utf8')
                paycheckDB = eval(file.read())
                file.close()
            except FileNotFoundError:
                pass

        except FileNotFoundError:
            pass

    @staticmethod
    def writeDB(path):
        try:
            file = open(f'dataBase\\database\\{path}.db', 'w', encoding='utf8')
            global paths
            database = paths[path]
            file.write(f"{eval(database)}")
            file.flush()
            file.close()
        except SyntaxError:
            pass

    @classmethod
    def writeAll(cls):
        for path in paths:
            cls.writeDB(path)

    @staticmethod
    def eraseAll():

        global dynamicDataBase
        global dynamicTimeCards
        global dynamicSellResults
        global dynamicSyndicateDB
        global scheduleDB
        global scheduleList
        global paycheckDB

        dynamicDataBase = {}
        dynamicTimeCards = {}
        dynamicSellResults = {}
        dynamicSyndicateDB = {}
        scheduleDB = {}
        paycheckDB = {}
        scheduleList = {1: ['toda sexta-feira', 1, 4],
                        2: ['ultimo dia do mês', 2, 31],
                        3: ['a cada duas sextas-feiras', 3, 24]}

        for file in os.listdir('dataBase\\database'):
            try:
                os.remove(f'dataBase\\database\\{file}')
            except OSError:
                pass



