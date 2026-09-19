import os
from google import genai

# Get API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

print("================================")
print("       AI STUDY ASSISTANT")
print("================================")

topic = input("Enter a study topic: ")

prompt = f"""
You are an AI Study Assistant for a second-year engineering student.

For the topic "{topic}", provide:

1. Simple Explanation
2. 5 Key Points
3. Short Summary
4. 3 Practice Questions

Use simple and clear English.
"""

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)

print("\nTopic:", topic)
print("\n" + response.text)

print("\n================================")
print("       END OF SESSION")
print("================================")
