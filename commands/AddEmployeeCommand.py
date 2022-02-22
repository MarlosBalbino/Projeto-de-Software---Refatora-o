from .CommandInterface import CommandInterface
from management.employeeCRUD import EmployeeCRUD


class AddEmployeeCommand(CommandInterface):

    def execute(self) -> None:
        EmployeeCRUD.add()
