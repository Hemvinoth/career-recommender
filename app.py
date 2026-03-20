import streamlit as st

st.set_page_config(page_title="Career Recommender", page_icon="🎓")
st.title("🎓 Career Recommender System")
st.write("Welcome, Hemvinoth! Your project is live.")

# Simple interactive part
skill = st.selectbox("Select your best skill:", ["Python", "Data Science", "Web Dev"])
if st.button("Recommend Career"):
    st.balloons()
    st.success(f"Based on {skill}, you should be a Senior {skill} Engineer!")
