import requests
from send_email import send_news


# user to enter their API key
api_key = input("Please enter your API key: ")

# You can let users customize the topic and country
topic = input("Enter a topic (e.g., 'gaming'): ") or "gaming"
country = input("Enter a country code (e.g., 'us', 'tw'): ") or "tw"

# Construct the API URL
url = f"https://newsdata.io/api/1/news?apikey={api_key}&q={topic}&country={country}&category=entertainment"

try:
    # Send GET request
    response = requests.get(url)
    response.raise_for_status()
    content = response.json()
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    exit()

# Construct the email body
body = "Subject: 遊戲新聞\n\n"

for article in content["results"]:
    body = body + article["title"] + "\n" + article["description"][len(article["title"]) - 2:] + "\n" + article["link"] + 2 * "\n"

# Ensure body is encoded as UTF-8
body = body.encode("utf-8")

# Send the email
send_news(messages=body)
