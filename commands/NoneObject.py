from .CommandInterface import CommandInterface


class NoneObject(CommandInterface):

    def execute(self) -> None:
        pass
