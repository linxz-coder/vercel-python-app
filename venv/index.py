from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__, static_url_path='/static')
openai.api_key = "your_api_key" # you can get it from https://platform.openai.com/account/api-keys
chat_history = []


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json['input']
    chat_history.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_history,
        temperature=0,
        stream=False,
    )
    chat_output = response.choices[0]['message']['content']
    return jsonify({'output': chat_output})
    

if __name__ == '__main__':
    app.run(debug=True)