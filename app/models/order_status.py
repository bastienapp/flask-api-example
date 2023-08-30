from enum import Enum


class OrderStatus(str, Enum):
    PENDING = 'Pending'
    ONGOING = 'Ongoing'
    COMPLETE = 'Completed'
    DELIVERED = 'Delivered'
    CANCELLED = 'Cancelled'

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_
