from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password):
    """
    Hashes the provided password using Werkzeug's generate_password_hash function.

    Parameters:
    - password (str): The password to be hashed.

    Returns:
    - str: The hashed password.
    """

    return generate_password_hash(password)

def check_password(password, hash):
    """
    Checks if the provided password matches the hashed password.

    Parameters:
    - password (str): The password to be checked.
    - hash (str): The hashed password to compare against.

    Returns:
    - bool: True if the password matches the hash, False otherwise.
    """
    return check_password_hash(hash, password)
