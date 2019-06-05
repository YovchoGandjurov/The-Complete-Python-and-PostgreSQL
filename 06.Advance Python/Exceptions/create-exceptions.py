class MissingLabelError(KeyError):
    pass


class PageNotFoundError(LookupError):
    pass


class IncorrectPasswordError(ValueError):
    pass


class IncorrectUsernameError(ValueError):
    pass


class APIThrottleLimitError(RuntimeError):
    pass


# Program... user entes wrong username
def login():
    raise IncorrectUsernameError

try:
    login()
except IncorrectUsernameError:
    print("Your username was incorrect.")
except IncorrectPasswordError:
    print("Your password was incorrect.")
