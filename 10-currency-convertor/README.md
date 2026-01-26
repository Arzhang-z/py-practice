# 💱 Currency Converter (Streamlit App)

A simple web-based currency converter built with **Python** and **Streamlit**.  
It fetches real-time exchange rates from an external API and allows users to convert between a wide range of global currencies with a clean UI and cached API calls.

---

## 🚀 Features

- Convert between **150+ global currencies**
- Real-time exchange rates via **ExchangeRate-API**
- **Caching** with TTL to reduce API calls and improve performance
- Simple, clean UI built using **Streamlit**
- Input validation and error handling
- Modular project structure

---

## 🗂 Project Structure

```
.
├── app.py # Main Streamlit application
├── Currency_converter.py # Currency conversion & API logic
├── constants.py # Supported currency codes
├── requirements.txt # Project dependencies
└── README.md # Project documentation
```


---

## 🧠 How It Works

1. User selects:
   - Base currency
   - Target currency
   - Amount to convert
2. The app:
   - Fetches the exchange rate from the API
   - Uses a cached result if available
   - Calculates the converted amount
3. Results are displayed using Streamlit metrics and layout columns

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Arzhang-z/currency-converter.git
cd currency-converter
```

Create a virtual environment (recommended):

```python
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## ▶️ Running the App
0. First User exports the Exchange_Rate_API_KEY in terminal session:
```bash
   export Exchange_Rate_API_KEY {Your_Exchange_Rate_API_KEY_from_exchange_rate_api}
```
then run the app
```bash
streamlit run app.py
```

The app will open automatically in your browser.

## 🔐 API Configuration

This project uses ExchangeRate-API.

You will need an API key:

Sign up at ExchangeRate-API

Replace the API key in Currency_converter.py:

url = f"https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest/{base_currency}"

## 🧪 Error Handling

- Network failures

- Invalid currency codes

- API timeouts

- HTTP errors

Errors are handled explicitly and shown to the user instead of failing silently.

## 📚 Things I Learned in This Project

- How to build interactive web apps using Streamlit

- Structuring a Python project into reusable modules

- Fetching and parsing data from a REST API using requests

- Why silent failures are dangerous and how to handle errors properly

- Using cachetools (TTLCache) to optimize API usage

- Basic frontend layout techniques in Streamlit (columns, metrics, markdown)

- The importance of validating external data before using it

- How small indentation and structure mistakes can break Python programs

## 📄 License
This project is for educational purposes