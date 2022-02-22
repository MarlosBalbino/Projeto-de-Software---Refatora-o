from .CommandInterface import CommandInterface
from management.employeeCRUD import EmployeeCRUD


class EraseDataBaseCommand(CommandInterface):

    def execute(self) -> None:
        EmployeeCRUD.eraseDataBase()
