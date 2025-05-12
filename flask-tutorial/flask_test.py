from flask import Flask, jsonify, render_template

# Initialize Flask application
app1 = Flask(__name__)

# Route for home page
@app1.route('/')
def home():
    return render_template('index.html', title="Welcome to Flask")

# Route for API
@app1.route('/api')
def api():
    return jsonify({"message": "This is a simple Flask API"})

@app1.route('/hi')
def hi():
    return jsonify({"message": "Hi from Megha"})

if __name__ == '__main__':
    # Run the application in debug mode (reloads automatically)
    app1.run(debug=True)