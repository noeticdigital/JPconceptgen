import streamlit as st
import streamlit_ext as ste
import openai
from streamlit_tags import st_tags

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY

def write_concept(product_name, company_name, use_case, product_type, needs, target_user, new, cred, differentiation, promise, backup):
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=f"write a product concept called {product_name}, created by {company_name} for {target_user}, "
                   f"the product solves {needs} because we have {cred}. "
                   f"The new point is {new} and the differentiation is {differentiation}. "
                   f"{product_name} promises to {promise} because {backup}.",
            temperature=0.7,
            max_tokens=278,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response['choices'][0]['text']
    except Exception as e:
        return f"An error occurred: {e}"

st.header("Noetic Digital - Startup Concept Generator:")
st.write("Complete the form below and Noetic will generate your concept")

with st.form("Product/Service Concept Generator", clear_on_submit=False):
    product_name = st.text_input("Product/Service Name: ")
    company_name = st.text_input("Company name: ")
    use_case = st.text_area("Enter the product or service use case:")
    product_type = st_tags(
        label="Enter your product type:",
        text="Press enter after each product type",
        value=[],
        suggestions=["Saas", "food", "beverage", "appliance", "AI"],
        maxtags=8,
        key="1"
    )
    target_user = st_tags(
        label="Enter target user",
        text="Press enter after each user type",
        value=[],
        suggestions=["elderly", "caretakers", "families", "care homes", "doctors"],
        maxtags=8,
        key="2"
    )
    needs = st.text_area("What specific needs does it meet?")
    new = st.text_area("What is new about this product?")
    cred = st.text_area("Who produced it, including their background, history, and ‘right’ to make such a product?")
    differentiation = st.text_area("What is different compared to other products that try to meet the same needs?")
    promise = st.text_area("What is the core promise to the consumer i.e., what will this product do for me, and how will I feel?")
    backup = st.text_area("What information can you give me to help me believe that?")

    submitted = st.form_submit_button("Write Concept")
    if submitted:
        with st.spinner("Writing concept..."):
            concept_text = write_concept(product_name, company_name, use_case, product_type, needs, target_user, new, cred, differentiation, promise, backup)
            st.subheader("Your concept:")
            st.write(concept_text)
            ste.download_button("Download", concept_text, f"{product_name} - Concept.txt")
