from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/printHello', methods=['GET'])
def print_hello():
    return jsonify(message='Hello, world!')

@app.route('/api/modifyRecipe', methods=['POST'])
def modify_recipe():
    # Get the recipe data from the request
    recipe_data = 1

    # Process the recipe data here...
    # Modify the recipe as needed...

    # Return the modified recipe
    return jsonify(recipe=recipe_data)

if __name__ == '__main__':
    app.run(port=5001)

