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

    print("Binance response:", data)  # Affiche ce qui arrive

    # Vérifie si 'price' est bien là
    if "price" in data:
        return jsonify({"btc_price_usdt": data["price"]})
    else:
        return jsonify({"error": "Price not found", "response": data}), 500

if __name__ == "__main__":
    print("✅ Flask app starting with routes / and /btc-price")
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


