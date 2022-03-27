import enum

class ConnectionStatus(enum):
    REQUESTED = 1

class Connection:
    def __init__(self, follower, following) -> None:
        self.follower = follower
        self.following = following
        self.status = ConnectionStatus.REQUESTED
