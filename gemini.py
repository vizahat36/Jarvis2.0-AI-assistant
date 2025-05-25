# import requests

# API_KEY = "AIzaSyC4wUS-KnR4GaGLtg-4iETZPEH8GSRZfF0"  # Use your own key
# API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

# HEADERS = {
#     "Content-Type": "application/json"
# }

# def ask_question(question):
#     prompt = f"Answer briefly in 2 lines: {question}"

#     payload = {
#         "contents": [
#             {
#                 "parts": [
#                     {"text": prompt}
#                 ]
#             }
#         ],
#         "generationConfig": {
#             "maxOutputTokens": 60,
#             "temperature": 0.7,
#             "topP": 1
#         }
#     }

#     response = requests.post(API_URL, headers=HEADERS, json=payload)
#     response.raise_for_status()
#     data = response.json()

#     try:
#         return data["candidates"][0]["content"]["parts"][0]["text"]
#     except (KeyError, IndexError):
#         return "No response or unexpected format from Gemini API."

# def main():
#     question = input("Ask your question: ")
#     answer = ask_question(question)
#     print("\nAnswer:\n" + answer)

# if __name__ == "__main__":
#     main()
# gemini.py

import google.generativeai as genai

# Use your actual API key here
API_KEY = "AIzaSyC4wUS-KnR4GaGLtg-4iETZPEH8GSRZfF0"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-pro')

def chat_with_gemini(query):
    try:
        response = model.generate_content(query)
        return response.text  # Return the actual Gemini response
    except Exception as e:
        return f"Error from Gemini: {e}"
