import os
import pandas as pd
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

# Flask app initialization
app = Flask(__name__)
CORS(app)  # Enable CORS for API usage

# Configuration
app.config["UPLOAD_FOLDER"] = os.path.abspath("./uploads")
app.config["DATASET_FOLDER"] = os.path.abspath("./datasets")

# Ensure necessary folders exist
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
os.makedirs(app.config["DATASET_FOLDER"], exist_ok=True)

# Dataset path
dataset_path = os.path.join(app.config["DATASET_FOLDER"], "crowdsourced_artifacts.csv")

# Load or initialize the dataset
if os.path.exists(dataset_path):
    try:
        df = pd.read_csv(dataset_path)
        if df.empty:
            raise ValueError("Dataset is empty. Initializing a new dataset.")
    except Exception as e:
        print(f"Error loading dataset: {e}")
        # Create a new dataset if loading fails
        columns = [
            "Artifact Name", "Date", "Culture/Region", "Material",
            "Dimensions", "Category/Type", "Description", "Artifact Image Path"
        ]
        df = pd.DataFrame(columns=columns)
else:
    # Create a new dataset if it doesn't exist
    columns = [
        "Artifact Name", "Date", "Culture/Region", "Material",
        "Dimensions", "Category/Type", "Description", "Artifact Image Path"
    ]
    df = pd.DataFrame(columns=columns)

# Save updated dataset function
def save_dataset():
    try:
        if not os.access(dataset_path, os.W_OK):
            raise PermissionError(f"Write access denied for {dataset_path}")
        df.to_csv(dataset_path, index=False)
    except PermissionError as e:
        print(f"Permission error: {e}")
        raise
    except Exception as e:
        print(f"Error saving dataset: {e}")
        raise

# Route for the index page
@app.route("/")
def index():
    return render_template("index1.html")  # Render the HTML form for data submission

# Route for crowdsourcing artifact data
@app.route("/crowdsource", methods=["POST"])
def crowdsource():
    try:
        # Retrieve metadata from the form
        artifact_name = request.form.get("artifact_name")
        date = request.form.get("date")
        culture_region = request.form.get("culture_region")
        material = request.form.get("material")
        dimensions = request.form.get("dimensions")
        category_type = request.form.get("category_type")
        description = request.form.get("description")

        # Validate required fields
        if not all([artifact_name, date, culture_region, material, dimensions, category_type, description]):
            return jsonify({"status": "Error", "message": "All fields are required."}), 400

        # Handle file upload
        if "artifact_image" not in request.files:
            return jsonify({"status": "Error", "message": "No image file uploaded."}), 400

        file = request.files["artifact_image"]
        if file.filename == "":
            return jsonify({"status": "Error", "message": "No file selected."}), 400

        # Save the uploaded file
        image_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(image_path)

        # Add new data to the dataset
        global df
        new_row = {
            "Artifact Name": artifact_name,
            "Date": date,
            "Culture/Region": culture_region,
            "Material": material,
            "Dimensions": dimensions,
            "Category/Type": category_type,
            "Description": description,
            "Artifact Image Path": image_path
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        save_dataset()  # Save the updated dataset

        # Success response
        return jsonify({"status": "Success", "message": "Artifact data added successfully."}), 201
    except PermissionError as e:
        return jsonify({"status": "Error", "message": f"Permission error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"status": "Error", "message": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
