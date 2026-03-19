import google.generativeai as genai

# Use ADC from `gcloud auth application-default login`
genai.configure()

# Use full Vertex model path (required for ADC auth)
model = genai.GenerativeModel(
    "projects/1036711794272/locations/us-central1/models/gemini-1.5-pro"
)

response = model.generate_content("What is a recommended PAN-OS firewall best practice?")
print(response.text)
