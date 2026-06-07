import streamlit as st
from email_generator import generate_email
from templates import templates

st.set_page_config(
    page_title="AI Email Generator",
    page_icon="📧",
    layout="centered"
)

st.title("📧 AI Email Generator")

template = st.selectbox(
    "Choose Template",
    list(templates.keys())
)

tone = st.selectbox(
    "Choose Tone",
    ["Formal", "Friendly", "Professional"]
)

details = st.text_area(
    "Enter Details",
    height=150,
    placeholder="Describe what the email should contain..."
)

if st.button("Generate Email"):
    if not details.strip():
        st.warning("Please enter some details.")
    else:
        prompt = f"""
{templates[template]}

Tone: {tone}

Details:
{details}

Generate a complete email with:
1. Subject line
2. Greeting
3. Email body
4. Closing
"""

        try:
            with st.spinner("Generating email using Gemma 4 E4B..."):
                email = generate_email(prompt)

            st.success("Email Generated Successfully!")

            st.subheader("Generated Email")
            st.text_area(
                "Output",
                value=email,
                height=350
            )

        except Exception as e:
            st.error(f"Error: {str(e)}")
