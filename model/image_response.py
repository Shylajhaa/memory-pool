class ImageResponse:
    def __init__(self, image_id, user_id, response_type, value) -> None:
        self.image_id = image_id
        self.user_id = user_id
        self.response_type = response_type
        self.value = value