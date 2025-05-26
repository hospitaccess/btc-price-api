import os
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "BTC API is running"

@app.route("/btc-price")
def btc_price():
    coingecko_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(coingecko_url)
    data = response.json()
    
    # Sécurisation en cas d'erreur inattendue
    if "bitcoin" not in data or "usd" not in data["bitcoin"]:
        return jsonify({"error": "Price not found", "response": data}), 500

    return jsonify({"btc_price_usdt": data["bitcoin"]["usd"]})

if __name__ == "__main__":
    print("Available routes: / and /btc-price")
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)



