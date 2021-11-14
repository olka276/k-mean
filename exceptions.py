class Error(Exception):
    pass


class UnevenDimensionsError(Error):
    def __init__(self, message):
        self.message = message
