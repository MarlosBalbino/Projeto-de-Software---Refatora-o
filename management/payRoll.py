from employee import *
from dataBase import data as dt
from management.extraModules.mycalendar import Calendar
from management.extraModules.findInSyndicate import FindSyndicate
from os import system


class PayRoll:

    INSS = 7.5
    FGTS = 8
    payed = 0

    @classmethod
    def __pay(cls, Id):
        employee = dt.dynamicDataBase[Id]
        unionFee = 0
        serviceFee = 0

        find = FindSyndicate()
        find.search(Id)
        if find.found():
            syndicateId = find.getSyndicateId()
            syndicate = dt.dynamicSyndicateDB[syndicateId]
            serviceFee = syndicate.getServiceFee()
            unionFee = syndicate.getUnionFee()

        paycheck = employee.calculateSalary()
        grossSalary = employee.getGrossSalary()

        serviceDiscount = (serviceFee/100) * grossSalary
        unionDiscount = (unionFee/100) * grossSalary
        INSSDiscount = (cls.INSS/100) * grossSalary
        FGTSDiscount = (cls.FGTS/100) * grossSalary
        totalDiscounts = serviceDiscount + unionDiscount + INSSDiscount + FGTSDiscount

        netSalary = grossSalary - totalDiscounts

        paycheck.setRates(cls.FGTS, cls.INSS, unionFee, serviceFee)
        paycheck.setDiscounts(serviceDiscount, unionDiscount, INSSDiscount, FGTSDiscount, totalDiscounts)
        paycheck.setNetSalary(netSalary)

        print(f"{16*'='} Contracheque {16*'='}")
        print(paycheck.payCheck())
        print(paycheck.printDiscounts())
        print()

        dt.paycheckDB[Id] = paycheck
        dt.DataBaseManager.writeDB('paychecks')

    @classmethod
    def __weekly(cls, day, Id):
        if day == Calendar.currentDay():
            cls.__pay(Id)
            cls.payed = 1

    @classmethod
    def __monthly(cls, day, Id):
        lastMonthDay = Calendar.lastMonthDay()
        currentMonthDay = Calendar.currentMonthDay()
        if day == currentMonthDay or day > lastMonthDay:
            cls.__pay(Id)
            cls.payed = 1

        secondDay = day + 14
        if secondDay > lastMonthDay:
            secondDay = secondDay - lastMonthDay
        if secondDay == currentMonthDay:
            cls.__pay(Id)
            cls.payed = 1

    @classmethod
    def run(cls):
        for Id in dt.scheduleDB:
            day = dt.scheduleDB[Id][2]
            scheduleType = dt.scheduleDB[Id][1]
            switch = {1: cls.__weekly,
                      2: cls.__monthly,
                      3: cls.__monthly}
            switch[scheduleType](day, Id)
        if not cls.payed:
            print('Não há nem um pagamento agendado pra hoje.')
        else:
            dt.done = 1
        system('pause')

