import enum

class OrderStatus(enum.Enum):
    pending = 'Pending'
    ongoing = 'Ongoing'
    completed = 'Completed'
    delivered = 'Delivered'
    cancelled = 'Cancelled'