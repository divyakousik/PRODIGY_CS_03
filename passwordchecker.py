import re

def check_password_strength(password):

    strength = 0
    feedback = []

    # Check password length
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters.")
    else:
        strength += 1

    # Check for uppercase letters
    if not re.search("[A-Z]", password):
        feedback.append("Password should have at least one uppercase letter.")
    else:
        strength += 1

    # Check for lowercase letters
    if not re.search("[a-z]", password):
        feedback.append("Password should have at least one lowercase letter.")
    else:
        strength += 1

    # Check for numbers
    if not re.search("[0-9]", password):
        feedback.append("Password should have at least one number.")
    else:
        strength += 1

    # Check for special characters
    if not re.search("[^A-Za-z0-9]", password):
        feedback.append("Password should have at least one special character.")
    else:
        strength += 1

    # Assess password strength
    if strength == 5:
        password_strength = "Strong"
    elif strength >= 3:
        password_strength = "Medium"
    else:
        password_strength = "Weak"

    return {"strength": password_strength, "feedback": feedback}

def main():
    password = input("Enter a password: ")
    result = check_password_strength(password)

    print(f"Password Strength: {result['strength']}")
    for feedback in result["feedback"]:
        print(feedback)

if __name__ == "__main__":
    main()