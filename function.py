import re
# Function to check if a user exists
def user_exists(username, users):
    return username in users
# Function for user registration with enhanced features
def register(username, password, email, users):
    if user_exists(username, users):
        return "Error: Username already exists. Please choose a different one."
    if not is_valid_email(email):
        return "Error: Invalid email format."
    # Validate the password
    if not is_valid_password(password):
        return "Error: Password does not meet the criteria. It should be at least 8 characters long, contain 1 numeric, 1 capital letter, and 1 symbol."
    users[username] = {'password': password, 'email': email}
    return "Registration successful."
# Function for user login
def login(username, password, users):
    if not user_exists(username, users):
        return "Error: Username does not exist."
    if users[username]['password'] == password:
        return "Login successful."
    return "Error: Incorrect password."

# Function to validate the email
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

# Function to validate the password
def is_valid_password(password):
    if len(password) < 8:
        return False
    if not any(char.isnumeric() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

# Example usage
users = {}  # This dictionary will store registered users and their passwords
# Ask if the user is already registered
existing_user = input("Do you already have an account? (yes/no): ").lower()

if existing_user == "yes":
    # User wants to log in
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    login_result = login(username, password, users)
    print(login_result)
else:
    # User wants to register
    username = input("Enter your desired username: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    register_result = register(username, password, email, users)
    if "successful" in register_result:
        # If registration is successful, prompt the user to log in
        username = input("Registration successful. Please log in. Enter your username: ")
        password = input("Enter your password: ")
        login_result = login(username, password, users)
        print(login_result)
    else:
        print(register_result)
