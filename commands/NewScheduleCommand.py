from .CommandInterface import CommandInterface
from management.schedule import Schedule


class NewScheduleCommand(CommandInterface):

    def execute(self) -> None:
        Schedule.newSchedules()
