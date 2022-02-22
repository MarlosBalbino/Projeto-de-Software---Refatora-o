from employee.employee_ import __Employee
from management.paycheck.paycheck import Paycheck
from employee.SalaryInterface import SalaryInterface


class Hourly(__Employee, SalaryInterface):
    """representa empregado horista"""

    # estende o método __init__ da super classe
    def __init__(self, name='None', address='None', type='None', id=0, syndicate=0, payment='None',
                 hourlysalary=0, hours=0):
        super().__init__(name, address, type, id, syndicate, payment)
        self.hourlysalary = hourlysalary
        self.hours = hours
        self.extra_hours = 0

    def setWorkingHours(self, hours):
        """determina horas trabalhadas"""
        self.hours += hours

    def setExtraWorkingHours(self, hours):
        self.extra_hours += hours

    def setHourlySalary(self, hourlysalary):
        """determina o salário horário"""
        self.hourlysalary = hourlysalary

    def getWorkingHours(self):
        """retorna as horas de trabalho"""
        return self.hours

    def getExtraWorkingHours(self):
        """retorna as horas extras de trabalho"""
        return self.extra_hours

    def getHourlySalary(self):
        """retorna salário horário"""
        return self.hourlysalary

    def getData(self):
        return f"{super().getData()}" + \
               f"Salário horário: R$ {self.hourlysalary:.2f}\n" \
               f"Horas trabalhadas: {self.hours:.2f} horas\n" \
               f"Horas extras: {self.extra_hours:.2f} horas"

    def _repr(self):
        return f"{super()._repr()}, " + \
               f"{self.hourlysalary}, " \
               f"{self.hours}"

    def __repr__(self):
        return f"Hourly({self._repr()})"

    def __str__(self):
        return f"Hourly({self._repr()})"

    def calculateSalary(self):

        workingHours = self.getWorkingHours()
        extraHours = self.getExtraWorkingHours()
        hourlySalary = self.getHourlySalary()

        salary = hourlySalary * workingHours
        extraRate = ((1.5 / 100) * hourlySalary) + hourlySalary
        extraSalary = extraRate * extraHours
        self.grossSalary = salary + extraSalary

        paycheck = Paycheck(self.name, self.id, self.grossSalary, self.payment,
                            self.hourlysalary, self.hours, self.extra_hours)
        return paycheck
