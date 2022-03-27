import enum
from utils.model import Model

class ResponseType(enum):
    LIKE = 1
    COMMENT = 2

class ImageResponse(Model):
    def __init__(self, image_id, user_id, response_type, value = None) -> None:
        self.image_id = image_id
        self.user_id = user_id
        self.response_type = ResponseType(response_type)
        self.value = value
