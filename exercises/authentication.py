class InvalidUsernameOrPassword(Exception):
    """Raised when the username or password is incorrect."""
    pass

class AccountLocked(Exception):
    """Raised when the account is locked after multiple failed attempts."""
    pass

class InsufficientPrivileges(Exception):
    """Raised when a user does not have sufficient privileges."""
    pass

class AuthSystem:
    def __init__(self):
        # Predefined username and password
        self.username = "admin"
        self.password = "password123"
        # Privileges dictionary for user roles
        self.privileges = {"admin": "all_access", "user": "limited_access"}
        # Maximum number of allowed attempts
        self.max_attempts = 3
        self.attempts = 0
        self.locked = False
