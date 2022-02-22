from .CommandInterface import CommandInterface
from management.employeeCRUD import EmployeeCRUD


class RemoveEmployeeCommand(CommandInterface):

    def execute(self) -> None:
        EmployeeCRUD.remove()
