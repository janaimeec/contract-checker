from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Function to check if a contract exists by number
def check_contract(contract_number):
    conn = sqlite3.connect('contracts.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contracts WHERE contract_number = ?", (contract_number,))
    result = cursor.fetchone()
    conn.close()
    return result

# Route to show the form
@app.route('/')
def form():
    return render_template('form.html')

# Route to process form submission
@app.route('/check', methods=['POST'])
def check():
    contract_number = request.form['contract_number']
    result = check_contract(contract_number)
    if result:
        return f"""
        <strong>Contract found!</strong><br>
        <ul>
            <li><b>Contract Name:</b> {result[1]}</li>
            <li><b>Supplier:</b> {result[2]}</li>
            <li><b>Contract Number:</b> {result[3]}</li>
            <li><b>Start Date:</b> {result[4]}</li>
            <li><b>End Date:</b> {result[5]}</li>
        </ul>
        <br><a href="/">Back to search</a>
        """
    else:
        return "No contract found with that number.<br><br><a href='/'>Try again</a>"

if __name__ == '__main__':
    app.run(debug=True)