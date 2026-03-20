import streamlit as st

# --- CONFIG & STYLING ---
st.set_page_config(page_title="Career Recommender", page_icon="🎓")
st.title("🎓 Career Recommender System")
st.write("---")

# --- MAPPING LOGIC (From your Image) ---
realistic_next = {
    'python': 'AWS Basics',
    'sql': 'Power BI',
    'java': 'Spring Boot',
    'c': 'Python',
    'html': 'React Basics',
    'general it': 'Python'
}

# --- INPUT WIDGETS (Matching your Image) ---
qual = st.selectbox(
    "Qualification:", 
    options=['B.Tech / BE', 'B.Sc CS/IT', 'BCA', 'M.Sc / MCA', 'Diploma', 'Other']
)

gap = st.slider("Career Gap (years):", min_value=0, max_value=10, value=1, step=1)

current = st.text_area(
    "Current Skills:", 
    value="Python, SQL",
    placeholder="comma separated, e.g. Python, Java, SQL"
)

# --- CLEAN LOGIC (The "Get Recommendation" Button) ---
if st.button("Get Recommendation", type="primary"):
    # Processing the input
    curr_raw = current.strip()
    curr_list = [s.strip().lower() for s in curr_raw.split(',') if s.strip()]
    
    st.write("---")
    st.subheader("Your Career Analysis")
    
    # 1. Show Qualification and Gap
    st.write(f"*Qualification:* {qual}")
    st.write(f"*Career Gap:* {gap} years")
    
    # 2. Find Next Skills
    found_recommendations = []
    for skill in curr_list:
        if skill in realistic_next:
            found_recommendations.append(realistic_next[skill])
    
    # 3. Display Result
    if found_recommendations:
        unique_next = list(set(found_recommendations))
        st.success(f"✅ Based on your skills, you should learn: *{', '.join(unique_next)}*")
    else:
        st.info("💡 Keep strengthening your current skills or explore Python/AWS!")

    # 4. Gap Warning Logic (From your logic)
    if gap >= 4:
        st.warning(f"⚠️ Note: With a {gap} year gap, we recommend finishing 1 small project + the next skill mentioned above.")
    else:
        st.balloons()
        st.write("✨ You are in a good position to apply for entry-level roles!")

    # 5. Salary range (Standard estimation)
    st.write("*Estimated Starting Salary:* ₹3.5L - ₹6L per annum")
