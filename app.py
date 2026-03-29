import streamlit as st

st.set_page_config(
    page_title="Chennai Career Recommender",
    page_icon="🎓",
    layout="centered"
)

# Modern Colorful CSS
st.markdown("""
<style>
    .main { background: linear-gradient(135deg, #f0f9ff, #e0f2fe); }
    .hero { text-align: center; padding: 1rem 0 2rem 0; }
    .title { font-size: 3.4rem; font-weight: 800; color: #1e40af; margin: 0; }
    .subtitle { font-size: 1.35rem; color: #334155; margin-top: 0.5rem; }
    .input-card, .result-card {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.12);
        margin: 1.5rem 0;
    }
    .stButton>button {
        background: linear-gradient(90deg, #2563eb, #1e40af);
        color: white;
        font-size: 1.25rem;
        font-weight: bold;
        border-radius: 50px;
        height: 3.8rem;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# ====================== HERO SECTION WITH CAREER IMAGE ======================
st.markdown('<div class="hero">', unsafe_allow_html=True)

# Reliable Career Image (Professional IT Job Scene)
st.image(
    "https://source.unsplash.com/1200x400/?professional,career,technology",
    use_container_width=True
)

st.markdown('🎓 <span class="title">Chennai Career Recommender</span>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Real-Time Personalized Roadmap for Chennai IT Job Market (2026)</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ====================== DATA ======================
realistic_next = {
    'python': 'AWS Basics & Django', 'sql': 'Power BI & Tableau',
    'java': 'Spring Boot & Microservices', 'c': 'Python & Embedded Systems',
    'html': 'React.js & Tailwind CSS', 'general it': 'Python & SQL'
}

job_roles = {
    'python': 'Python Developer / Data Scientist',
    'sql': 'Data Analyst / Database Administrator',
    'java': 'Java Backend Developer',
    'c': 'System Programmer / Software Engineer',
    'html': 'Front-end Developer / Web Designer',
    'general it': 'IT Support / System Admin'
}

# ====================== INPUT SECTION (Clean & Visible) ======================
with st.container():
    st.markdown('<div class="input-card">', unsafe_allow_html=True)
    
    st.subheader("👤 Your Profile Details")
    
    col1, col2 = st.columns(2)
    with col1:
        qual_options = ['B.Tech / BE', 'B.Sc CS/IT', 'BCA', 'M.Sc / MCA', 'Diploma', 'Other']
        qualification = st.selectbox("Highest Qualification", qual_options)
        custom_qual = ""
        if qualification == "Other":
            custom_qual = st.text_input("Enter your qualification", placeholder="e.g. B.E. ECE, M.Tech AI")

    with col2:
        gap_options = [f"{i} Year{'s' if i > 1 else ''}" for i in range(0, 11)]
        career_gap_str = st.selectbox("Career Gap", gap_options)
        gap_years = int(career_gap_str.split()[0])

    current_skills = st.text_area(
        "Current Skills (comma separated)",
        value="Python, SQL",
        placeholder="Python, Java, SQL, HTML, React",
        height=100
    )
    
    st.markdown('</div>', unsafe_allow_html=True)

# ====================== ANALYZE BUTTON ======================
if st.button("🚀 Get My Personalized Career Roadmap"):
    curr_list = [s.strip().lower() for s in current_skills.split(',') if s.strip()]

    st.markdown("---")
    st.markdown('<div class="result-card">', unsafe_allow_html=True)

    st.header("🔍 Your Personalized Career Roadmap")

    rcol1, rcol2 = st.columns(2)

    with rcol1:
        st.subheader("💼 Recommended Job Roles")
        st.image("https://source.unsplash.com/600x280/?job,career,professional", use_container_width=True)
        roles = [job_roles.get(skill, "Junior Software Engineer") for skill in curr_list]
        for role in list(set(roles)):
            st.success(f"✅ {role}")

    with rcol2:
        st.subheader("📚 Next Skills to Upgrade")
        st.image("https://source.unsplash.com/600x280/?learning,skills,upgrade", use_container_width=True)
        next_skills = [realistic_next.get(skill, "Python & Cloud Basics") for skill in curr_list]
        if next_skills:
            st.success(f"**Learn Next:** {', '.join(list(set(next_skills)))}")

    # Salary Section
    st.subheader("💰 Expected Salary in Chennai (2026)")
    st.image("https://source.unsplash.com/800x250/?salary,growth,money", use_container_width=True)

    # Salary Calculation
    if qualification in ['B.Tech / BE', 'M.Sc / MCA'] or (qualification == "Other" and any(x in (custom_qual or "").upper() for x in ["M.TECH", "ME", "MASTER"])):
        base_min, base_max = 4.2, 8.0
    else:
        base_min, base_max = 3.0, 5.8

    if gap_years > 2:
        base_min = max(2.2, base_min - gap_years * 0.25)
        base_max = max(4.0, base_max - gap_years * 0.15)

    st.metric("Realistic Annual Package", f"₹{round(base_min,1)}L – ₹{round(base_max,1)}L")

    # Advice
    if gap_years >= 4:
        st.error(f"⚠️ {gap_years} Year Gap — Build 2 strong projects in {curr_list[0] if curr_list else 'Python'} now!")
    elif gap_years >= 1:
        st.warning(f"💡 {gap_years} Year Gap manageable. Focus on certifications.")
    else:
        st.balloons()
        st.success("🌟 Fresh Profile! High chances in Chennai walk-ins.")

    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center; color:#64748b;'>Made with ❤️ for Chennai Job Seekers | Updated for 2026</p>", unsafe_allow_html=True)
