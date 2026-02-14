import scanner
import ocr_processor
import expense_analyzer
import sys
import matplotlib.pyplot as plt


def scan_receipt(image_path):
    print(f"Processing {image_path}...")

    processed = scanner.process_image(image_path)

    text = ocr_processor.extract_text(image_path)
    print(f"Extracted text:\n{text[:200]}...\n")

    amounts = ocr_processor.extract_amounts(text)
    date = ocr_processor.extract_date(text)

    expense = expense_analyzer.create_expense_entry(text, amounts, date)
    print(f"Detected: ${expense['amount']} at {expense['vendor']} ({expense['category']})")

    expense_analyzer.save_expense(expense)
    print("✓ Saved to expenses.csv\n")


def show_report():
    insights = expense_analyzer.generate_insights()

    print("=" * 50)
    print("SPENDING REPORT")
    print("=" * 50)
    print(f"Total Spent: ${insights['total_spent']:.2f}")
    print(f"Average Transaction: ${insights['avg_transaction']:.2f}\n")

    print("By Category:")
    for category, amount in insights['by_category'].items():
        print(f"  {category}: ${amount:.2f}")

    categories = list(insights['by_category'].keys())
    amounts = list(insights['by_category'].values())

    plt.bar(categories, amounts)
    plt.title('Spending by Category')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('output/spending_chart.png')
    print("\n✓ Chart saved to output/spending_chart.png")


if __name__ == '__main__':
    print("Smart Document Scanner & Analyzer")
    print("1. Scan receipt")
    print("2. View report")

    choice = input("Choose option: ")

    if choice == '1':
        image_path = input("Enter receipt image path: ")
        scan_receipt(image_path)
    elif choice == '2':
        show_report()

#takes an image and processes it (increases contrast, etc.), then extracts text and data, then analyzes expenses and saves it
#this uses all the files and functions created before

#formats the chart and prints all the data in the report out in a well-structured way