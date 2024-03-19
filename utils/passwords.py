import hashlib
import secrets


class PasswordManager:
    @staticmethod
    def hash_password(password: str, salt: bytes) -> str:
        """
        Hashes the given password using SHA3-512 algorithm with the provided salt.

        Args:
            password (str): The password to hash.
            salt (bytes): The salt used in hashing.

        Returns:
            str: The hashed password.
        """
        password_salt = password.encode() + salt
        hashed_password = hashlib.sha3_512(password_salt).hexdigest()
        return hashed_password

    @staticmethod
    def generate_salt(length: int = 16) -> bytes:
        """
        Generates a random salt of the specified length.

        Args:
            length (int): The length of the salt. Default is 16.

        Returns:
            bytes: The generated salt.
        """
        return secrets.token_bytes(length)

    @staticmethod
    def verify_password(hashed_password: str, password: str, salt: bytes) -> bool:
        """
        Verifies if the provided password matches the hashed password using the given salt.

        Args:
            hashed_password (str): The hashed password to compare against.
            password (str): The password to verify.
            salt (bytes): The salt used in hashing.

        Returns:
            bool: True if the passwords match, False otherwise.
        """
        return hashed_password == PasswordManager.hash_password(password, salt)
