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

    def login(self, username_input, password_input):
        # Check if the account is locked
        if self.locked:
            raise AccountLocked("Account is locked due to multiple failed login attempts.")
        
        if username_input == self.username and password_input == self.password:
            print("Login successful!")
            self.attempts = 0  # Reset attempts after a successful login
            return True
        else:
            self.attempts += 1
            if self.attempts >= self.max_attempts:
                self.locked = True
                raise AccountLocked("Account is locked due to multiple failed login attempts.")
            raise InvalidUsernameOrPassword("Incorrect username or password. Please try again.")
