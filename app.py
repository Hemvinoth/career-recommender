import streamlit as st

st.set_page_config(
    page_title="Chennai Career Recommender",
    page_icon="🎯",
    layout="centered"
)

# Professional + Colorful CSS
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
        color: white;
    }
    .title {
        font-size: 3.4rem;
        font-weight: 800;
        text-align: center;
        margin: 1.5rem 0 0.5rem 0;
        color: white;
    }
    .card {
        background: white;
        color: #1e2937;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        margin: 1.5rem 0;
    }
    .result-card {
        background: white;
        color: #1e2937;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    }
    .stButton>button {
        background: linear-gradient(90deg, #f59e0b, #ea580c);
        color: white;
        font-size: 1.25rem;
        font-weight: bold;
        border-radius: 50px;
        height: 3.7rem;
        width: 100%;
    }
    /* Clean multiselect - no pink box */
    .stMultiSelect [data-baseweb="tag"] {
        background-color: #e0f2fe !important;
        color: #1e40af !important;
    }
</style>
""", unsafe_allow_html=True)

# Title at Top
st.markdown('<h1 class="title">🎯 Chennai Career Recommender</h1>', unsafe_allow_html=True)

# Data
realistic_next = {
    'python': 'AWS Basics & Django', 'sql': 'Power BI & Tableau',
    'java': 'Spring Boot & Microservices', 'c': 'Python & Embedded Systems',
    'html': 'React.js & Tailwind CSS', 'javascript': 'React.js & Node.js',
    'css': 'Tailwind CSS & Bootstrap', 'general it': 'Python & SQL'
}

job_roles = {
    'python': 'Python Developer / Data Scientist',
    'sql': 'Data Analyst / Database Administrator',
    'java': 'Java Backend Developer',
    'c': 'System Programmer / Software Engineer',
    'html': 'Front-end Developer / Web Designer',
    'javascript': 'Full Stack Developer',
    'css': 'UI/UX Developer',
    'general it': 'IT Support / System Admin'
}

common_skills = [
    "Python", "SQL", "Java", "C", "HTML", "CSS", "JavaScript", "React.js", 
    "Django", "Power BI", "Tableau", "AWS", "Docker", "Git", "Machine Learning"
]

# Input Card - Subtitle INSIDE white box
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    # Subtitle moved inside white box
    st.markdown('<p style="text-align: center; font-size: 1.25rem; color: #334155; margin-bottom: 1.5rem; font-weight: 600;">Real-Time Personalized Roadmap for Chennai IT Job Market (2026)</p>', unsafe_allow_html=True)
    
    st.subheader("👤 Your Profile Details")

    col1, col2 = st.columns(2)
    with col1:
        qual_options = ['B.Tech / BE', 'B.Sc CS/IT', 'BCA', 'M.Sc / MCA', 'Diploma', 'Other']
        qualification = st.selectbox("Highest Qualification", qual_options)
        custom_qual = st.text_input("Enter your qualification", placeholder="e.g. B.E. ECE, M.Tech AI") if qualification == "Other" else ""

    with col2:
        gap_options = [f"{i} Year{'s' if i > 1 else ''}" for i in range(0, 11)]
        career_gap_str = st.selectbox("Career Gap", gap_options)
        gap_years = int(career_gap_str.split()[0])

    # Current Skills - Multi-select Dropdown
    st.subheader("💻 Current Skills")
    selected_skills = st.multiselect(
        "Select your current skills",
        options=common_skills,
        default=["Python", "SQL"],
        help="You can select multiple skills"
    )
    
    custom_skill = st.text_input("Add any other skill (optional)", placeholder="e.g. Kotlin, Flutter, Cyber Security")
    if custom_skill.strip():
        selected_skills.append(custom_skill.strip())

    st.markdown('</div>', unsafe_allow_html=True)

# Main Button & Results
if st.button("🚀 Get My Personalized Career Roadmap"):
    curr_list = [s.strip().lower() for s in selected_skills if s.strip()]

    st.markdown("---")
    st.markdown('<p class="inside-subtitle">Real-Time Personalized Roadmap for Chennai IT Job Market (2026)</p>', unsafe_allow_html=True)
    

    st.header("🔍 Your Personalized Career Roadmap")

    rcol1, rcol2 = st.columns(2)

    with rcol1:
        st.subheader("💼 Recommended Job Roles")
        roles = []
        for skill in curr_list:
            role = job_roles.get(skill, "Junior Software Engineer / IT Professional")
            if role not in roles:
                roles.append(role)
        for role in roles:
            st.success(f"✅ {role}")

    with rcol2:
        st.subheader("📚 Next Skills to Upgrade")
        next_skills = []
        for skill in curr_list:
            ns = realistic_next.get(skill, "Cloud Computing & Python")
            if ns not in next_skills:
                next_skills.append(ns)
        if next_skills:
            st.success(f"**Learn Next:** {', '.join(next_skills)}")

    # Salary Section
    st.subheader("💰 Expected Salary in Chennai (2026)")

    if qualification in ['B.Tech / BE', 'M.Sc / MCA'] or (qualification == "Other" and any(x in (custom_qual or "").upper() for x in ["M.TECH", "ME", "MASTER"])):
        base_min, base_max = 4.2, 8.0
    else:
        base_min, base_max = 3.0, 5.8

    if gap_years > 2:
        base_min = max(2.2, base_min - gap_years * 0.25)
        base_max = max(4.0, base_max - gap_years * 0.15)

    st.metric("Realistic Annual Package", f"₹{round(base_min,1)}L – ₹{round(base_max,1)}L")

    if gap_years >= 4:
        st.error(f"⚠️ {gap_years} Year Gap — Build 2 strong projects immediately!")
    elif gap_years >= 1:
        st.warning(f"💡 {gap_years} Year Gap is manageable.")
    else:
        st.balloons()
        st.success("🌟 Fresh Profile! High chances in Chennai campus drives & walk-ins.")

    st.caption("Analysis based on current 2026 Chennai IT job market trends.")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer - Fixed visibility
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#black; font-size:1.1rem; margin-top: 1rem;'>"
    "Made with ❤️ for Chennai Job Seekers | Updated for 2026 Market"
    "</p>",
    unsafe_allow_html=True
)
