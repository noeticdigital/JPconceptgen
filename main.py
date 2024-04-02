import streamlit as st
import openai

# Assuming openai is correctly installed and configured
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY

def write_product_concept(product_name, company_name, use_case, needs, new, cred, differentiation, promise, backup):
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"Write a product concept following this structure: {product_name}, created by {company_name}, is designed to {use_case}. "
               f"It meets the need of {needs} by offering {new}. The product is produced by {cred}. "
               f"It differs from other products by {differentiation}. Its core promise is {promise}. "
               f"To support this promise, {backup}."
               f"keep it within 250 words."
         ,
        temperature=0.7,
        max_tokens=328,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text

st.header("Product or Service Concept Generator:")
st.text("Powered by Noetic Digital")


# URL of the image you want to display
image_url = 'https://living-best.tech/wp-content/webp-express/webp-images/uploads/2023/07/LivingBest_Logo_CarterGroup-V2.jpg.webp'

# Use Streamlit's st.image function to display the image
st.image(image_url, caption='')

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
