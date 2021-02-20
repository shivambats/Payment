import unittest

from data.models.common.constants import FeeType
from data.models.job import Job
from assertpy import assert_that
from data.models.exceptions.job import AmountNotPresentException, UserIDNotPresentException, FeeTypeNotPresentException

fake_user_id = 1


class TestJobModel(unittest.TestCase):
    def test_when_job_is_initialized_required_params_are_provided(self):
        job_one = Job(amount=-18, user_id=fake_user_id, fee_type=FeeType.Tax)
        assert_that(job_one.amount).is_equal_to(-18)
        assert_that(job_one.user_id).is_equal_to(fake_user_id)
        assert_that(job_one.fee_type).is_equal_to(FeeType.Tax)

    def test_when_job_is_created_and_amount_is_not_given_then_amount_not_present_exception_is_raised(self):
        assert_that(Job).raises(AmountNotPresentException).when_called_with(user_id=fake_user_id, fee_type=FeeType.ServiceFee)

    def test_when_job_is_created_and_userid_is_not_given_then_userid_not_present_exception_is_raised(self):
        assert_that(Job).raises(UserIDNotPresentException).when_called_with(amount=20, fee_type=FeeType.ServiceFee)

    def test_when_job_is_created_and_feetype_is_not_given_then_feetype_not_present_exception_is_raised(self):
        assert_that(Job).raises(FeeTypeNotPresentException).when_called_with(amount=10, user_id=fake_user_id)
