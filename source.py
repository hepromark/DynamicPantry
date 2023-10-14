from flask import Flask

# Create instance
app = Flask(__name__)
print("hello world")

# How to access home
@app.route("/")  # "/" for the default landing page
# Home page
def home():
    # Returns in-line HTML
    return "Hello! this is the main page <h1>HELLO<h1>"

# Run app
if __name__ == "__main__":
    app.run()

