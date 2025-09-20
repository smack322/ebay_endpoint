from flask import Flask, request, jsonify
app = Flask(__name__)

@app.get("/health")
def health():
    return {"ok": True}, 200

@app.post("/ebay/madn")
def ebay_madn():
    payload = request.get_json(silent=True) or {}
    # TODO: handle deletion/closure here
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    # Render injects PORT; default to 8080 for local dev
    import os
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
