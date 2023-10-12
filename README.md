# Stock Alert System

Keep an eye on your favorite stocks and stay updated with the latest news surrounding them. This Python script tracks the stock price of a specified company and sends an SMS alert along with the latest news headlines if there is a significant change in the stock price.

## Features

- Monitors a specified stock for significant price changes (default is 5%).
- Sends an SMS alert with the price change information.
- Fetches and sends the latest three news articles related to the company via SMS.

## Getting Started

### Prerequisites

- Ensure you have Python installed on your machine.
- Install the necessary Python libraries using the following command:
```bash
pip install requests twilio
```
## Setup

1. Clone the repository or download the files to your machine.
2. Navigate to the project directory in your terminal.
3. Update the script with your credentials and target stock/company information:
    - `ALPHA_VANTAGE_API`: Your Alpha Vantage API Key for fetching stock data.
    - `NEWSAPI_API`: Your NewsAPI Key for fetching news articles.
    - `TWILIO_SID`, `TWILIO_AUTH_TOKEN`: Your Twilio credentials for sending SMS.
    - `TWILIO_PHONE_NUMBER`: Your Twilio phone number.
    - `YOUR_PHONE_NUMBER`: The phone number where you want to receive the alerts.
    - `STOCK`: The stock symbol of the company you want to monitor (e.g., "TSLA" for Tesla).
    - `COMPANY_NAME`: The name of the company (e.g., "Tesla Inc").

## Usage

1. Run the script using the following command:
```bash
python main.py
```

Replace `main.py` with the name you've saved the file as, if different.

The script will check the specified stock's price change and send an SMS alert with the latest news articles if there is a significant price change.

## Built With

- [Python](https://www.python.org/)
- [Requests](https://docs.python-requests.org/en/latest/)
- [Twilio](https://www.twilio.com/)
- [Alpha Vantage](https://www.alphavantage.co/)
- [NewsAPI](https://newsapi.org/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

