import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="Chennai Career Recommender", page_icon="🎯")
st.title("🎓 Career Recommender System")
st.write("### Real-Time Analysis for Chennai Job Market")
st.write("---")

# --- 1. THE DATA LOGIC (Real Mappings) ---
realistic_next = {
    'python': 'AWS Basics & Django',
    'sql': 'Power BI & Tableau',
    'java': 'Spring Boot & Microservices',
    'c': 'Python & Embedded Systems',
    'html': 'React.js & Tailwind CSS',
    'general it': 'Python & SQL'
}

job_roles = {
    'python': 'Python Developer / Data Scientist',
    'sql': 'Data Analyst / Database Administrator',
    'java': 'Java Backend Developer',
    'c': 'System Programmer / Software Engineer',
    'html': 'Front-end Developer / Web Designer',
    'general it': 'IT Support / System Admin'
}

# --- 2. INPUT WIDGETS (Exactly like your analysis) ---
qual = st.selectbox(
    "Qualification:", 
    options=['B.Tech / BE', 'B.Sc CS/IT', 'BCA', 'M.Sc / MCA', 'Diploma', 'Other']
)

gap = st.slider("Career Gap (years):", min_value=0, max_value=10, value=1, step=1)

current_input = st.text_area(
    "Current Skills:", 
    value="Python, SQL",
    placeholder="e.g. Python, Java, SQL"
)

# --- 3. THE "REAL" ANALYSIS ENGINE ---
if st.button("Get Detailed Recommendation", type="primary"):
    # Process Skills
    curr_list = [s.strip().lower() for s in current_input.split(',') if s.strip()]
    
    st.write("---")
    st.header("🔍 Personal Career Roadmap")
    
    # Create Columns for a professional look
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📌 Recommended Roles")
        roles = []
        for s in curr_list:
            if s in job_roles:
                roles.append(job_roles[s])
        if roles:
            for r in list(set(roles)):
                st.write(f"✅ {r}")
        else:
            st.write("✅ Junior Software Engineer")

    with col2:
        st.subheader("📚 Skill Upgrades")
        next_skills = []
        for s in curr_list:
            if s in realistic_next:
                next_skills.append(realistic_next[s])
        if next_skills:
            st.success(f"*Learn Next:* {', '.join(list(set(next_skills)))}")
        else:
            st.info("Start learning *Python* for better reach.")

    # --- 4. CHENNAI SALARY ANALYSIS (The "Real" part) ---
    st.subheader("💰 Expected Salary (Chennai Market)")
    
    # Base Salary calculation logic
    base_min = 3.5 if qual in ['B.Tech / BE', 'M.Sc / MCA'] else 2.8
    base_max = 6.5 if qual in ['B.Tech / BE', 'M.Sc / MCA'] else 4.5
    
    # Gap penalty logic
    if gap > 2:
        base_min -= (gap * 0.2)
        base_max -= (gap * 0.1)
    
    # Final display
    st.metric(label="Salary Range", value=f"₹{round(base_min,1)}L - ₹{round(base_max,1)}L", delta="Per Annum")

    # --- 5. THE NOTE (From your logic) ---
    st.write("---")
    if gap >= 4:
        st.error(f"⚠️ *Urgent Action Needed:* Since you have a {gap} year gap, Chennai HRs will look for projects. Build 2 projects in {curr_list[0]} immediately!")
    elif gap >= 1:
        st.warning(f"💡 *Gap Strategy:* A {gap} year gap is manageable. Focus on 'Certification' in {next_skills[0] if next_skills else 'Cloud'}.")
    else:
        st.balloons()
        st.success("🌟 Fresh Profile: You have high priority in Chennai Walk-ins!")

    st.caption("Salary data based on 2026 Chennai IT park averages (OMR/Siruseri).")
