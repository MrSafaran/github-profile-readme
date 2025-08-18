import streamlit as st
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


st.title(":gear: GitHub Profile Generator :gear:")

# Get Personal Info
st.header(":notebook: Personal Info")
with st.expander("Personal Info"):
    col1, col2 = st.columns(2)
    name = col1.text_input("Name")
    phone = col2.text_input("Phone")
    email = col1.text_input("Email")
    website = col2.text_input("Website")
    location = st.text_input("Location")

# Get Social Media
st.header(":iphone: Social Media")
with st.expander("Social Media"):
    st.caption("Enter your social media username (not the url):")
    col1 , col2 = st.columns(2)
    Linkedin = col1.text_input("Linkedin")
    Telegram = col2.text_input("Telegram")
    Instagram = col1.text_input("Instagram")
    Twitter = col2.text_input("Twitter")
    Github = col1.text_input("Github")
    Youtube = col2.text_input("Youtube")

# Get Skills
st.header("Technical Skills")
with st.expander("Technical Skills"):
    skill = st.text_input("Enter your skill:")

    if st.button("Add"):
        if skill :
            st.session_state.skills.append(skill)
            st.success(f"The skill '{skill}' added successfully!")
        else:
            st.error("Please enter a skill.")

if 'skills' not in st.session_state:
    st.session_state.skills = []

st.subheader("Your Skills:")
if 'skills' in st.session_state:
    skills = st.session_state.skills
    cols = st.columns(3) 
    for i, skill in enumerate(skills):
        cols[i % 3].write(f"- {skill}")

# Select theme
st.header("Theme")
themes = Path("src/themes").iterdir()
themes = [theme.name for theme in themes]
theme = st.selectbox("Select a Theme",themes)
st.write(f"Selected theme : **{theme}**")

# Generate the readme
if st.button("Generate README"):
    theme_path = Path("src/themes") / theme
    env = Environment(loader=FileSystemLoader(str(theme_path)))
    template = env.get_template("template.md")

    data = {
        "name": name,
        "phone": phone,
        "email": email,
        "website": website,
        "location": location,
        "Linkedin": Linkedin,
        "Telegram": Telegram,
        "Instagram": Instagram,
        "Twitter": Twitter,
        "Github": Github,
        "Youtube": Youtube,
        "skills": skills
    }

    output = template.render(data)

    st.markdown("### 📄 Generated README")
    st.code(output, language="markdown")

    # Download button
    st.download_button(
        "Download README.md",
        output,
        file_name="README.md",
        mime="text/markdown"
    )
