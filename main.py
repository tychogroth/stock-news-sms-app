import requests
from twilio.rest import Client

# Define constants for stock, company name, and API credentials
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_VANTAGE_API = ""
NEWSAPI_API = ""
TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""
TWILIO_PHONE_NUMBER = ""
YOUR_PHONE_NUMBER = ""

# Function to get stock price history from Alpha Vantage
def get_stock_price_history():
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": ALPHA_VANTAGE_API
    }
    
    response = requests.get(url, params=params)
    data = response.json()

    return data

# Function to calculate the percentage price change between yesterday and the day before yesterday
def calculate_price_change():
    data = get_stock_price_history()
    dates = list(data["Time Series (Daily)"].keys())
    yesterday_price = float(data["Time Series (Daily)"][dates[0]]["4. close"])
    day_before_yesterday_price = float(data["Time Series (Daily)"][dates[1]]["4. close"])
    
    # Calculate the percentage change
    percent_change = ((yesterday_price - day_before_yesterday_price) / day_before_yesterday_price) * 100
    
    return percent_change

# Function to get the latest three news articles from NewsAPI
def get_news():
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": COMPANY_NAME,
        "apiKey": NEWSAPI_API,
        "pageSize": 3,
        "sortBy": "publishedAt"
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    articles = data["articles"][:3]  # Get the first 3 news articles

    return articles

# Function to send an SMS message via Twilio
def send_sms(message):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,
        to=YOUR_PHONE_NUMBER
    )

# Main script execution
percent_change = calculate_price_change()
if abs(percent_change) >= 5:
    arrow = "🔺" if percent_change > 0 else "🔻"
    change_message = f"{STOCK}: {arrow}{abs(percent_change):.2f}%"
    send_sms(change_message)  # Send the percentage change as a separate message
    
    articles = get_news()
    for article in articles:
        article_message = f"Title: {article['title']}, Description: {article['description']}"
        send_sms(article_message)  # Send each article as a separate message
else:
    print("No big fluctuation!")