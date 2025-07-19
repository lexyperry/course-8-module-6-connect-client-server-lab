from flask import Flask, jsonify, request

app = Flask(__name__)

# Create a list called 'events' with a couple of sample event dictionaries
# Each dictionary should have an 'id' and a 'title'
events = [
    {"id": 1, "title": "Adoption-a-thon"},
    {"id": 2, "title": "Basket weaving contest"}    
]
# TASK: Create a route for "/"
# This route should return a JSON welcome message
@app.route("/")
def home():
    return jsonify({"message": "Welcome"})

# TASK: Create a GET route for "/events"
# This route should return the full list of events as JSON
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(events)
# TASK: Create a POST route for "/events"
# This route should:
# 1. Get the JSON data from the request
# 2. Validate that "title" is provided
# 3. Create a new event with a unique ID and the provided title
# 4. Add the new event to the events list
# 5. Return the new event with status code 201
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({"error": "Missing title"}), 400
    new_event = {
        "id": events[-1]["id"] + 1 if events else 1,
        "title": data["title"]
    }
    events.append(new_event)
    return jsonify(new_event), 201

if __name__ == "__main__":
    app.run(debug=True)
