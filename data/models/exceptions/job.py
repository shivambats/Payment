class AmountNotPresentException(Exception):
    def __str__(self):
        return 'Job cannot be created without amount'


class UserIDNotPresentException(Exception):
    def __str__(self):
        return 'Job cannot be created without userid'


class FeeTypeNotPresentException(Exception):
    def __str__(self):
        return 'Job cannot be created without FeeType'
