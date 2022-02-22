from .CommandInterface import CommandInterface
from management.printData import PrintData


class PrintPaychecksCommand(CommandInterface):

    def execute(self) -> None:
        PrintData.printPaychecks()