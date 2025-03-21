from flask import Flask, render_template

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return render_template("index.html")

# Route for robots.txt
@app.route('/robots.txt')
def robots():
    return """
    User-agent: * \n
    Allow: /secret \n
    Disallow: /flag.txt \n
    """

# Route for flag.txt
@app.route('/secret/flag.txt')
def flag():
    # Open flag.txt in read-only mode and return its content
    try:
        with open("flag.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "Flag not found! Contact the administrator.", 404

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)
