# AI Customer Review Analyzer

A simple, automated Python tool that uses the Google Gemini API to read and sort customer reviews.

This project shows how to connect modern AI to everyday business tasks (like reading data from a CSV file) to automatically sort customer support messages and find useful information.

## Features
* **Automatic Sorting:** Uses AI prompts to put reviews into clear categories (`POSITIVE`, `NEGATIVE`, `NEUTRAL`, `SUPPORT_REQUEST`).
* **Process Many Reviews at Once:** Reads data from `.csv` files using `pandas`, making it easy to analyze a lot of feedback quickly.
* **Modern AI Connection:** Built with the new `google-genai` package, using the fast `gemini-3.6-flash` model.
* **Safe Configuration:** Uses `python-dotenv` to keep your secret API keys safe and hidden from the internet.

## What You Need
* Python 3.8 or newer
* A free Google AI Studio (Gemini) API Key

## Installation & Setup

1. **Download the project:**
   ```bash
   git clone https://github.com/almosgecse/customer-review-analyzer.git
   cd customer-review-analyzer
   ```

2. **Install the required packages:**
   (It is recommended to use a virtual environment.)
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the API Key:**
   Create a file named `.env` in the main folder and add your Gemini API key like this:
   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   ```

## How to Use

1. Add your customer reviews to the `input_reviews.csv` file. Make sure the file has `id` and `review_text` columns.
2. Run the program:
   ```bash
   python main.py
   ```
3. The script will read the data and create a new file named `categorized_reviews.csv`. This file will have the original reviews and the new categories added by the AI.

## Future Ideas
* Handle API limits when working with very large files.
* Connect the script directly to customer service apps (like Zendesk) instead of using CSV files.
* Save the results in JSON format.
