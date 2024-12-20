from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/twitter.html')
def page_1():
    return render_template('twitter.html')

@app.route('/weed.html')
def page_2():
    return render_template('weed.html')

# Home route
@app.route('/')
def home():
    return render_template("layout.html")

# About route
@app.route('/about')
def about():
    return render_template("voting.html")
# JSON response route
@app.route('/api/data')
def get_data():
    data = {"message": "Hello, this is a JSON response!", "status": "success"}
    return jsonify(data)


# Route to handle POST requests
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        data = request.form.get('data', 'No data submitted')
        return f"<h1>Form Submitted</h1><p>You entered: {data}</p>"
    return '''
        <form method="POST" action="/submit">
            <label for="data">Enter something:</label>
            <input type="text" id="data" name="data">
            <button type="submit">Submit</button>
        </form>
    '''

# Custom 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Page not found!</p>", 404

if __name__ == '__main__':
    app.run(debug=True)