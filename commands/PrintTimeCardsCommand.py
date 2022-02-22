from .CommandInterface import CommandInterface
from management.printData import PrintData


class PrintTimeCardsCommand(CommandInterface):

    def execute(self) -> None:
        PrintData.printTimeCards()