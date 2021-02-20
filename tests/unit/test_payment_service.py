import unittest
from assertpy import assert_that
from data.models.payment import Payment
from data.models.common.constants import PaymentStatus
from data.models.exceptions.payment import JobNotPresentException, EmptyJobException, InvalidJobTypeException
from tests.fixtures import job_one, job_two


class TestPaymentService(unittest.TestCase):
    def test_payment_initialization(self):
        payment_one = Payment(job=[job_one, job_two])
        assert_that(payment_one.job).is_equal_to([job_one, job_two])
        assert_that(payment_one.status).is_equal_to(PaymentStatus.CREATED)

    def test_payment_initialization_when_job_is_an_empty_list_then_empty_job_list_exception_is_raised(self):
        assert_that(Payment).raises(EmptyJobException).when_called_with(job=[])

    def test_payment_initialization_when_job_is_not_in_params_then_job_not_present_exception_is_raised(self):
        assert_that(Payment).raises(JobNotPresentException).when_called_with()

    def test_payment_initialization_when_job_is_not_a_list_then_invalid_job_type_exception_is_raised(self):
        assert_that(Payment).raises(InvalidJobTypeException).when_called_with(job='JOB')
