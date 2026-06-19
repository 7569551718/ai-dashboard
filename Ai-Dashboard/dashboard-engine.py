import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content(
    "What is Data Science?"
)

print(response.text)

model = genai.GenerativeModel("gemini-2.5-flash")

def get_dashboard_suggestion(columns, prompt):

    response = model.generate_content(
        f"""
        Dataset Columns:
        {columns}

        User Request:
        {prompt}

        Suggest suitable dashboard charts.
        """
    )

    return response.text
