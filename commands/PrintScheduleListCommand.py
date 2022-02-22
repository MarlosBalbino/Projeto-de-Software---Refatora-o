from .CommandInterface import CommandInterface
from management.printData import PrintData


class PrintScheduleListCommand(CommandInterface):

    def execute(self) -> None:
        PrintData.printScheduleList()