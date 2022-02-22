from .CommandInterface import CommandInterface
from management.printData import PrintData


class PrintDataBaseCommand(CommandInterface):

    def execute(self) -> None:
        PrintData.printDataBase()
