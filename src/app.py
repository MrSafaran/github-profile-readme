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
    about_me = st.text_area("About Me", placeholder="Write a few lines about yourself...")

# Get Social Media
st.header(":iphone: Social Media")
with st.expander("Social Media"):
    st.caption("Enter your social media username (not the URL):")
    col1, col2 = st.columns(2)
    linkedin = col1.text_input("LinkedIn")
    telegram = col2.text_input("Telegram")
    instagram = col1.text_input("Instagram")
    twitter = col2.text_input("Twitter")
    github = col1.text_input("GitHub")
    youtube = col2.text_input("YouTube")

# Get Skills
st.header("Skills")
with st.expander("Skills"):
    skill = st.text_input("Enter your skill:")
    if st.button("Add Skill"):
        if skill:
            if 'skills' not in st.session_state:
                st.session_state.skills = []
            st.session_state.skills.append(skill)
            st.success(f"The skill '{skill}' added successfully!")
        else:
            st.error("Please enter a skill.")

st.subheader("Your Skills:")
if 'skills' in st.session_state:
    skills = st.session_state.skills
    cols = st.columns(3)
    for i, skill in enumerate(skills):
        cols[i % 3].write(f"- {skill}")

# Get Tech Stacks
st.header("Tech Stacks")
with st.expander("Tech Stacks"):
    stack = st.text_input("Enter your Tech Stack:")
    if st.button("Add Stack"):
        if stack:
            if 'stacks' not in st.session_state:
                st.session_state.stacks = []
            st.session_state.stacks.append(stack)
            st.success(f"The Tech Stack '{stack}' added successfully!")
        else:
            st.error("Please enter a Tech Stack.")

st.subheader("Your Tech Stacks:")
if 'stacks' in st.session_state:
    stacks = st.session_state.stacks
    cols = st.columns(3)
    for i, stack in enumerate(stacks):
        cols[i % 3].write(f"- {stack}")

# Select theme
st.header("Theme")
themes_dir = Path("src/themes")
themes = [theme.name for theme in themes_dir.iterdir() if theme.is_file() and theme.suffix == '.md']
theme = st.selectbox("Select a Theme", themes)
st.write(f"Selected theme: **{theme}**")

# Generate the README
if st.button("Generate README"):
    # Load template
    env = Environment(loader=FileSystemLoader(str(themes_dir)))
    template = env.get_template(theme)

    # Prepare data for template
    data = {
        "name": name,
        "phone": phone,
        "email": email,
        "website": website,
        "location": location,
        "about_me": about_me,
        "linkedin": linkedin,
        "telegram": telegram,
        "instagram": instagram,
        "twitter": twitter,
        "github": github,
        "youtube": youtube,
        "skills": st.session_state.get('skills', []),
        "stacks": st.session_state.get('stacks', [])
    }

    # Render template
    output = template.render(**data)

    # Display output
    st.markdown("### 📄 Generated README")
    st.code(output, language="markdown")
    st.markdown("<h1 style='color: Green; text-align: center; border-bottom: solid 1px gray; padding-bottom: 1px; margin-bottom:3px;'>Preview</h1>", unsafe_allow_html=True)
    st.caption("For better experience copy and paste the code to a markdown viewer environment.")
    st.markdown(output)

    # Download button
    st.download_button(
        label="Download README.md",
        data=output,
        file_name="README.md",
        mime="text/markdown"
    )