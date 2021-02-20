from enum import Enum


class FeeType(Enum):
    ServiceFee = 1
    ItemPrice = 2
    Tip = 3
    Tax = 4


class PaymentStatus(Enum):
    CREATED = 1
    ON_HOLD = 2
    SENT_TO_PSP = 3
    PARTIALLY_PROCESSED = 4
    PROCESSED = 5
