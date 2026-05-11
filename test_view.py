from flask import Flask, render_template
import os

# این بخش به پایتون می‌گوید دقیقاً برو داخل پوشه app و بعد templates
base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, 'app', 'templates')

app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/books')
def books():
    return render_template('books.html')

if __name__ == '__main__':
    print(f"--- Templates are loading from: {template_dir} ---")
    app.run(debug=True, port=8000)