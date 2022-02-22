import time
from dataBase import data
from employee.hourly import Hourly
from management.extraModules.mytime import Time
from management.fill_employee_data.fillData import FillHourly
from management.extraModules.verifyEmployee import verifyEmployee
from os import system


class TimeCard:
    @staticmethod
    def calcWorkingHours(timecards, new_timecard, employee):
        Id = employee.getId()

        def calcExtraWorkingHours(delta_h):
            extra_h = 0
            if delta_h > 8:
                extra_h = delta_h - 8
            return extra_h

        # CALCULA AS HORAS TRABALHADAS NO DIA
        if len(timecards) % 2 != 0:
            last_timecard = timecards[-1]  # pega o último cartão de ponto registrado
            h_final = new_timecard.split()[-1]  # obtém a hora final
            h_initial = last_timecard.split()[-1]  # obtém a hora inicial
            # Δh = hora_final - hora_inicial
            h_final = Time(h_final)
            h_initial = Time(h_initial)
            delta_h = h_final - h_initial
            extra_h = calcExtraWorkingHours(delta_h.getHours())
            employee.setWorkingHours(delta_h.getHours())
            employee.setExtraWorkingHours(extra_h)
            data.dynamicDataBase[Id] = employee
            data.DataBaseManager.writeDB('employees')

    @staticmethod
    def setTimeCard():
        """lança um cartão de ponto"""
        print(f"{16 * '='} Cartão de ponto {16 * '='}")

        Id = verifyEmployee()
        if Id != -1:
            employee = data.dynamicDataBase[Id]
            if type(employee) != Hourly:
                print('Esse empregado não é horista.\n')
                system('pause')
                return None

            try:
                new_timecard = time.strftime('%d/%m/%y %H:%M:%S')
                timecards = []

                # RECUPERA CARTÕES DE PONTO, CASO EXISTAM
                if Id in data.dynamicTimeCards:
                    timecards = data.dynamicTimeCards[Id]
                    TimeCard.calcWorkingHours(timecards, new_timecard, employee)

                # ADICIONA NOVO CARTÃO DE PONTO
                timecards.append(new_timecard)
                data.dynamicTimeCards[Id] = timecards
                data.DataBaseManager.writeDB('timecards')
                print('Cartão de ponto adicionado com sucesso!!\n')
                system('pause')
                return 1

            except:
                print('Não foi possível lançar cartão de ponto.\n')
        system('pause')

    @staticmethod
    def setHours():
        Id = verifyEmployee()
        if Id != -1:
            employee = data.dynamicDataBase[Id]
            if type(employee) != Hourly:
                print('Esse empregado não é horista.\n')
                system('pause')
                return None

            fill = FillHourly(init=0)
            fill.setWorkingHours()
            hours = fill.getWorkingHours()

            employee.setWorkingHours(hours)
            data.dynamicDataBase[Id] = employee
            data.DataBaseManager.writeDB('employees')
        system('pause')

    @staticmethod
    def setExtra():
        Id = verifyEmployee()
        if Id != -1:
            employee = data.dynamicDataBase[Id]
            if type(employee) != Hourly:
                print('Esse empregado não é horista.\n')
                system('pause')
                return None

            fill = FillHourly(init=0)
            fill.setExtraWorkingHours()
            extra_h = fill.getExtraWorkingHours()

            employee.setExtraWorkingHours(extra_h)
            data.dynamicDataBase[Id] = employee
            data.DataBaseManager.writeDB('employees')
        system('pause')
