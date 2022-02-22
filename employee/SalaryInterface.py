from abc import ABC, abstractmethod


class SalaryInterface(ABC):

    @abstractmethod
    def calculateSalary(self):
        pass
