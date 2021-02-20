class JobNotPresentException(Exception):
    def __str__(self):
        return 'Payment cannot be created without Job property'


class EmptyJobException(Exception):
    def __str__(self):
        return 'Payment must have at least one job'


class InvalidJobTypeException(Exception):
    def __str__(self):
        return 'Job property must be a list'
