import os
import pandas as pd
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()


def analyze_review(review_text):
    """
    This function sends the review to Gemini and returns the category.
    """

    system_prompt = """
    You are an automated customer service assistant.
    Analyze the provided customer review and categorize it into exactly ONE of the following categories:
    - POSITIVE
    - NEGATIVE
    - NEUTRAL
    - SUPPORT_REQUEST

    Respond ONLY with the category name. Do not add any punctuation or explanation.
    """

    try:
        response = client.models.generate_content(
            model='gemini-3.6-flash',
            contents=review_text,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.0
            )
        )
        return response.text.strip()
    except Exception as e:
        print(f"Error analyzing review: {e}")
        return "ERROR"


def main():
    print("Starting Customer Review Analysis with Gemini...")

    input_file = 'input_reviews.csv'
    output_file = 'categorized_reviews.csv'

    try:
        df = pd.read_csv(input_file)
        print(f"Successfully loaded {len(df)} reviews.")
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
        return

    df['category'] = ""

    for index, row in df.iterrows():
        text = row['review_text']
        print(f"Analyzing review {row['id']}...")

        category = analyze_review(text)

        df.at[index, 'category'] = category

    df.to_csv(output_file, index=False)
    print(f"Analysis complete! Results saved to {output_file}.")


if __name__ == "__main__":
    main()
