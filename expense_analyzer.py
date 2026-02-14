import pandas as pd
from datetime import datetime

def categorize_expense(text):
    text_lower = text.lower()

    categories = {
        'Food & Dining': ['restaurant', 'cafe', 'coffee', 'pizza', 'burger', 'food'],
        'Transportation': ['uber', 'lyft', 'taxi', 'gas', 'fuel', 'parking'],
        'Shopping': ['amazon', 'target', 'walmart', 'store', 'shop'],
        'Utilities': ['electric', 'water', 'internet', 'phone'],
        'Healthcare': ['pharmacy', 'doctor', 'medical', 'health']
    }

    for category, keywords in categories.items():
        if any(keyword in text_lower for keyword in keywords):
            return category
    return 'Other'

def create_expense_entry(text, amounts, date):
    return {
        'date': date,
        'category': categorize_expense(text),
        'amount': max(amounts) if amounts else 0.0,
        'vendor': extract_vendor(text),
        'raw_text': text[:100]
    }

def extract_vendor(text):
    lines = text.split('\n')
    for line in lines:
        if line.strip():
            return line.strip()[:50]
    return 'Unknown'


def save_expense(expense_data, csv_file='expenses.csv'):
    df = pd.DataFrame([expense_data])

    try:
        existing = pd.read_csv(csv_file)
        updated = pd.concat([existing, df], ignore_index=True)
        updated.to_csv(csv_file, index=False)
    except FileNotFoundError:
        df.to_csv(csv_file, index=False)


def generate_insights(csv_file='expenses.csv'):
    df = pd.read_csv(csv_file)

    insights = {
        'total_spent': df['amount'].sum(),
        'by_category': df.groupby('category')['amount'].sum().to_dict(),
        'avg_transaction': df['amount'].mean(),
        'largest_expense': df.loc[df['amount'].idxmax()].to_dict()
    }

    return insights

#categorizes entries by seeing possible keywords, then creates the entry in the form of a dictionary, then finds the vendor name (first line in receipt)
#then it saves expenses in a table in a file (if a file doesn't exist it makes one), then gives insights and data on what you've submitted