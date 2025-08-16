from flask import Flask, request, jsonify, render_template
from chatbot_logic import generate_response

app = Flask(__name__)

# ✅ This route renders your frontend UI
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data['message']
    bot_reply = generate_response(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == '__main__':
    app.run(debug=True)

