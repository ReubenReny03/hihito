import time
import os
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Set up WebDriver
COOKIE_FILE = "linkedin_cookies.pkl"
chrome_options = Options()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


def save_cookies(driver, file_path):
    """Save cookies to a file."""
    with open(file_path, "wb") as file:
        pickle.dump(driver.get_cookies(), file)


def load_cookies(driver, file_path):
    """Load cookies from a file."""
    if os.path.exists(file_path):
        with open(file_path, "rb") as file:
            cookies = pickle.load(file)
            for cookie in cookies:
                driver.add_cookie(cookie)


def login_to_linkedin():
    """Log in to LinkedIn if cookies are not available."""
    driver.get("https://www.linkedin.com/login")
    time.sleep(5)  # Wait for the login page to load

    # Enter username and password
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")

    username.send_keys("your-email@example.com")  # Replace with your LinkedIn email
    password.send_keys("your-password")  # Replace with your LinkedIn password

    # Submit the login form
    password.send_keys(Keys.RETURN)
    time.sleep(5)  # Wait for LinkedIn to log in

    # Save cookies after login
    save_cookies(driver, COOKIE_FILE)


def reply_to_comment(comment_element, response_text):
    """Click the reply button and post a response with mention."""
    try:
        # Find and click the "Reply" button
        reply_button = comment_element.find_element(By.CSS_SELECTOR, "button[aria-label^='Reply']")
        driver.execute_script("arguments[0].click();", reply_button)
        time.sleep(2)  # Wait for the reply editor to open

        # Locate the reply box within the comment element
        reply_box = comment_element.find_element(By.CSS_SELECTOR, "div.comments-comment-box--reply div[contenteditable='true']")
        reply_box.click()
        time.sleep(1)  # Ensure the box is active

        # Split the response text at the '@' symbol to identify the mention
        before_mention, mention_name = response_text.split("@")
        mention_name = mention_name.strip()  # Remove any leading/trailing whitespace

        # Type the text before the mention
        reply_box.send_keys(before_mention + "@")
        time.sleep(1)

        # Type the mention name
        reply_box.send_keys(mention_name)
        time.sleep(2)  # Wait for the mention suggestions to load

        # Press DOWN and ENTER to select the first suggestion
        reply_box.send_keys(Keys.DOWN)
        time.sleep(0.5)
        reply_box.send_keys(Keys.ENTER)
        time.sleep(1)

        # If there's any text after the mention, type it
        # (Modify as needed if you have text after the mention)

        # Submit the reply
        submit_button = comment_element.find_element(By.CSS_SELECTOR, "button.comments-comment-box__submit-button--cr")
        driver.execute_script("arguments[0].click();", submit_button)
        print(f"Replied with: {response_text}")
        time.sleep(2)  # Wait for the comment to post
    except Exception as e:
        print(f"Error during reply: {e}")


def monitor_and_respond(post_url):
    # Define the keyword and response
    keyword = "need a referal for zepto"  # The keyword to look for in comments
    # AI ----- Hito 
    response = "check out @Renuka Rajpuria"  # The response to post

    driver.get(post_url)
    time.sleep(5)  # Wait for the page to load

    while True:
        try:
            # Scroll to load comments
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)  # Wait for comments to load

            # Find all comments
            comments = driver.find_elements(By.CSS_SELECTOR, ".comments-comment-entity")
            for comment in comments:
                try:
                    # Extract the comment text
                    comment_text = comment.find_element(By.CSS_SELECTOR, ".comments-comment-item__main-content").text
                    print("Found comment:", comment_text)

                    # Check if the comment matches the keyword
                    if comment_text.strip().lower() == keyword.lower():
                        print("Keyword match found. Responding...")
                        reply_to_comment(comment, response)
                except Exception as e:
                    print(f"Error processing comment: {e}")

            # Refresh to check for new comments
            time.sleep(10)  # Adjust based on frequency of checking
            driver.refresh()
        except Exception as e:
            print(f"Error monitoring comments: {e}")
            break


def main():
    post_url = "https://www.linkedin.com/feed/update/urn:li:activity:7213119857825861632/"
    try:
        print("Starting script...")

        # Load cookies or log in
        driver.get("https://www.linkedin.com")
        if os.path.exists(COOKIE_FILE):
            load_cookies(driver, COOKIE_FILE)
            driver.refresh()
            time.sleep(5)
        else:
            login_to_linkedin()

        # Monitor the post and respond to comments
        monitor_and_respond(post_url)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
