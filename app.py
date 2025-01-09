from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the routes and corresponding view functions
@app.route('/')
def home():
    return render_template('index.html')  # Renders the 'index.html' template

@app.route('/about')
def about():
    return render_template('about.html')  # Renders the 'about.html' template

@app.route('/membership')
def membership():
    return render_template('membership.html')  # Renders the 'membership.html' template

# Run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
