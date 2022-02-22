from .CommandInterface import CommandInterface
from management.timeCard import TimeCard


class SetExtraHoursCommand(CommandInterface):

    def execute(self) -> None:
        TimeCard.setExtra()
