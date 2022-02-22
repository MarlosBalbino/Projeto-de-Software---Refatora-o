from .CommandInterface import CommandInterface
from management.employeeCRUD import EmployeeCRUD


class UpdateEmployeeCommand(CommandInterface):

    def execute(self) -> None:
        EmployeeCRUD.update()

