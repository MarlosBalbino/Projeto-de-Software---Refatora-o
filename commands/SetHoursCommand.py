from .CommandInterface import CommandInterface
from management.timeCard import TimeCard


class SetHoursCommand(CommandInterface):

    def execute(self) -> None:
        TimeCard.setHours()
