import streamlit as st
import openai

# Assuming openai is correctly installed and configured
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY

def write_product_concept(product_name, company_name, use_case, needs, new, cred, differentiation, promise, backup):
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"Write a product concept for {product_name}, created by {company_name}. It is designed to {use_case}. "
               f"It meets the need of {needs} by offering {new}. The product is produced by {cred}. "
               f"It differs from other products by {differentiation}. The core promise to the consumer is {promise}. "
               f"To support this promise, we provide {backup}."
        f"Here's an example concept: Introducing product name – Revolutionizing Rest for Those with Mobility Challenges"
f"Are you tired of getting tangled in your bedsheets, especially if you face pain or mobility issues? For millions worldwide, this is more than just an annoyance; it's a significant problem. Comfort Linen is the solution. It's a game-changing approach to your nightly routine."
f"At Comfort Linen, we applied the principles of tribology, the science of friction, to develop a patented design that minimizes surface contact area, allowing sleepwear to glide with minimal resistance. Our sheets aren't just functional; they're also smooth, elegant, and luxurious, delivering unparalleled comfort."
       
        temperature=0.7,
        max_tokens=378,
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
