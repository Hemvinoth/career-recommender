import streamlit as st

st.set_page_config(
    page_title="Chennai Career Recommender",
    page_icon="🎯",
    layout="centered"
)

# --- PROFESSIONAL GLASSMORPHISM CSS ---
st.markdown("""
<style>
    /* 1. Main Background */
    .stApp {
        background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
    }

    /* 2. Title Styling (Outside the card) */
    .main-title {
        font-size: 3rem !important;
        font-weight: 800 !important;
        text-align: center;
        color: white !important;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    /* 3. The Professional White Card */
    /* This targets the container holding the inputs */
    [data-testid="stVerticalBlock"] > div:has(div.stSelectbox) {
        background-color: white !important;
        padding: 40px !important;
        border-radius: 24px !important;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2) !important;
        margin-top: 20px;
    }

    /* 4. Text INSIDE the White Card (Subtitle & Labels) */
    .card-subtitle {
        color: #4b5563 !important; /* Professional Dark Grey */
        font-size: 1.15rem !important;
        text-align: center;
        margin-bottom: 2rem !important;
        font-weight: 500;
        border-bottom: 1px solid #f1f5f9;
        padding-bottom: 15px;
    }

    /* Force all input labels inside the card to be Dark Blue/Grey */
    [data-testid="stVerticalBlock"] > div:has(div.stSelectbox) label, 
    [data-testid="stVerticalBlock"] > div:has(div.stSelectbox) p,
    [data-testid="stVerticalBlock"] > div:has(div.stSelectbox) h3 {
        color: #1e2937 !important;
        font-weight: 600 !important;
    }

    /* 5. Modern Orange Button */
    .stButton>button {
        background: linear-gradient(90deg, #f59e0b, #ea580c) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        height: 3.8rem !important;
        font-weight: bold !important;
        font-size: 1.2rem !important;
        width: 100%;
        margin-top: 20px;
        transition: all 0.3s ease;
        box-shadow: 0 8px 20px rgba(234, 88, 12, 0.3) !important;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 25px rgba(234, 88, 12, 0.4) !important;
    }

    /* Footer Text */
    .footer-text {
        text-align: center;
        color: #dbeafe;
        font-size: 0.9rem;
        margin-top: 30px;
    }
</style>
""", unsafe_allow_html=True)

# --- APP LAYOUT ---

# Header (Outside the card)
st.markdown('<h1 class="main-title">🎯 Chennai Career Recommender</h1>', unsafe_allow_html=True)

# Main Input Card
with st.container():
    # Subtitle is now INSIDE the white box
    st.markdown('<p class="card-subtitle">Real-Time Personalized Roadmap for Chennai IT Job Market (2026)</p>', unsafe_allow_html=True)
    
    st.subheader("👤 Your Profile Details")
    
    col1, col2 = st.columns(2)
    with col1:
        qual_options = ['B.Tech / BE', 'B.Sc CS/IT', 'BCA', 'M.Sc / MCA', 'Diploma', 'Other']
        qualification = st.selectbox("Highest Qualification", qual_options)
        
    with col2:
        gap_options = [f"{i} Year{'s' if i > 1 else ''}" for i in range(0, 11)]
        career_gap_str = st.selectbox("Career Gap", gap_options)
        gap_years = int(career_gap_str.split()[0])

    current_skills = st.text_area(
        "Current Skills (comma separated)",
        value="Python, SQL",
        placeholder="e.g. Java, HTML, React, AWS",
        height=110
    )
    
    # Predict Button
    if st.button("🚀 Get My Personalized Career Roadmap"):
        st.session_state['run_analysis'] = True

# --- RESULTS SECTION ---
if st.session_state.get('run_analysis', False):
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Result Display Card
    with st.container():
        st.markdown("### 🔍 Analysis Result")
        
        # Skill Processing
        curr_list = [s.strip().lower() for s in current_skills.split(',') if s.strip()]
        
        rcol1, rcol2 = st.columns(2)
        with rcol1:
            st.info("**Recommended Roles**\n- Data Analyst\n- Python Developer")
        with rcol2:
            st.success("**Estimated Salary (Chennai)**\n₹4.8L - ₹7.5L per annum")
            
        if gap_years > 2:
            st.warning(f"⚠️ {gap_years} Year Gap detected. We recommend focusing on 2 strong portfolio projects.")
        else:
            st.balloons()

# Footer
st.markdown('<p class="footer-text">Made with ❤️ for Chennai Job Seekers | Updated for 2026 Market</p>', unsafe_allow_html=True)
