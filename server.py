import os
import requests
from flask import Flask, jsonify, request
from datetime import datetime

@app.route("/btc-history")
def btc_history():
    try:
        # Récupération des paramètres d'URL
        interval = request.args.get("interval", "day")  # "minute", "hour", "day"
        limit = int(request.args.get("limit", 2000))    # max 2000
        tsym = request.args.get("tsym", "USD")

        # Construction de l’URL vers CryptoCompare
        interval_map = {
            "minute": "histominute",
            "hour": "histohour",
            "day": "histoday"
        }
        if interval not in interval_map:
            return jsonify({"error": "Invalid interval. Use 'minute', 'hour' or 'day'"}), 400

        url = f"https://min-api.cryptocompare.com/data/v2/{interval_map[interval]}?fsym=BTC&tsym={tsym}&limit={limit}"
        response = requests.get(url)
        data = response.json()["Data"]["Data"]

        # Formatage des données
        result = []
        for d in data:
            result.append({
                "timestamp": datetime.utcfromtimestamp(d["time"]).isoformat() + "Z",
                "open": d["open"],
                "high": d["high"],
                "low": d["low"],
                "close": d["close"],
                "volume_from": d.get("volumefrom"),
                "volume_to": d.get("volumeto")
            })

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500




