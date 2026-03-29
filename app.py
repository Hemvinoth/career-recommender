import streamlit as st

st.set_page_config(
    page_title="Chennai Career Recommender",
    page_icon="🎯",
    layout="centered"
)

# Clean Professional + Colorful CSS
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%);
    }
    .title {
        font-size: 3.2rem;
        font-weight: 800;
        color: #1e40af;
        text-align: center;
        margin-bottom: 0.3rem;
    }
    .subtitle {
        font-size: 1.35rem;
        color: #334155;
        text-align: center;
        margin-bottom: 2rem;
    }
    .card {
        background: white;
        padding: 2rem;
        border-radius: 18px;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
        margin: 1.5rem 0;
    }
    .stButton>button {
        background: linear-gradient(90deg, #2563eb, #1e40af);
        color: white;
        font-size: 1.25rem;
        font-weight: bold;
        border-radius: 50px;
        height: 3.6rem;
        width: 100%;
    }
    .result-card {
        background: white;
        padding: 2rem;
        border-radius: 18px;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="title">🎯 Chennai Career Recommender</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Real-Time Personalized Roadmap for Chennai IT Job Market (2026)</p>', unsafe_allow_html=True)

# Data
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

# Input Section - Clean Card
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
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

    current_skills = st.text_area(
        "Current Skills (comma separated)",
        value="Python, SQL",
        placeholder="Python, Java, SQL, HTML, React",
        height=100
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Button & Results
if st.button("🚀 Get My Personalized Career Roadmap"):
    curr_list = [s.strip().lower() for s in current_skills.split(',') if s.strip()]

    st.markdown("---")
    st.markdown('<div class="result-card">', unsafe_allow_html=True)

    st.header("🔍 Your Personalized Career Roadmap")

    rcol1, rcol2 = st.columns(2)

    with rcol1:
        st.subheader("💼 Recommended Job Roles")
        roles = [job_roles.get(skill, "Junior Software Engineer") for skill in curr_list]
        for role in list(set(roles)):
            st.success(f"✅ {role}")

    with rcol2:
        st.subheader("📚 Next Skills to Upgrade")
        next_skills = [realistic_next.get(skill, "Python & Cloud Basics") for skill in curr_list]
        if next_skills:
            st.success(f"**Learn Next:** {', '.join(list(set(next_skills)))}")

    # Salary
    st.subheader("💰 Expected Salary in Chennai (2026)")

    if qualification in ['B.Tech / BE', 'M.Sc / MCA'] or (qualification == "Other" and any(x in (custom_qual or "").upper() for x in ["M.TECH", "ME", "MASTER"])):
        base_min, base_max = 4.2, 8.0
    else:
        base_min, base_max = 3.0, 5.8

    if gap_years > 2:
        base_min = max(2.2, base_min - gap_years * 0.25)
        base_max = max(4.0, base_max - gap_years * 0.15)

    st.metric("Realistic Annual Package", f"₹{round(base_min,1)}L – ₹{round(base_max,1)}L")

    # Gap Advice
    if gap_years >= 4:
        st.error(f"⚠️ {gap_years} Year Gap — Build 2 strong projects immediately!")
    elif gap_years >= 1:
        st.warning(f"💡 {gap_years} Year Gap is manageable. Focus on certifications.")
    else:
        st.balloons()
        st.success("🌟 Fresh Profile! High chances in Chennai walk-ins.")

    st.caption("Based on 2026 Chennai IT market trends.")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center; color:#475569; font-size:1rem;'>Made with ❤️ for Chennai Job Seekers | 2026 Updated</p>", unsafe_allow_html=True)
