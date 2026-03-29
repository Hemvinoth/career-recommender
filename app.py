import streamlit as st

st.set_page_config(
    page_title="Chennai Career Recommender",
    page_icon="🎓",
    layout="centered"
)

# Custom CSS - More Colorful & Professional
st.markdown("""
<style>
    .main { background: linear-gradient(135deg, #f0f9ff, #e0f2fe); }
    .hero { text-align: center; padding: 1rem 0; }
    .title { font-size: 3.3rem; font-weight: 800; color: #1e40af; }
    .subtitle { font-size: 1.4rem; color: #334155; }
    .input-card, .result-card {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.12);
        margin: 1.5rem 0;
    }
    .stButton>button {
        background: linear-gradient(90deg, #2563eb, #1d4ed8);
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

# Career-based Hero Image (Chennai IT / Career Growth Theme)
hero_image_url = "https://source.unsplash.com/featured/1200x400/?career,technology,india"
st.image(hero_image_url, use_container_width=True)

st.markdown('🎓 <span class="title">Chennai Career Recommender</span>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Real-Time Personalized Roadmap for Chennai IT Job Market (2026)</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Data (same as before)
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

# ====================== INPUT SECTION ======================
with st.container():
    st.markdown('<div class="input-card">', unsafe_allow_html=True)
    st.subheader("👤 Your Profile Details")

    col1, col2 = st.columns(2)
    with col1:
        qual_options = ['B.Tech / BE', 'B.Sc CS/IT', 'BCA', 'M.Sc / MCA', 'Diploma', 'Other']
        qualification = st.selectbox("Highest Qualification", qual_options)
        custom_qual = st.text_input("Specify if Other", placeholder="e.g. B.E. ECE") if qualification == "Other" else ""

    with col2:
        gap_options = [f"{i} Year{'s' if i > 1 else ''}" for i in range(0, 11)]
        career_gap_str = st.selectbox("Career Gap", gap_options)
        gap_years = int(career_gap_str.split()[0])

    current_skills = st.text_area("Current Skills (comma separated)", value="Python, SQL", placeholder="Python, Java, SQL, HTML", height=100)
    st.markdown('</div>', unsafe_allow_html=True)

# ====================== BUTTON & RESULTS ======================
if st.button("🚀 Get My Personalized Career Roadmap"):
    curr_list = [s.strip().lower() for s in current_skills.split(',') if s.strip()]

    st.markdown("---")
    st.markdown('<div class="result-card">', unsafe_allow_html=True)

    st.header("🔍 Your Personalized Career Roadmap")

    # Career Images in Results
    rcol1, rcol2 = st.columns(2)

    with rcol1:
        st.subheader("💼 Recommended Job Roles")
        st.image("https://source.unsplash.com/featured/600x300/?job,career", use_container_width=True)
        roles = [job_roles.get(skill, "Junior Software Engineer") for skill in curr_list]
        for role in list(set(roles)):
            st.success(f"✅ {role}")

    with rcol2:
        st.subheader("📚 Next Skills to Upgrade")
        st.image("https://source.unsplash.com/featured/600x300/?skills,learning", use_container_width=True)
        next_skills = [realistic_next.get(skill, "Python & Cloud") for skill in curr_list]
        if next_skills:
            st.success(f"**Learn Next:** {', '.join(list(set(next_skills)))}")

    # Salary with image
    st.subheader("💰 Expected Salary in Chennai (2026)")
    st.image("https://source.unsplash.com/featured/800x250/?salary,money,growth", use_container_width=True)

    # Salary logic (same accurate calculation)
    if qualification in ['B.Tech / BE', 'M.Sc / MCA'] or (qualification == "Other" and any(x in custom_qual.upper() for x in ["M.TECH","ME","MASTER"])):
        base_min, base_max = 4.2, 8.0
    else:
        base_min, base_max = 3.0, 5.8

    if gap_years > 2:
        base_min = max(2.2, base_min - gap_years * 0.25)
        base_max = max(4.0, base_max - gap_years * 0.15)

    st.metric("Realistic Annual Package", f"₹{round(base_min,1)}L – ₹{round(base_max,1)}L", delta="Chennai IT Parks")

    # Gap Advice
    if gap_years >= 4:
        st.error(f"⚠️ {gap_years} Year Gap — Build 2 strong projects immediately!")
    elif gap_years >= 1:
        st.warning(f"💡 {gap_years} Year Gap manageable. Focus on certifications.")
    else:
        st.balloons()
        st.success("🌟 Fresh Profile! High chances in Chennai walk-ins.")

    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center;color:#64748b;'>Made with ❤️ for Chennai Job Seekers | 2026 Market</p>", unsafe_allow_html=True)
