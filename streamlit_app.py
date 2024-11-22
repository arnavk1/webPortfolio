import streamlit as st

# page setup##
st.set_page_config(page_title="Arnav Kashyap", page_icon=":material/edit:")

about_page=st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True
)

project_page_1 = st.Page(
    page="views/knowAboutMeBot.py",
    title="Chat Bot",
    icon=":material/smart_toy:"
)
project_page_2 = st.Page(
    page="views/current_project.py",
    title="Project Summary",
    icon=":material/summarize:"
)

# pg = st.navigation(pages=[about_page,project_page_1,project_page_2])

pg = st.navigation(
    {
        "Info": [about_page, project_page_2],
        "Talk With Me":[project_page_1]
    }
)

st.logo("assets/logo.png",size='large',)
st.sidebar.markdown("Made with ❤ by Arnav")
#run navigation
pg.run()
