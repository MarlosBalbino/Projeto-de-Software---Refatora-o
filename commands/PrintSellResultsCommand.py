from .interface import CommandInterface
from management.printData import PrintData


class PrintSellResultsCommand(CommandInterface):

    def execute(self) -> None:
        PrintData.printSellResults()