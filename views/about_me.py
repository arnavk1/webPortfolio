import streamlit as st
from forms.contact import contact_form

st.markdown("""
            <style>
            #root > div:nth-child(1) > div.withScreencast > div > div > section.stMain.st-emotion-cache-bm2z3a.ea3mdgi8 > div.stMainBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.stHorizontalBlock.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(1) > div > div > div > div > div > div > div.stImage.st-emotion-cache-kn8v7q.e115fcil2 > div > img{
                border-radius:50%
            }
            </style>
            """,unsafe_allow_html=True)

@st.dialog("Contact Me")        
def show_contact_form():
    contact_form()

# --- HERO SECTION ---#
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/profile.png", width=300, caption="Trying to make myself better.")

with col2:
    st.title("Arnav Kashyap", anchor=False)
    st.write(
        "Software Engineer, assisting enterprises by supporting data-driven decision-making."
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()
        
# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications 🦜", anchor=False)
st.write(
    """
    - 2 Years experience extracting actionable insights from data
    - Strong hands-on experience and knowledge in Python and Excel
    - Good understanding of Generative AI Models and Embeddings
    - Excellent team-player and displaying a strong sense of initiative on tasks
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills 🤹‍♀️", anchor=False)
st.write(
    """
    - Programming: Python (Scikit-learn, Pandas), SQL, JAVA
    - Generative-AI Technologies: LLM models (OpenAI, Mistral, Llama2), VectorDb(FAISS, ChromaDb, Pinecone, Cassandra)
    - Tech and Frameworks: Rag, Langchain, Groq, HuggingFace, Streamlit,
    - Cloud Platforms: Azure - OpenAI Studio, DataFactory, AI Search, Databricks
    - Softskills: Analytical Thinking, Problem Solving, Teamwork
    """
)
