from abc import ABC, abstractmethod


class PaymentInterface(ABC):

    @abstractmethod
    def calcPayment(self):
        pass
