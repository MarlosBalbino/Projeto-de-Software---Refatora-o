from .interface import CommandInterface
from management.payRoll import PayRoll


class PayRollCommand(CommandInterface):

    def execute(self) -> None:
        PayRoll.run()
