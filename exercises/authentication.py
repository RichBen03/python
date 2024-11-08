class InvalidUsernameOrPassword(Exception):
    """Raised when the username or password is incorrect."""
    pass

class AccountLocked(Exception):
    """Raised when the account is locked after multiple failed attempts."""
    pass

class InsufficientPrivileges(Exception):
    """Raised 