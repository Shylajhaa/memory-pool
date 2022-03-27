from utils.model import Model

class Image(Model):
    def __init__(self, caption, image_url, created_by) -> None:
        self.caption = caption
        self.image_url = image_url
        self.created_by = created_by