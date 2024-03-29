import streamlit as st
import openai

# Assuming openai is correctly installed and configured
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY

def write_product_concept(product_name, company_name, use_case, needs, new, cred, differentiation, promise, backup):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Write a product concept for {product_name}, created by {company_name}. It is designed to {use_case}. "
               f"It meets the need of {needs} by offering {new}. The product is produced by {cred}. "
               f"It differs from other products by {differentiation}. The core promise to the consumer is {promise}. "
               f"To support this promise, we provide {backup}.",
        temperature=0.7,
        max_tokens=278,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text

def write_cover_letter(full_name, job_title, personal_skills, job_description, contact_number, email):
    prompt = f"Write a cover letter for {full_name}, applying for the position of {job_title}. Highlight their skills: {personal_skills}. "
    prompt += f"Describe how they fit the job description: {job_description}. Include their contact number: {contact_number} and email: {email}."
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=400,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text

st.header("Product or Service Concept Generator:")
with st.form("product_concept_form", clear_on_submit=True):
    product_name = st.text_input("Product or Service Name:")
    company_name = st.text_input("Company Name:")
    use_case = st.text_area("Enter the product or service use case:")
    needs = st.text_area("What specific need/s does it meet?")
    new = st.text_area("What is new about this product?")
    cred = st.text_area("Who produced it, including their background, history; and ‘right’ to make such a product?")
    differentiation = st.text_area("What is different, when compared with other products that try to meet the same needs?")
    promise = st.text_area("What is the core promise to the consumer; i.e., what will this product do for me and how will I feel?")
    backup = st.text_area("What information can you offer to help me believe this promise?")
    if st.form_submit_button("Generate Product Concept"):
        concept_text = write_product_concept(product_name, company_name, use_case, needs, new, cred, differentiation, promise, backup)
        st.subheader("Generated Product Concept:")
        st.write(concept_text)

st.header("Cover Letter Generator:")
with st.form("cover_letter_form", clear_on_submit=True):
    full_name = st.text_input("Your Full Name:")
    job_title = st.text_input("Job Title You're Applying For:")
    personal_skills = st.text_area("List Your Personal Skills:")
    job_description = st.text_area("Job Description:")
    contact_number = st.text_input("Contact Number:")
    email = st.text_input("Email:")
    if st.form_submit_button("Generate Cover Letter"):
        cover_letter_text = write_cover_letter(full_name, job_title, personal_skills, job_description, contact_number, email)
        st.subheader("Your Cover Letter:")
        st.write(cover_letter_text)
