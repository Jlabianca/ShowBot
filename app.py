from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample movie data for recommendations
movies = [
    {'title': 'Suggested Show 1', 'image': 'https://placehold.co/100x150', 'description': 'Description for suggested show 1.'},
    {'title': 'Suggested Movie 2', 'image': 'https://placehold.co/100x150', 'description': 'Description for suggested movie 2.'}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_suggestions', methods=['POST'])
def get_suggestions():
    recent_watched = request.form['recent_watched']
    # Here you would normally process the recent_watched data and generate suggestions
    # For now, we'll just return the sample data
    return jsonify(movies)

if __name__ == '__main__':
    app.run(debug=True)
