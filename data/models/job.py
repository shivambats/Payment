from data.models.common.constants import FeeType
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
        try:
            self.fee_type = FeeType[kwargs['fee_type']]
        except KeyError:
            raise TypeError("Fee Type is invalid") from None
