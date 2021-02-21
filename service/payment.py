from common.constants import INVALID_FEE_TYPE_FROM_CLIENT, AMOUNT_NOT_PRESENT_IN_JOB, USERID_NOT_PRESENT_IN_JOB
from data.models.exceptions.job import AmountNotPresentException, UserIDNotPresentException
from data.models.job import Job
from data.models.payment import Payment


class PaymentService:
    @staticmethod
    def create_new_payment(jobs):
        try:
            job_arr = [Job(**job) for job in jobs]
        except TypeError as error:
            if str(error) == "Fee Type is invalid":
                return INVALID_FEE_TYPE_FROM_CLIENT
        except AmountNotPresentException:
            return AMOUNT_NOT_PRESENT_IN_JOB
        except UserIDNotPresentException:
            return USERID_NOT_PRESENT_IN_JOB
        else:
            return Payment(job=job_arr).save()
