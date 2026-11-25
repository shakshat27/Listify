import os
import google.generativeai as genai

API_KEY = os.getenv("GOOGLE_API_KEY")  # export GOOGLE_API_KEY=...
genai.configure(api_key=API_KEY)

#myfile = genai.upload_file("C:/Users/Aksha/Desktop/eathren.jpg")
#print(f"{myfile=}")
#myfile1 = "https://i.ibb.co/zFZwXsS/eathren.jpg"

model = genai.GenerativeModel("gemini-1.5-flash")
result = model.generate_content(
    [myfile1, "\n\n", "whats the photo about?"]
)
print(result.text)