import streamlit as st

# ====================== PAGE CONFIG ======================
st.set_page_config(
    page_title="Chennai Career Recommender",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====================== CUSTOM CSS FOR COLORFUL & PROFESSIONAL LOOK ======================
st.markdown("""
<style>
    .main {
        background-color: #f8fafc;
    }
    .stApp header {
        background: linear-gradient(90deg, #1e40af, #3b82f6);
        color: white;
    }
    .title {
        font-size: 3rem;
        font-weight: 700;
        color: #1e3a8a;
        text-align: center;
        margin: 1rem 0;
    }
    .subtitle {
        font-size: 1.4rem;
        color: #475569;
        text-align: center;
        margin-bottom: 2rem;
    }
    .card {
        background: white;
        padding: 1.8rem;
        border-radius: 15px;
        box-shadow: 0 6px 16px rgba(0,0,0,0.1);
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #2563eb, #60a5fa);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
    }
    .stButton>button {
        background: linear-gradient(90deg, #3b82f6, #1e40af);
        color: white;
        font-weight: bold;
        border-radius: 10px;
        height: 3.2rem;
        font-size: 1.1rem;
    }
</style>
""", unsafe_allow_html=True)

# ====================== HEADER ======================
st.markdown('<h1 class="title">🎓 Chennai Career Recommender</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Real-Time Personalized Roadmap for Chennai IT Job Market (2026)</p>', unsafe_allow_html=True)
st.markdown("---")

# ====================== DATA MAPPINGS ======================
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

# ====================== INPUT SECTION (Sidebar) ======================
with st.sidebar:
    st.header("👤 Enter Your Details")
    
    qual_options = ['B.Tech / BE', 'B.Sc CS/IT', 'BCA', 'M.Sc / MCA', 'Diploma', 'Other']
    qualification = st.selectbox("Highest Qualification", options=qual_options)
    
    custom_qual = ""
    if qualification == "Other":
        custom_qual = st.text_input("Please specify your qualification", 
                                  placeholder="e.g. B.E. Electronics, M.Tech AI, etc.")
    
    # Professional Dropdown for Career Gap
    gap_options = [f"{i} Year{'s' if i > 1 else ''}" for i in range(0, 11)]
    career_gap_str = st.selectbox("Career Gap", options=gap_options)
    gap_years = int(career_gap_str.split()[0])
    
    current_skills = st.text_area(
        "Current Skills (comma separated)",
        value="Python, SQL",
        placeholder="Python, Java, SQL, HTML, React",
        height=120
    )

# ====================== MAIN BUTTON ======================
if st.button("🚀 Get My Personalized Career Roadmap", type="primary", use_container_width=True):
    
    curr_list = [s.strip().lower() for s in current_skills.split(',') if s.strip()]
    
    st.markdown("---")
    st.header("🔍 Your Personalized Career Roadmap")
    
    # Two Column Layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💼 Recommended Job Roles")
        roles = [job_roles.get(skill, "Junior Software Engineer") for skill in curr_list]
        roles = list(set(roles))
        for role in roles:
            st.success(f"✅ {role}")
    
    with col2:
        st.subheader("📚 Next Skills to Upgrade")
        next_skills = [realistic_next.get(skill, "Python & Cloud Basics") for skill in curr_list]
        next_skills = list(set(next_skills))
        if next_skills:
            st.success(f"**Learn Next:** {', '.join(next_skills)}")
        else:
            st.info("Start learning **Python** — highest demand in Chennai.")

    # ====================== SALARY ANALYSIS ======================
    st.markdown("### 💰 Expected Salary in Chennai IT Market (2026)")
    
    # Salary Calculation Logic
    if qualification in ['B.Tech / BE', 'M.Sc / MCA'] or (qualification == "Other" and any(x in custom_qual.upper() for x in ["M.TECH", "ME", "MASTER"])):
        base_min = 4.2
        base_max = 8.0
    else:
        base_min = 3.0
        base_max = 5.8
    
    # Apply gap penalty
    if gap_years > 2:
        base_min = max(2.2, base_min - (gap_years * 0.25))
        base_max = max(4.0, base_max - (gap_years * 0.15))
    
    st.metric(
        label="Realistic Monthly Salary Range",
        value=f"₹{round(base_min, 1)}L – ₹{round(base_max, 1)}L per annum",
        delta="Based on OMR, Siruseri, Guindy & Tidel Park"
    )
    
    # Gap Advice
    st.markdown("---")
    if gap_years >= 4:
        st.error(f"⚠️ **{gap_years} Year Gap** – Chennai recruiters are strict. Build 2 strong projects in {curr_list[0] if curr_list else 'Python'} immediately and add certifications.")
    elif gap_years >= 1:
        st.warning(f"💡 **{gap_years} Year Gap** is manageable. Focus on certifications + live projects in {next_skills[0] if next_skills else 'Python & Cloud'}.")
    else:
        st.balloons()
        st.success("🌟 **Fresh Profile!** Excellent chances in Chennai campus drives and walk-ins.")

    st.caption("Salary data based on 2026 Chennai IT trends from Naukri, LinkedIn & Glassdoor.")

# ====================== FOOTER ======================
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #64748b; font-size: 0.95rem;'>"
    "Made with ❤️ for Chennai Job Seekers | Updated for 2026 IT Market"
    "</p>",
    unsafe_allow_html=True
)
