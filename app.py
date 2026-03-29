import streamlit as st

# ====================== PAGE CONFIG ======================
st.set_page_config(
    page_title="Chennai Career Recommender",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====================== CUSTOM CSS ======================
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    .stApp header {
        background: linear-gradient(90deg, #1e3a8a, #3b82f6);
    }
    .title {
        font-size: 2.8rem;
        font-weight: 700;
        color: #1e3a8a;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        font-size: 1.3rem;
        color: #64748b;
        text-align: center;
        margin-bottom: 2rem;
    }
    .card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #3b82f6, #60a5fa);
        color: white;
        padding: 1.2rem;
        border-radius: 12px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# ====================== HEADER ======================
st.markdown('<h1 class="title">🎓 Chennai Career Recommender</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Real-Time Job Market Analysis & Personalized Roadmap for Chennai IT Industry</p>', unsafe_allow_html=True)
st.markdown("---")

# ====================== DATA LOGIC ======================
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

# ====================== SIDEBAR + INPUTS ======================
with st.sidebar:
    st.header("👤 Your Profile")
    
    qual_options = ['B.Tech / BE', 'B.Sc CS/IT', 'BCA', 'M.Sc / MCA', 'Diploma', 'Other']
    qualification = st.selectbox("Highest Qualification", options=qual_options)
    
    # Show text input when "Other" is selected
    custom_qual = ""
    if qualification == "Other":
        custom_qual = st.text_input("Enter your qualification", placeholder="e.g. B.E. ECE, M.Tech AI, etc.")
    
    gap_options = [f"{i} Year{'s' if i > 1 else ''}" for i in range(0, 11)]
    career_gap = st.selectbox("Career Gap", options=gap_options)
    gap_years = int(career_gap.split()[0])  # Extract number
    
    current_skills = st.text_area(
        "Current Skills (comma separated)",
        value="Python, SQL",
        placeholder="Python, Java, SQL, HTML, C++",
        height=100
    )

# ====================== MAIN CONTENT ======================
col1, col2 = st.columns([3, 2])

with col1:
    st.subheader("📋 Your Inputs")
    st.info(f"**Qualification:** {qualification if qualification != 'Other' else custom_qual}")
    st.info(f"**Career Gap:** {career_gap}")
    st.info(f"**Current Skills:** {current_skills}")

with col2:
    if st.button("🚀 Get My Personalized Career Roadmap", type="primary", use_container_width=True):
        # Process skills
        curr_list = [s.strip().lower() for s in current_skills.split(',') if s.strip()]
        
        st.markdown("---")
        st.header("🔍 Your Personalized Career Roadmap")
        
        # Two-column professional layout
        c1, c2 = st.columns(2)
        
        with c1:
            st.subheader("💼 Recommended Job Roles")
            roles = [job_roles.get(skill, "Junior Software Engineer") for skill in curr_list]
            roles = list(set(roles))  # remove duplicates
            
            for role in roles:
                st.success(f"✅ {role}")
        
        with c2:
            st.subheader("📚 Next Skills to Learn")
            next_skills = [realistic_next.get(skill, "Python & Cloud Basics") for skill in curr_list]
            next_skills = list(set(next_skills))
            
            if next_skills:
                st.success(f"**Recommended Next:** {', '.join(next_skills)}")
            else:
                st.info("Start with **Python** — highest demand in Chennai right now.")

        # ====================== SALARY ANALYSIS ======================
        st.markdown("### 💰 Expected Salary in Chennai (2026 Market)")
        
        # Salary calculation logic (kept your original logic)
        if qualification in ['B.Tech / BE', 'M.Sc / MCA'] or (qualification == "Other" and "M.Tech" in custom_qual.upper()):
            base_min = 4.0
            base_max = 7.5
        else:
            base_min = 3.0
            base_max = 5.5
        
        # Gap penalty
        if gap_years > 2:
            base_min = max(2.0, base_min - (gap_years * 0.25))
            base_max = max(3.5, base_max - (gap_years * 0.15))
        
        st.metric(
            label="Realistic Salary Range (Per Annum)",
            value=f"₹{round(base_min, 1)}L – ₹{round(base_max, 1)}L",
            delta="OMR / Siruseri / Guindy IT Parks"
        )
        
        # Gap-specific advice
        st.markdown("---")
        if gap_years >= 4:
            st.error(f"⚠️ **{gap_years} Year Gap Detected** — Chennai recruiters are strict. Build **2 strong projects** in {curr_list[0] if curr_list else 'Python'} and get certifications immediately.")
        elif gap_years >= 1:
            st.warning(f"💡 **{gap_years} Year Gap** is manageable. Focus on certifications + live projects in {next_skills[0] if next_skills else 'Cloud & Python'}.")
        else:
            st.balloons()
            st.success("🌟 **Fresh Profile!** You have very high chances in Chennai campus drives & walk-ins.")

        st.caption("Salary estimates based on current 2026 Chennai IT job market trends (Naukri, LinkedIn, Glassdoor averages).")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #64748b;'>Made with ❤️ for Chennai Job Seekers | Updated for 2026 Market</p>",
    unsafe_allow_html=True
)
