from unittest import TestCase
from assertpy import assert_that

from common.constants import INVALID_FEE_TYPE_FROM_CLIENT, AMOUNT_NOT_PRESENT_IN_JOB, USERID_NOT_PRESENT_IN_JOB
from service.payment import PaymentService
from tests.fixtures import job_two_client, job_one_client, invalid_type_job_one, missing_amount_job, missing_user_id_job


class TestPaymentService(TestCase):
    def setUp(self) -> None:
        self.payment_service = PaymentService()

    def test_when_payment_is_created_payment_id_is_returned(self):
        assert_that(self.payment_service.create_new_payment(jobs=[job_one_client, job_two_client])).is_equal_to('11')

    def test_when_create_new_payment_is_called_and_job_is_not_provided_then_return_job_not_provided(self):
        assert_that(self.payment_service.create_new_payment).raises(TypeError).when_called_with().is_equal_to(
            "create_new_payment() "
            "missing 1 required "
            "positional argument: "
            "'jobs'")

    def test_when_create_new_payment_is_called_and_job_has_invalid_type_then_invalid_message_is_returned(self):
        assert_that(self.payment_service.create_new_payment(jobs=[invalid_type_job_one])).is_equal_to(INVALID_FEE_TYPE_FROM_CLIENT)

    def test_when_create_new_payment_is_called_and_payload_does_not_contain_amount_then_amount_not_present_is_returned(self):
        assert_that(self.payment_service.create_new_payment(jobs=[missing_amount_job])).is_equal_to(AMOUNT_NOT_PRESENT_IN_JOB)

    def test_when_create_new_payment_is_called_and_payload_does_not_contain_userid_then_amount_not_present_is_returned(self):
        assert_that(self.payment_service.create_new_payment(jobs=[missing_user_id_job])).is_equal_to(USERID_NOT_PRESENT_IN_JOB)
