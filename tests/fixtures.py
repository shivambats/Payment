from data.models.common.constants import FeeType
from data.models.job import Job

fake_user_one = 1223
fake_user_two = 2234

job_one = Job(amount=19.2, fee_type=FeeType.ServiceFee, user_id=fake_user_one)
job_two = Job(amount=18, fee_type=FeeType.Tax, user_id=fake_user_two)
