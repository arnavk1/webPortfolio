import streamlit as st

st.subheader("Project Summary", anchor=False)
st.write(
    """
    - The website integrates AI to provide interactive elements, dynamic content updates, and tailored experiences based on user behavior (browsing history, project interests).
    - Implement AI chatbot to guide users through your portfolio and answer their questions about specific projects or technologies used.
    - You can interact with chatbot to know more about me😁
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Technologies Used 👩‍💻", anchor=False)
st.write(
    """
    - Hugging Face (For LLM Deployment): Hugging Face is a fantastic platform for deploying and hosting my LLM model, allowing for seamless integration with other tools.
    - Streamlit: For highly interactive and minimal development experience, Streamlit is perfect for quick demos and prototypes.
    - OpenAI API: This is my primary gateway to OpenAI's powerful language model (e.g., GPT-3). It allows you to integrate these models into my website.
    - Database: Cassandra excels at handling large volumes of data, which is ideal if you have diverse project information or need to process user interactions in real-time.
    """
)

st.write("\n")
st.subheader("Just a Note 📝: ", anchor=False)
st.write(
    """
    Let me know if you'd like help with implementing any of these concepts!  Feel free to ask about specific technical details related to embedding, Cassandra integration, or my any overall project ideas.
    """
)