import secrets
import string

def generate_secure_password(length=12):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+?"

    # Ensure at least one character from each category
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    all_characters = lowercase + uppercase + digits + symbols

    while len(password) < length:
        password.append(secrets.choice(all_characters))

    secrets.SystemRandom().shuffle(password)

    return "".join(password)

print("Secure Password:", generate_secure_password())
