# Smart Document Scanner & Analyzer

An AI-powered Python application that scans receipts, extracts expenses, and generates spending insights using computer vision and OCR technology.

## Features

- 📸 **Image Processing** - Automatically cleans and enhances receipt photos
- 🔍 **OCR Text Extraction** - Reads text from images using Tesseract
- 🏷️ **Smart Categorization** - Automatically categorizes expenses (Food, Transport, Shopping, etc.)
- 📊 **Analytics** - Generates spending reports and visualizations
- 💾 **Data Export** - Saves all expenses to CSV for further analysis

## Demo

[Add a screenshot here later - see instructions below]

## Technologies

- **Python 3.x**
- **OpenCV** - Image preprocessing and computer vision
- **Tesseract OCR** - Optical character recognition
- **Pandas** - Data analysis and manipulation
- **Matplotlib** - Chart generation

## Installation

### Prerequisites

Make sure you have Python 3.8+ installed.

### Step 1: Clone the repository
```bash
git clone https://github.com/Nav400/document-scanner.git
cd document-scanner
```

### Step 2: Install Python dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Install Tesseract OCR

**Windows:**
1. Download the installer: https://github.com/UB-Mannheim/tesseract/wiki
2. Run the `.exe` file and install
3. Update the path in `ocr_processor.py` if installed in a different location

**Mac:**
```bash
brew install tesseract
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```

## Usage

Run the application:
```bash
python main.py
```

### Scanning a Receipt

1. Choose option `1` from the menu
2. Enter the path to your receipt image (e.g., `sample_images/receipt.jpg`)
3. The program will:
   - Extract all text from the image
   - Identify amounts and dates
   - Categorize the expense
   - Save it to `expenses.csv`

### Viewing Reports

1. Choose option `2` from the menu
2. See your spending statistics:
   - Total amount spent
   - Breakdown by category
   - Average transaction amount
3. A bar chart is automatically saved to `output/spending_chart.png`

## Project Structure
```
document-scanner/
├── main.py                 # Main program and user interface
├── scanner.py              # Image preprocessing functions
├── ocr_processor.py        # Text extraction and parsing
├── expense_analyzer.py     # Categorization and analytics
├── requirements.txt        # Python dependencies
├── README.md              # Documentation (this file)
├── sample_images/         # Test receipt images (not tracked)
└── output/                # Generated charts and reports (not tracked)
```

## How It Works

1. **Image Preprocessing** - Converts receipts to grayscale, removes noise, enhances contrast
2. **OCR Extraction** - Uses Tesseract to read text from the processed image
3. **Data Parsing** - Extracts amounts, dates, and vendor names using regex patterns
4. **Categorization** - Analyzes keywords to auto-categorize expenses
5. **Storage** - Saves structured data to CSV
6. **Analytics** - Generates insights and visualizations

## Future Enhancements

- [ ] Web interface using Streamlit or Flask
- [ ] Batch processing for multiple receipts
- [ ] Machine learning model for improved categorization
- [ ] Mobile app integration
- [ ] PDF export for monthly reports
- [ ] Cloud storage integration

## Contributing

This is a portfolio project, but suggestions and feedback are welcome!

## Contact

Navjot Singh
Email: navjot1singh1@outlook.com

---

*Built as a portfolio project to demonstrate Python, computer vision, and data analysis skills.*