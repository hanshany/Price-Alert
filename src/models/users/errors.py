__author__ = 'Yolanda'


class UserError(Exception):
    # contain everything that the exception contains and potentially something more
    def __init__(self, message):
        # another program can access this message
        self.message = message


class UserNotExistsError(UserError):
    pass

class IncorrectPasswordError(UserError):
    pass

class UserAlreadyRegisteredError(UserError):
    pass

class InvalidEmailError(UserError):
    pass


