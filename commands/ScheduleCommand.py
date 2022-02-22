from .CommandInterface import CommandInterface
from management.schedule import Schedule


class ScheduleCommand(CommandInterface):

    def execute(self) -> None:
        Schedule.schedules()