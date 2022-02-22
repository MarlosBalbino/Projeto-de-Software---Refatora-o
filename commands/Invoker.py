from commands import *


class Invoker:

    functions = {1: AddEmployeeCommand,
                 2: RemoveEmployeeCommand,
                 3: SetTimeCardCommand,
                 4: SetSellResultCommand,
                 5: SetServiceCommand,
                 6: UpdateEmployeeCommand,
                 7: PayRollCommand,
                 8: ScheduleCommand,
                 9: NewScheduleCommand,
                 10: PrintDataBaseCommand,
                 11: PrintTimeCardsCommand,
                 12: PrintSellResultsCommand,
                 13: PrintSyndicateDBCommand,
                 14: PrintSchedulesCommand,
                 15: PrintScheduleListCommand,
                 16: PrintPaychecksCommand,
                 17: UndoCommand,
                 18: RedoCommand,
                 0: NoneObject,
                 -1: EraseDataBaseCommand,
                 -2: SetHoursCommand,
                 -3: SetExtraHoursCommand}

    def __init__(self):
        self.slot = None

    def run(self, option):
        try:
            self.slot = self.functions[int(option)]()
        except:
            print('Digite uma das opções acima!')
            self.slot = NoneObject()
        self.slot.execute()






