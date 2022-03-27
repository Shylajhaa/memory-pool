import enum
from utils.model import Model

class ConnectionStatus(enum):
    REQUESTED = 1

class Connection(Model):
    def __init__(self, follower, following) -> None:
        self.follower = follower
        self.following = following
        self.status = ConnectionStatus.REQUESTED
