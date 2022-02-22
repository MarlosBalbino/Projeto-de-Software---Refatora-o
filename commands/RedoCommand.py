from .interface import CommandInterface
from management.undoRedo import UndoRedo


class RedoCommand(CommandInterface):

    def execute(self) -> None:
        UndoRedo.redo()