from .interface import CommandInterface
from management.undoRedo import UndoRedo


class UndoCommand(CommandInterface):

    def execute(self) -> None:
        UndoRedo.undo()