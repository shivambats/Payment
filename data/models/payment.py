from data.models.common.constants import PaymentStatus
from data.models.exceptions.payment import JobNotPresentException, InvalidJobTypeException, EmptyJobException

REQUIRED_PROPS = {
    'job': JobNotPresentException
}


class Payment:
    def __init__(self, *args, **kwargs):
        for required_params, exception in REQUIRED_PROPS.items():
            if required_params not in kwargs:
                raise exception

        self.job = kwargs["job"]
        self.status = PaymentStatus.CREATED

        if not isinstance(self.job, list):
            raise InvalidJobTypeException

        if not self.job:
            raise EmptyJobException
