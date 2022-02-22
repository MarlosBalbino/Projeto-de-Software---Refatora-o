from .interface import CommandInterface


class NoneObject(CommandInterface):

    def execute(self) -> None:
        pass
