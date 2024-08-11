import io
import base64
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, redirect, url_for, send_file
from data_entry import get_amount, get_category, get_date, get_description
from csv_handler import CSV  # Assuming you renamed the CSV class to csv_handler

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        date = request.form.get('date') or get_date("Enter the date of the transaction (dd-mm-yyyy) or enter for today's date: ", allow_default=True)
        amount = float(request.form.get('amount'))
        category = request.form.get('category')
        description = request.form.get('description')
        CSV.add_entry(date, amount, category, description)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/view', methods=['GET', 'POST'])
def view():
    if request.method == 'POST':
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        df = CSV.get_transactions(start_date, end_date)
        
        if 'plot' in request.form:
            plot_url = generate_plot(df)
            return render_template('view.html', plot_url=plot_url, transactions=df.to_html(classes='table table-striped'))
        
        return render_template('view.html', transactions=df.to_html(classes='table table-striped'))
    
    return render_template('view.html')

def generate_plot(df):
    df.set_index('date', inplace=True)

    income_df = (
        df[df["category"] == "Income"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )
    expense_df = (
        df[df["category"] == "Expense"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )

    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df["amount"], label="Income", color="g")
    plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title('Income and Expense Over Time')
    plt.legend()
    plt.grid(True)

    # Save plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    # Encode the image in base64
    img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')
    return f"data:image/png;base64,{img_base64}"

if __name__ == "__main__":
    app.run(debug=True)




