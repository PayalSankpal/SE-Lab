from flask import Flask, request, jsonify, render_template
import pandas as pd
import os

app = Flask(__name__)

# Route to serve the registration form (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Define the route for form submission
@app.route('/register', methods=['POST'])
def register():
    data = request.json

    # Registration details from form
    MIS = data.get('MIS')
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')
    phone = data.get('phone')

    # Create or append data to the Excel file
    file_path = 'registration_data.xlsx'
    new_data = {'MIS': [MIS], 'First Name': [first_name], 'Last Name': [last_name], 'Email': [email], 'Phone': [phone]}

    df = pd.DataFrame(new_data)

    if not os.path.exists(file_path):
        df.to_excel(file_path, index=False)
    else:
        existing_data = pd.read_excel(file_path)
        updated_data = pd.concat([existing_data, df], ignore_index=True)
        updated_data.to_excel(file_path, index=False)

    return jsonify({'message': 'Registration successful!'})

if __name__ == '__main__':
    app.run(debug=True)
