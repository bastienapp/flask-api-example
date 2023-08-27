from enum import Enum

class OrderStatus(str, Enum):
    PENDING = 'Pending'
    ONGOING = 'Ongoing'
    COMPLETE = 'Completed'
    DELIVERED = 'Delivered'
    CANCELLED = 'Cancelled'