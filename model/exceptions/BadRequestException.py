class BadRequestException(Exception):
    def __init__(self, message="Bad Request"):
        self.message = message
        super().__init__(self.message)
