import os
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "BTC API is running"

@app.route("/btc-price")
def btc_price():
    binance_url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = requests.get(binance_url)
    data = response.json()
    print(data)  # Pour debug, à retirer en prod

    # Vérifie que la clé "price" existe
    if "price" not in data:
        return jsonify({"error": "Price not found in response"}), 500

    return jsonify({"btc_price_usdt": data["price"]})

if __name__ == "__main__":
    print("✅ Flask app starting with routes / and /btc-price")
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


