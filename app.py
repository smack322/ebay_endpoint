from flask import Flask, request, jsonify
app = Flask(__name__)

@app.get("/health")
def health():
    return {"ok": True}, 200


VERIFY_TOKEN = os.getenv("EBAY_VERIFICATION_TOKEN", "")  # your chosen secret
ENDPOINT_URL = os.getenv("EBAY_ENDPOINT_URL", "")        # must EXACTLY match eBay form

@app.get("/ebay/madn")
def ebay_madn_challenge():
    cc = request.args.get("challenge_code")  # comes from eBay; do NOT store
    if not (cc and VERIFY_TOKEN and ENDPOINT_URL):
        return jsonify({"error": "misconfigured"}), 500
    digest = hashlib.sha256((cc + VERIFY_TOKEN + ENDPOINT_URL).encode("utf-8")).hexdigest()
    return jsonify({"challengeResponse": digest}), 200

@app.post("/ebay/madn")
def ebay_madn():
    payload = request.get_json(silent=True) or {}
    # TODO: handle deletion/closure here
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    # Render injects PORT; default to 8080 for local dev
    import os
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
