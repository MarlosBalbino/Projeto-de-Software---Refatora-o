from .CommandInterface import CommandInterface
from management.timeCard import TimeCard


class SetTimeCardCommand(CommandInterface):

    def execute(self) -> None:
        TimeCard.setTimeCard()
