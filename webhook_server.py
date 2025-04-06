from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

# Replace with your real token & endpoint
VERIFICATION_TOKEN = "Bet365Welcomebonus"
ENDPOINT_URL = "https://yourdomain.com/ebay-webhook"

@app.route("/ebay-webhook", methods=["POST"])
def ebay_webhook():
    data = request.json

    # eBay webhook verification
    if "challengeCode" in data:
        challenge_code = data["challengeCode"]
        combined = challenge_code + VERIFICATION_TOKEN + ENDPOINT_URL
        hashed = hashlib.sha256(combined.encode("utf-8")).hexdigest()
        return jsonify({"challengeResponse": hashed}), 200

    print("📦 Received eBay webhook payload:", data)
    return "", 200
