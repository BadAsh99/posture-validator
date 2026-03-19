from vertexai.preview.language_models import ChatModel
import vertexai

# Replace with your actual project ID and location
vertexai.init(project="gen-lang-client-0921676642", location="us-central1")

# Correct Gemini model and method
chat_model = ChatModel.from_pretrained("chat-bison@001")  # Temporary fallback

chat = chat_model.start_chat()
response = chat.send_message("What is a best practice for PAN-OS?")
print(response.text)
