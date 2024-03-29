import streamlit as st
import streamlit_ext as ste
import openai
from streamlit_tags import st_tags
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY
def write_concept(product_name, company_name, use_case, needs, new, cred, differentiation, promise, backup):
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",  # Use "engine" instead of "model" for GPT-3.5-turbo
            prompt=(
                f"write a product concept called {product_name}, created by {company_name}, "
                f"the product solves {needs} because we have {cred}. "
                f"The new point is {new} and the differentiation is {differentiation}. "
                f"{product_name} promises to {promise} because {backup}. "
                f"Here's an example concept -- Comfort Linen: Revolutionizing Rest for Those with Mobility Challenges. "
                "Are you tired of getting tangled in your bedsheets, especially if you face pain or mobility issues? For millions worldwide, this is more than just an annoyance; it's a significant problem. Comfort Linen is the solution. It's a game-changing approach to your nightly routine. "
                "After extensive research, we created an award-winning system of friction-reducing sheets initially for caregivers. However, inspired by patients seeking the same comfort at home, we expanded our innovation to offer a complete range of mobility-enhancing products for consumers. "
                "At Comfort Linen, we applied the principles of tribology, the science of friction, to develop a patented design that minimizes surface contact area, allowing sleepwear to glide with minimal resistance. Our sheets aren't just functional; they're also smooth, elegant, and luxurious, delivering unparalleled comfort. "
                "Let's support the aging population, empower caregivers, and contribute to Japan's legacy of fostering health and wellness. Comfort Linen – where innovation meets tranquility, transforming the way we rest, one night at a time."
            ),
            temperature=0.7,
            max_tokens=778,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response['choices'][0]['text']
    except Exception as e:
        return f"An error occurred: {e}"
st.header("Noetic Digital - Product or Service Concept Generator:")
st.write("Complete the form below and Noetic will generate your concept description")
with st.form("Product or Service Concept Generator", clear_on_submit=False):
    product_name = st.text_input("Product or Service Name: ")
    company_name = st.text_input("Company Name: ")
    use_case = st.text_area("Enter the product or service use case:")
    needs = st.text_area("What specific need/s does it meet?")
    new = st.text_area("What is new about this product?")
    cred = st.text_area("Who produced it, including their background, history; and ‘right’ to make such a product?")
    differentiation = st.text_area("What is different, when compared with other products that try to meet the same needs?")
    promise = st.text_area("What is the core promise to the consumer; i.e. what will this product do for me and how will I feel?")
    backup = st.text_area("What information can you offer to help me believe this promise?")
    submitted = st.form_submit_button("Write Concept")
    if submitted:
        with st.spinner("Writing concept..."):
            concept_text = write_concept(product_name, company_name, use_case, needs, new, cred, differentiation, promise, backup)
            st.subheader("Your concept:")
            st.write(concept_text)
            ste.download_button("Download", concept_text, f"{product_name} - Concept.txt")
