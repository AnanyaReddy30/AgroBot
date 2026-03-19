from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    # Simple intelligent logic (replace later with AI model)
    if "irrigation" in user_input.lower():
        reply = "Drip irrigation is best for saving water."
    elif "fertilizer" in user_input.lower():
        reply = "Use compost or NPK based on soil test."
    else:
        reply = "I can help with crops, soil, irrigation, and farming 
advice."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run()
