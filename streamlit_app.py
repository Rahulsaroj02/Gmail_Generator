import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load Hugging Face API token
load_dotenv()
API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

MODEL = "HuggingFaceH4/zephyr-7b-beta"
API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"
HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}

# UI
st.set_page_config(page_title="Gmail Generator (Hugging Face)", page_icon="📧")
st.title("📧 Gmail Generator using Hugging Face API")

sender = st.text_input("Your Name (Sender)", "Rahul Saroj")
recipient = st.text_input("Recipient Name", "Rahul")
subject = st.text_input("Email Subject", "internship at swecha")
tone = st.selectbox("Tone", ["Formal", "Informal", "Professional", "Friendly"])
email = st.text_input("Email","rahul@gmail.com")
phone = st.text_input("Phoe No","+91-95XXXXXXXX")
purpose = st.text_area("Purpose of the Email", "to tell my friend that i got internship..")


def query_huggingface(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 300, "temperature": 0.7},
    }
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    if response.status_code == 200:
        return response.json()[0]['generated_text']
    else:
        return f"⚠️ Error: {response.status_code}\n{response.text}"

if st.button("Generate Email"):
    with st.spinner("Generating email using Hugging Face model..."):
        prompt = f"""
You are an expert email writer.

Write a {tone.lower()} email from {sender} to {recipient}.

Subject: "{subject}"

Purpose:
{purpose.strip()}

Structure the email as follows:
1. Greeting using recipient name.
2. Introduction of the sender.
3. Describe the purpose: {purpose.strip()}
4. Express any appreciation or gratitude if relevant.
5. Include a closing paragraph and encourage further communication.
6. End the email with:
   - Best regards,
   - {sender}
   - Email: {email}
   - Phone: {phone}

Use a {tone.lower()} tone. Keep the grammar correct, language appropriate, and avoid repetition.
Return only the email body without extra explanation or instructions.
"""


        result = query_huggingface(prompt)
        # Try to extract only the email body by removing echoed prompt parts
# Common marker the model uses
        split_marker = "Here is your email:"
        if split_marker in result:
            email_body = result.split(split_marker, 1)[1].strip()
        else:
            # Fallback: try to remove first lines that repeat the prompt
            lines = result.strip().splitlines()
            # Heuristic: keep lines after the first empty line or a line starting with "Dear"
            email_body = ""
            for line in lines:
                if line.strip().startswith("Dear"):
                    email_body = "\n".join(lines[lines.index(line):]).strip()
                    break
            if not email_body:
                email_body = result.strip()  # fallback if nothing found

        st.subheader("📨 Generated Email")
        st.markdown(email_body.replace("\n", "   \n"))
        st.download_button("📥 Download Email", email_body, file_name="email.txt")
