
# hihito Bot 🤖✨

Welcome to **hi hito**! This script is your AI-powered bestie that chills on LinkedIn posts, looks for specific keywords in comments, and slides in with replies like a pro. 💬✨

---

## What This Does 🤔
- 🕵️ **Monitors Comments:** Watches LinkedIn comments like it’s bingeing a Netflix series.
- 🔍 **Keyword Detective:** Detects keywords in comments. Someone says "need a referral for Zepto"? Boom. Got it.
- 💥 **Replies with Mentions:** Drops a tailored reply with an @mention to flex your networking game.

---

## How It Works 🛠️

1. **Cookies First 🍪**:
   - Saves LinkedIn login cookies so you’re logged in like a boss.
   - No more manual logging in every time. Work smarter, not harder. 😎

2. **Detect & Respond 🕶️**:
   - Scans comments for your keyword (like "I need a referral for Zepto").
   - Replies with a custom message like "Check out @Renuka Rajpuria."

3. **Rinse & Repeat 🔄**:
   - Keeps scrolling, finding, and replying. Your new social media manager!

---

## How to Run This Baddie 🏃‍♂️💨

### Prerequisites 📝
- Python 3.8+ 🐍
- Some decent Wi-Fi to vibe with 🌐
- A LinkedIn account (duh!)

### Step 1: Install the Requirements 🛠️
```bash
pip install selenium webdriver-manager
```

### Step 2: Update Your Deets ✍️
In the `login_to_linkedin` function, replace these with your LinkedIn creds:
```python
username.send_keys("your-email@example.com")  # Your LinkedIn email
password.send_keys("your-password")          # Your LinkedIn password
```
### Step 3: Get Your Post URL 🖇️
Find the LinkedIn post URL you wanna stalk. Example:
```python
post_url = "https://www.linkedin.com/feed/update/urn:li:activity:7213119857825861632/"
```

### Step 4: Run the Script 🚀
```bash
python your_script_name.py
```

---

## Cool Features You’ll Love 😍
- **AI Mentions:** Adds mentions like a ninja – no manual effort.
- **Auto Scrolling:** Goes through every comment. No FOMO here.
- **Cookie Magic:** Logs in fast AF with saved cookies.

---

## Gen-Z Warnings ⚠️
- **Use Responsibly:** Don’t spam people. Nobody likes a LinkedIn ghostbuster. 👻
- **Keyword Matters:** Update the keyword and response text to keep it real.
- **Browser Pops Up:** A browser will launch – don’t freak out. It’s working, okay?

---

## FAQs 🤓
### Q1. Why is it not replying?
- Check your keyword. Are you even spelling it right, bruh? 😅

### Q2. Can I add more keywords?
- Yup. Customize `keyword` and `response` in the `monitor_and_respond` function.

### Q3. What’s with the cookies?
- It saves login cookies so you don’t need to type creds every time. Think of it as your digital vault. 🗄️

---

## License 🛡️
MIT License. Do what you want with it, but don’t get in trouble. 😇

---

Made with 💙 by Resquare✨
