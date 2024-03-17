import streamlit as st
import streamlit_ext as ste
import openai
from streamlit_tags import st_tags

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

openai.api_key = OPENAI_API_KEY


def write_cover_letter(product_name, product_type, use_case, target_user, personal_skills, job_description, target_user, company_name):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"write a cover letter as {product_name}, contact details {company_name} and {target_user}, "
               f"applying for the following job vacancy to make him "
               f"an ideal candidate based on the selection criteria and his skills. {product_name} is a {product_type}, "
               f"with  {use_case} , intermediate {int_tech_skills} skills, and personal "
               f"skills including {personal_skills}:"
               f"\n\n{job_description}",
        temperature=0.7,
        max_tokens=278,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['text']


st.header("Startup Concept GENERATOR:")
st.write("Complete the form below and I will generat eyour concept")

with st.form("Product/Service Concept Generator", clear_on_submit=False):
    product_name = st.text_input("Product/Service Name: ")
    target_user = st.text_input("Who is the product targeted at? ")
    Company name = st.text_input("Company name: ")
    product_t00000ype = st.text_input("Enter the product or service type:")
    product_type = st_tags(
        label="Enter your product_type:",
        text="Press enter product_type detailed",
        value=[],
        suggestions=["Saas", "food", "bevergae", "appliance", "AI"],
        maxtags=8,
        key="1"
    )
    target_user = st_tags(
        label="Enter target user",
        text="Press enter dsecond product_type detailed",
        value=[],
        suggestions=["elderly", "caretakers", "families", "carehomes", "doctors"],
        maxtags=8,
        key="2"
    )
    personal_skills = st_tags(
        label="Enter your personal skills:",
        text="Press enter or tap to add more skills",
        value=[],
        suggestions=["Able to work under pressure", "Great communication skills", "Team leader", "Team player",
                     "Fast learner", "Goal driven", "Great attention to detail", "Career driven"],
        maxtags=8,
        key="3"
    )
    job_description = st.text_area("Paste a few relevant paragraphs from the job you wish to apply for:")

    submitted = st.form_submit_button("Write Concpet")
    if submitted:
        with st.spinner("Writing cover letter..."):
            cover_letter_text = write_cover_letter(product_name=product_name, product_type=product_type,
                                                   use_case=use_case,
                                                   int_tech_skills=intermediate_technical_skills,
                                                   personal_skills=personal_skills, job_description=job_description,
                                                   contact_number=contact_number, email=email)
            st.subheader("Your cover letter:")
            st.write(cover_letter_text)
            ste.download_button("Download", cover_letter_text,
                                f"{applicant_name} - Cover letter.txt")
