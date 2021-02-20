from data.models.exceptions.job import AmountNotPresentException, UserIDNotPresentException, FeeTypeNotPresentException

REQUIRED_JOB_PROPS = {'amount': AmountNotPresentException,
                      'user_id': UserIDNotPresentException,
                      'fee_type': FeeTypeNotPresentException}


class Job:
    def __init__(self, *args, **kwargs):
        for required_params in REQUIRED_JOB_PROPS.keys():
            if required_params not in kwargs:
                raise REQUIRED_JOB_PROPS[required_params]

        self.amount = kwargs['amount']
        self.user_id = kwargs['user_id']
        self.fee_type = kwargs['fee_type']
