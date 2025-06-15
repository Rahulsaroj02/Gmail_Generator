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
├── app.py # Main Streamlit app file
├── .env # Environment file containing the Hugging Face API token (do not commit!)
├── requirements.txt # Project dependencies
└── .gitignore # Files and directories to ignore in Git (e.g., .env, pycache)
