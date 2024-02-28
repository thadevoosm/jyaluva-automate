from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.methods == 'POST':
        print(request.json)
        return 'scucess', 200
    else:
        abort(400)

if __name__ == '__main__':
    app.run()