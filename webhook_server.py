from flask import Flask, request, jsonify
import hashlib
import os

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's assigned port or default to 5000
    app.run(host="0.0.0.0", port=port)
