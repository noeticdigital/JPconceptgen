import streamlit as st
import streamlit_ext as ste
import openai
from streamlit_tags import st_tags

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY



def write_concept(product_name, company_name, use_case, product_type, needs, target_user, new, cred, differentiation, promise, backup):
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",  # Adjusted to use a non-chat model
            prompt=
                f"write a product concept called {product_name}, created by {company_name} for {target_user}, "
                f"the product solves {needs} because we have {cred}. "
                f"The new point is {new} and the differentiation is {differentiation}. "
                f"{product_name} promises to {promise} because {backup}. "
                f"Here's an example concept -- Comfort Linen: Revolutionizing Rest for Those with Mobility Challenges. "
                "Are you tired of getting tangled in your bedsheets, especially if you face pain or mobility issues? For millions worldwide, this is more than just an annoyance; it's a significant problem. Comfort Linen is the solution. It's a game-changing approach to your nightly routine. "
                "After extensive research, we created an award-winning system of friction-reducing sheets initially for caregivers. However, inspired by patients seeking the same comfort at home, we expanded our innovation to offer a complete range of mobility-enhancing products for consumers. "
                "At Comfort Linen, we applied the principles of tribology, the science of friction, to develop a patented design that minimizes surface contact area, allowing sleepwear to glide with minimal resistance. Our sheets aren't just functional; they're also smooth, elegant, and luxurious, delivering unparalleled comfort. "
                "But Comfort Linen goes beyond providing a good night's sleep. We've developed a range of mobility-enhancing products, including positioning pads, to assist caregivers. These products reduce strain and effort, promoting independence and easing the physical demands on caregivers. "
                "Our technology has proven effective, with satisfied users praising improved movement and newfound independence. The Comfort Linen community has experienced firsthand the positive impact on both individuals with mobility issues and their dedicated caregivers. "
                "Let's support the aging population, empower caregivers, and contribute to Japan's legacy of fostering health and wellness. Comfort Linen – where innovation meets tranquility, transforming the way we rest, one night at a time."
            
            ,
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

 <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

