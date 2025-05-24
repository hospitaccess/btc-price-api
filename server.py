from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/btc-price")
def btc_price():
    binance_url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = requests.get(binance_url)
    data = response.json()
    return jsonify({"btc_price_usdt": data["price"]})

if __name__ == "__main__":
    app.run(debug=True, port=5001)

