import bcrypt


class PasswordManager:
    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hashes the given password using bcrypt algorithm with a random salt.

        Args:
            password (str): The password to hash.

        Returns:
            str: The hashed password as a string.
        """
        salt = bcrypt.gensalt(13)
        hashed_password_bytes = bcrypt.hashpw(password.encode('utf-8'), salt)
        hashed_password_str = hashed_password_bytes.decode('utf-8')
        return hashed_password_str

    @staticmethod
    def verify_password(hashed_password: str, password: str) -> bool:
        """
        Verifies if the provided password matches the hashed password using bcrypt.

        Args:
            hashed_password (str): The hashed password to compare against.
            password (str): The password to verify.

        Returns:
            bool: True if the passwords match, False otherwise.
        """
        try:
            hashed_password_bytes = hashed_password.encode('utf-8')
            return bcrypt.checkpw(password.encode('utf-8'), hashed_password_bytes)
        except (ValueError, TypeError):
            return False
