from .CommandInterface import CommandInterface
from management.serviceFee import Service


class SetServiceCommand(CommandInterface):

    def execute(self) -> None:
        Service.setServiceFee()