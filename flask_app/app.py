from flask import Flask, request, render_template_string
import psycopg2
import re
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        dbname="sales_db",
        user="airflow",
        password="airflow",
        host="postgres",
        port="5432"
    )

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        customer = request.form['customer']
        amount = request.form['amount']
        date = request.form['date']

        # Validate customer name
        if not re.fullmatch(r'[A-Za-z ]+', customer):
            message = "❌ Name must contain only letters."
        # Validate amount
        elif not re.fullmatch(r'\d+(\.\d{1,2})?', amount):
            message = "❌ Amount must be a number or decimal (e.g., 99.99)."
        # Validate date format
        elif not re.fullmatch(r'\d{2}/\d{2}/\d{4}', date):
            message = "❌ Date must be in dd/mm/yyyy format."
        else:
            # Convert date to YYYY-MM-DD for Postgres
            try:
                formatted_date = datetime.strptime(date, "%d/%m/%Y").date()

                conn = get_db_connection()
                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO sales (customer, amount, date) VALUES (%s, %s, %s)",
                    (customer, float(amount), formatted_date)
                )
                conn.commit()
                cur.close()
                conn.close()

                message = "✅ Sale recorded successfully!"
            except Exception as e:
                message = f"❌ Database error: {str(e)}"

    return render_template_string('''
        <h2>Enter Sales Record</h2>
        <form method="POST">
            Customer (letters only): <input type="text" name="customer" required><br><br>
            Amount (e.g. 100.50): <input type="text" name="amount" required><br><br>
            Date (dd/mm/yyyy): <input type="text" name="date" required><br><br>
            <input type="submit" value="Submit Sale">
        </form>
        <p>{{message}}</p>
    ''', message=message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
