import streamlit as st
import streamlit_ext as ste
import openai
from streamlit_tags import st_tags

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

openai.api_key = OPENAI_API_KEY


def write_cover_letter(full_name, job_title, adv_tech_skills, int_tech_skills, personal_skills, job_description, contact_number, email):
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=(
                f"write a product concept called {product_name}, created by {company_name}, "
                f"the product solves {needs} because we have {cred}. "
                f"The new point is {new} and the differentiation is {differentiation}. "
                f"{product_name} promises to {promise} because {backup}. "
                f"Here's an example concept of appropriate length -- Comfort Linen: Revolutionizing Rest for Those with Mobility Challenges. "
                "After extensive research, we created an award-winning system of friction-reducing sheets initially for caregivers. However, inspired by patients seeking the same comfort at home, we expanded our innovation to offer a complete range of mobility-enhancing products for consumers. "
                "At Comfort Linen, we applied the principles of tribology, the science of friction, to develop a patented design that minimizes surface contact area, allowing sleepwear to glide with minimal resistance. Our sheets aren't just functional; they're also smooth, elegant, and luxurious, delivering unparalleled comfort. "
                "Let's support the aging population, empower caregivers, and contribute to Japan's legacy of fostering health and wellness. Comfort Linen – where innovation meets tranquility, transforming the way we rest, one night at a time.",
        temperature=0.7,
        max_tokens=278,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['text']

st.header("COVER LETTER GENERATOR:")
st.write("Complete the form below and we'll do our best to bang together a bitchin cover letter for your dream job:")

with st.form("Cover Letter Generator", clear_on_submit=False):
    applicant_name = st.text_input("Full Name: ")
    contact_number = st.text_input("Contact number: ")
    email = st.text_input("Email: ")
    job_title = st.text_input("Enter your job title:")
    advanced_technical_skills = st_tags(
        label="Enter your advanced technical skills:",
        text="Press enter or tap to add more skills",
        value=[],
        suggestions=["Python", "Javascript", "Java", "C#", "C++", "Golang", "HTML", "CSS", "Microsoft Office Suite",
                     "Adobe Suite", "XPLAN", "MYOB"],
        maxtags=8,
        key="1"
    )
    intermediate_technical_skills = st_tags(
        label="Enter your intermediate technical skills:",
        text="Press enter or tap to add more skills",
        value=[],
        suggestions=["Python", "Javascript", "Java", "C#", "C++", "Golang", "HTML", "CSS", "Microsoft Office Suite",
                     "Adobe Suite", "XPLAN", "MYOB"],
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

    submitted = st.form_submit_button("Write my damn cover letter!")
    if submitted:
        with st.spinner("Writing cover letter..."):
            cover_letter_text = write_cover_letter(full_name=applicant_name, job_title=job_title,
                                                   adv_tech_skills=advanced_technical_skills,
                                                   int_tech_skills=intermediate_technical_skills,
                                                   personal_skills=personal_skills, job_description=job_description,
                                                   contact_number=contact_number, email=email)
            st.subheader("Your cover letter:")
            st.write(cover_letter_text)
            ste.download_button("Download", cover_letter_text,
                                f"{applicant_name} - Cover letter.txt")
