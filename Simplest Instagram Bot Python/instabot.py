import requests

ACCESS_TOKEN = "your token"
INSTAGRAM_ACCOUNT_ID = "your id"

def get_user_id(username):
    """Get the Instagram User ID from a username."""
    url = f"https://graph.facebook.com/v18.0/{INSTAGRAM_ACCOUNT_ID}"
    params = {
        "fields": f"business_discovery.username({username}){{id}}",
        "access_token": ACCESS_TOKEN
    }
    
    response = requests.get(url, params=params)
    data = response.json()

    if "error" in data:
        print("Error retrieving user ID:", data)
        return None

    user_id = data.get("business_discovery", {}).get("id")
    
    if user_id:
        return user_id
    else:
        print("User ID not found.")
        return None

# Example Usage:
user_id = get_user_id("doston__ruziyev")
print("User ID:", user_id)

def send_dm(username, message):
    """Get User ID and Send a DM"""
    user_id = get_user_id(username)
    
    if not user_id:
        print("User ID not found. Cannot send message.")
        return

    url = f"https://graph.facebook.com/v18.0/{INSTAGRAM_ACCOUNT_ID}/messages"
    params = {
        "recipient": {"id": user_id},
        "message": {"text": message},
        "access_token": ACCESS_TOKEN
    }
    response = requests.post(url, json=params)
    print(response.json())

# Example Usage
send_dm("doston__ruziyev", "Hello from the Instagram API!")