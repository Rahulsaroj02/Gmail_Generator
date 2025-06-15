# **Gmail Generator using Hugging Face and Streamlit**

This project is a Gmail Generator web application that leverages Hugging Face’s Inference API and Streamlit to generate professionally formatted emails based on user inputs such as sender/recipient names, email subject, tone, and purpose.  
The app is designed to dynamically build a well-structured email that includes a greeting, body, closing, and contact details.

---

## **Features**

- Generates emails with just a few inputs  
- Supports multiple tones: Formal, Informal, Professional, Friendly  
- Automatically structures the email: greeting, body, closing  
- Uses Hugging Face's LLM API (`zephyr-7b-beta`)  
- Download the generated email as a `.txt` file  
- Secure token management via `.env` file  

---

## **Project Structure**



gmail-generator/


├── app.py               # Main Streamlit app file


├── .env                 # Environment file containing the Hugging Face API token (do not commit!)


└──  requirements.txt     # Project dependencies


---

## **Prerequisites**

1. Python 3.7 or higher  
2. A Hugging Face account and your API token  
   - Get your token from: https://huggingface.co/settings/tokens  

---

## **Installation**

### 1. Clone the repository

git clone https://github.com/Rahulsaroj02/Gmail_Generator
cd gmail-generator

### 2. Create and activate a virtual environment (optional but recommended)

python -m venv venv
venv\Scripts\activate

### 3. Create a .env file

Create a file named .env in the root directory and add your Hugging Face API token:
HUGGINGFACE_API_TOKEN=your_huggingface_token_here
