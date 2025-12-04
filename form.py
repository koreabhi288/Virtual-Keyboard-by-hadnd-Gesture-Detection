from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    # Here, you can add code to save the data to a database or perform other actions
    return f"Registered successfully! Username: {username}, Email: {email}"

if __name__ == "__main__":
    app.run(debug=True)
