import streamlit as st

st.set_page_config(page_title="Career Recommender", page_icon="🎓")
st.title("🎓 Career Recommender System")

# 1. Inputs (Matching your image)
qual = st.selectbox("Qualification:", ["B.Tech / BE", "M.Tech", "B.Sc", "MBA", "Others"])
gap = st.slider("Career Gap (Years):", 0, 10, 1)
skills = st.text_input("Current Skills:", "Python, SQL")

# 2. Salary Logic (Example matching your project)
# You can change these numbers to match your specific code
est_min = 350000
est_max = 600000

# 3. Output logic
if st.button("Get Recommendation"):
    st.balloons()
    st.subheader("Results:")
    
    # Recommendation text
    st.write(f"*Target Role:* Software Engineer / Data Analyst")
    st.write(f"*Expected Salary Range in Chennai:* ₹{est_min:,} - ₹{est_max:,}")
    
    if gap >= 4:
        st.warning(f"Note: With a {gap} year gap, finish one small project to boost your profile!")
    else:
        st.success("Your profile looks strong for entry-level roles!")

    st.info(f"Recommended Next Skill: Advanced {skills.split(',')[0]}")
