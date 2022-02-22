class Paycheck:

    def __init__(self, name, Id, grossSalary, payment, hourlySalary=0, workingHours=0, extraHours=0,
                 commission=0, periodCommission=0, unionFee=0, serviceFee=0, INSS=0, FGTS=0, netSalary=0,
                 discounts=0, serviceDiscount=0, unionDiscount=0, INSSDiscount=0, FGTSDiscount=0):

        self.__name = name
        self.__Id = Id
        self.__grossSalary = grossSalary
        self.__payment = payment

        self.__hourlySalary = hourlySalary
        self.__workingHours = workingHours
        self.__extraHours = extraHours

        self.__commission = commission
        self.__periodCommission = periodCommission

        self.__unionFee = unionFee
        self.__serviceFee = serviceFee
        self.__INSS = INSS
        self.__FGTS = FGTS
        self.__netSalary = netSalary
        self.__discounts = discounts

        self.__serviceDiscount = serviceDiscount
        self.__unionDiscount = unionDiscount
        self.__INSSDiscount = INSSDiscount
        self.__FGTSDiscount = FGTSDiscount

    def __repr(self):
        return f"'{self.__name}', " \
               f"{self.__Id}, " \
               f"{self.__grossSalary}, " \
               f"'{self.__payment}', " \
               f"{self.__hourlySalary}, " \
               f"{self.__workingHours}, " \
               f"{self.__extraHours}, " \
               f"{self.__commission}, " \
               f"{self.__periodCommission}, " \
               f"{self.__unionFee}, " \
               f"{self.__serviceFee}, " \
               f"{self.__INSS}, " \
               f"{self.__FGTS}, " \
               f"{self.__netSalary}, " \
               f"{self.__discounts}, " \
               f"{self.__serviceDiscount}, " \
               f"{self.__unionDiscount}, " \
               f"{self.__INSSDiscount}, " \
               f"{self.__FGTSDiscount}"

    def __repr__(self):
        return f'Paycheck({self.__repr()})'

    def __str__(self):
        return f'Paycheck({self.__repr()})'

    def setRates(self, FGTS, INSS, unionFee, serviceFee):
        self.__FGTS = FGTS
        self.__INSS = INSS
        self.__unionFee = unionFee
        self.__serviceFee = serviceFee

    def setDiscounts(self, serviceDiscount, unionDiscount, INSSDiscount, FGTSDiscount,
                     totalDiscounts):
        self.__serviceDiscount = serviceDiscount
        self.__unionDiscount = unionDiscount
        self.__INSSDiscount = INSSDiscount
        self.__FGTSDiscount = FGTSDiscount
        self.__discounts = totalDiscounts

    def setNetSalary(self, netSalary):
        self.__netSalary = netSalary

    @staticmethod
    def __rate(x):
        if x:
            return f'{x:.2f}%'
        return 'n/a'

    @staticmethod
    def __RS(x):
        if x:
            return f"R$ {x:.2f}"
        return 'n/a'

    @staticmethod
    def __hours(x):
        if x:
            return f"{x:.2f} horas"
        return 'n/a'

    def payCheck(self):
        return f'Nome do empregado(a): {self.__name}\n' \
               f'Id da folha de pagamento: {self.__Id}\n' \
               f'Forma de pagamento: {self.__payment}\n' \
               f'Taxa do sindicato: {self.__rate(self.__unionFee)}\n' \
               f'Taxa de serviço: {self.__rate(self.__serviceFee)}\n' \
               f'INSS: {self.__rate(self.__INSS)}\n' \
               f'FGTS: {self.__rate(self.__FGTS)}\n' \
               f'Ganho por hora: {self.__RS(self.__hourlySalary)}\n' \
               f'Horas trabalhadas: {self.__hours(self.__workingHours)}\n' \
               f'Horas extras: {self.__hours(self.__extraHours)}\n' \
               f'Percentual de comissão: {self.__rate(self.__commission)}\n' \
               f'Comissão do período: {self.__RS(self.__periodCommission)}\n' \
               f'Deduções: {self.__RS(self.__discounts)}\n' \
               f'Salário bruto: {self.__RS(self.__grossSalary)}\n' \
               f'Salário líquido: {self.__RS(self.__netSalary)}\n'

    def printDiscounts(self):

        return f"Taxas                 Deduções\n" \
               f"serviço: {self.__rate(self.__serviceFee)}        {self.__RS(self.__serviceDiscount):7}\n" \
               f"sindicato: {self.__rate(self.__unionFee)}      {self.__RS(self.__unionDiscount):7}\n" \
               f"INSS: {self.__rate(self.__INSS)}           {self.__RS(self.__INSSDiscount):7}\n" \
               f"FGTS: {self.__rate(self.__FGTS)}           {self.__RS(self.__FGTSDiscount):7}\n"
