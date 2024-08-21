import requests
import random
import string
import time

# Function to generate random user data
def generate_random_data():
    first_name = ''.join(random.choices(string.ascii_lowercase, k=5)).capitalize()
    last_name = ''.join(random.choices(string.ascii_lowercase, k=7)).capitalize()
    email = f"{first_name.lower()}.{last_name.lower()}@dlook.com"
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    phone_number = f"+1{random.randint(1000000000, 9999999999)}"
    return first_name, last_name, email, password, phone_number

# Function to simulate a session
def create_session(user_agent):
    headers = {
        'User-Agent': user_agent
    }
    session = requests.Session()
    session.headers.update(headers)
    return session

# Function to print logo
def print_logo():
    logo = """
    =========================
    |      Rajput                                   |
    |      tool free Auto Facebook    |
    =========================
    """
    print(logo)

# Function to simulate email verification
def verify_email(email):
    print(f"Verifying email: {email}")
    time.sleep(2)  # Simulate delay for verification
    return True

# Function to simulate OTP generation and verification
def generate_otp():
    return ''.join(random.choices(string.digits, k=5))

# Main function to execute the registration process
def main():
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    print_logo()
    
    first_name, last_name, email, password, phone_number = generate_random_data()
    print(f"Generated User Data:\nName: {first_name} {last_name}\nEmail: {email}\nPhone: {phone_number}\nPassword: {password}")
    
    session = create_session(user_agent)
    
    if verify_email(email):
        otp = generate_otp()
        print(f"Your OTP is: {otp}")
        user_otp = input("Enter the OTP sent to your email: ")
        
        if user_otp == otp:
            print("Registration successful!")
        else:
            print("Invalid OTP. Registration failed.")
    else:
        print("Email verification failed.")

if __name__ == "__main__":
    main()
