import bcrypt


class PasswordManager:
    @staticmethod
    def hash_password(password: str) -> bytes:
        """
        Hashes the given password using bcrypt algorithm with a random salt.

        Args:
            password (str): The password to hash.

        Returns:
            bytes: The hashed password.
        """
        salt = bcrypt.gensalt(13)
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    @staticmethod
    def verify_password(hashed_password: bytes, password: str) -> bool:
        """
        Verifies if the provided password matches the hashed password using bcrypt.

        Args:
            hashed_password (bytes): The hashed password to compare against.
            password (str): The password to verify.

        Returns:
            bool: True if the passwords match, False otherwise.
        """
        try:
            return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
        except (ValueError, TypeError):
            return False
