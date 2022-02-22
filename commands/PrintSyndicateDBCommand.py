from .interface import CommandInterface
from management.printData import PrintData


class PrintSyndicateDBCommand(CommandInterface):

    def execute(self) -> None:
        PrintData.printSyndicate()