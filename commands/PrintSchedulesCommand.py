from .CommandInterface import CommandInterface
from management.printData import PrintData


class PrintSchedulesCommand(CommandInterface):

    def execute(self) -> None:
        PrintData.printSchedules()