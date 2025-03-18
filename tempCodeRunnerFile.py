# from flask import Flask, render_template, request, jsonify
# import ollama
# import PyPDF2
# import os

# app = Flask(__name__)

# # Function to extract system prompt from a PDF
# def extract_prompt_from_pdf(pdf_path):
#     try:
#         with open(pdf_path, "rb") as pdf_file:
#             reader = PyPDF2.PdfReader(pdf_file)
#             prompt_text = []
#             for page in reader.pages:
#                 page_text = page.extract_text()
#                 if page_text:
#                     prompt_text.append(page_text.replace("\n", " "))  # Remove line breaks
#             return " ".join(prompt_text).strip()
#     except Exception as e:
#         return f"Error reading system prompt: {str(e)}"

# # Load system prompt from the PDF
# pdf_path = "Brainstromming/Brainstorming Agent - System Prompt.pdf"  # Update path accordingly
# system_prompt = extract_prompt_from_pdf(pdf_path)

# if not system_prompt or "Error" in system_prompt:
#     print("⚠️ Warning: System prompt not loaded correctly.")
# else:
#     print("✅ System prompt loaded successfully.")
    
# print (system_prompt)

# # System message to guide AI behavior
# system_message = {
#     "role": "system",
#     "content": ("You are a knowledgeable AI with expertise in AI and consulting. " + system_prompt)
# }

# # Initialize chat memory (Limited history for better context retention)
# memory = []

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/chat", methods=["POST"])
# def chat():
#     global memory
#     user_input = request.json.get("message", "").strip()
#     if not user_input:
#         return jsonify({"response": "Please enter a message."})

#     memory.append({"role": "user", "content": user_input})
    
#     try:
#         response = ollama.chat(
#             model="llama3.2",
#             messages=[system_message] + memory[-10:]  # Keep system prompt + last 10 interactions
#         )
#         ai_response = response["message"]["content"]
#         memory.append({"role": "assistant", "content": ai_response})
#     except Exception as e:
#         ai_response = f"Error: {str(e)}"
    
#     return jsonify({"response": ai_response})

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)
