import streamlit as st
import openai

# openaiが正しくインストールされ、設定されていることを前提とします
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY

def write_product_concept(product_name, company_name, use_case, needs, new, cred, differentiation, promise, backup):
    # 日本語の製品コンセプトを生成
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"250語以内で製品コンセプトを記述してください。以下の構造に従います: {product_name}は{company_name}によって作られ、{use_case}することを目的としています。"
               f"{needs}のニーズに応え、{new}を提供します。この製品は{cred}によって生産されます。"
               f"他の製品との違いは{differentiation}です。その核となる約束は{promise}です。"
               f"この約束を支えるために、{backup}。",
        temperature=0.7,
        max_tokens=358,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    日本語のコンセプト = response.choices[0].text

    # コンセプトを英語に翻訳
    英語のコンセプト = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=f"英語に翻訳してください: {日本語のコンセプト}",
        temperature=0.7,
        max_tokens=600,
        top_p=1.0,
        frequency_penalty=0,
        presence_penalty=0
    ).choices[0].text

    return 日本語のコンセプト, 英語のコンセプト

st.header("製品またはサービスコンセプトジェネレーター:")
st.text("Noetic Digital提供")

# 表示したい画像のURL
image_url = 'https://living-best.tech/wp-content/webp-express/webp-images/uploads/2023/07/LivingBest_Logo_CarterGroup-V2.jpg.webp'

# Streamlitのst.image関数を使って画像を表示
st.image(image_url, caption='')

with st.form("product_concept_form", clear_on_submit=True):
    product_name = st.text_input("製品またはサービス名:")
    company_name = st.text_input("会社名:")
    use_case = st.text_area("製品またはサービスの使用例を入力してください:")
    needs = st.text_area("それはどのような特定のニーズを満たしますか？")
    new = st.text_area("この製品の新しい点は何ですか？")
    cred = st.text_area("それを生産した人は誰で、その背景、歴史、そしてそのような製品を作る「権利」について教えてください。")
    differentiation = st.text_area("同じニーズを満たそうとする他の製品と比較して、何が異なりますか？")
    promise = st.text_area("消費者への核となる約束は何ですか；つまり、この製品は私に何をしてくれるのか、そして私はどのように感じるのか？")
    backup = st.text_area("この約束を信じるために、どのような情報を提供できますか？")
    if st.form_submit_button("製品コンセプトを生成"):
        concept_text_japanese, concept_text = write_product_concept(product_name, company_name, use_case, needs, new, cred, differentiation, promise, backup)
        st.subheader("生成された製品コンセプト（日本語）:")
        st.write(concept_text)
        st.subheader("生成された製品コンセプト（英語）:")
        st.write(concept_text_japanese)
