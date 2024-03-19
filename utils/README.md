# UTILS

### passwords
- The passwords util class hashes and compares passwords
```commandline
# Example password
    password = "secretpassword"

    # Hash the password with the generated salt
    hashed_password = PasswordManager.hash_password(password)

    # Verification
    is_verified = PasswordManager.verify_password(hashed_password, password)
```