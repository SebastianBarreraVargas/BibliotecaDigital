class NotAuthorizedException(Exception):
    def __init__(self, message="Not Authorized"):
        self.message = message
        super().__init__(self.message)