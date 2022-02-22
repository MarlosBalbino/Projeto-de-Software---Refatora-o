from .CommandInterface import CommandInterface
from management.sellResult import SellResult


class SetSellResultCommand(CommandInterface):

    def execute(self) -> None:
        SellResult.setSellResult()