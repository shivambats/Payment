from data.models.common.constants import FeeType
from data.models.job import Job

fake_user_one = 1223
fake_user_two = 2234

job_one = Job(amount=19.2, fee_type='ServiceFee', user_id=fake_user_one)
job_two = Job(amount=18, fee_type='Tax', user_id=fake_user_two)

job_one_client = {'amount': 20, 'fee_type': 'ServiceFee', 'user_id': 1234}
job_two_client = {'amount': 30, 'fee_type': 'Tax', 'user_id': 1234}

invalid_type_job_one = {'amount': 21, 'fee_type': 'SomeRandomTypeHere', 'user_id': 1234}
missing_amount_job = {'fee_type': 'ServiceFee', 'user_id': 1234}
missing_user_id_job = {'amount': 12, 'fee_type': 'ServiceFee'}
