import os
import google.generativeai as genai

# ✅ Use Gemini API Key directly (no service account)
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# ✅ This model is supported via API Key mode
model = genai.GenerativeModel("gemini-pro")

response = model.generate_content("Tell me one best practice for Palo Alto Networks firewalls.")
print(response.text)
