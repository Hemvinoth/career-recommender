import streamlit as st

st.set_page_config(
    page_title="Chennai Career Recommender",
    page_icon="🎯",
    layout="centered"
)

# --- DRIBBBLE-STYLE CLEAN & COLORFUL CSS ---
st.markdown("""
<style>
    /* 1. Light Professional Background */
    .stApp {
        background-color: #F8FAFC;
    }

    /* 2. Main Title (Dark & Professional) */
    .main-title {
        font-size: 3rem !important;
        font-weight: 800 !important;
        text-align: center;
        color: #1e293b !important;
        margin-top: 2rem;
        margin-bottom: 0.5rem;
    }

    /* 3. The Professional White Card (Fixes the "Empty Box" issue) */
    [data-testid="stVerticalBlock"] > div:has(div.stSelectbox) {
        background-color: white !important;
        padding: 45px !important;
        border-radius: 28px !important;
        box-shadow: 0 10px 25px rgba(0,0,0,0.04) !important;
        border: 1px solid #e2e8f0;
        margin-top: 10px;
    }

    /* 4. Subtitle Inside the White Card */
    .card-subtitle {
        color: #64748b !important;
        font-size: 1.1rem !important;
        text-align: center;
        margin-bottom: 2rem !important;
        background: #f1f5f9;
        padding: 12px;
        border-radius: 12px;
        font-weight: 500;
    }

    /* 5. Input Labels (Clean Dark Grey) */
    label, p, h3 {
        color: #334155 !important;
        font-weight: 600 !important;
    }

    /* 6. Vibrant Action Button (Dribbble Orange Gradient) */
    .stButton>button {
        background: linear-gradient(135deg, #FF4B2B 0%, #FF416C 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 14px !important;
        height: 3.8rem !important;
        font-weight: 700 !important;
        font-size: 1.2rem !important;
        width: 100%;
        margin-top: 15px;
        box-shadow: 0 8px 20px rgba(255, 75, 43, 0.25) !important;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 25px rgba(255, 75, 43, 0.35) !important;
    }

    /* 7. Results Dashboard Styling */
    .result-card {
        background: white;
        border-radius: 20px;
        padding: 25px;
        border: 1px solid #e2e8f0;
        margin-top: 20px;
    }
    .accent-text {
        color: #FF416C;
        font-weight: 800;
        font-size: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# --- APP LAYOUT ---

# Header (Outside the card)
st.markdown('<h1 class="main-title">🎯 Chennai Career Recommender</h1>', unsafe_allow_html=True)

# Main Input Card Container
with st.container():
    # Subtitle is now INSIDE the white box, perfectly visible
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
    predict = st.button("🚀 Get My Personalized Career Roadmap")

# --- RESULTS SECTION ---
if predict:
    st.markdown("---")
    st.markdown("### 🔍 Your Personalized Roadmap")
    
    # Dashboard-style results
    rcol1, rcol2 = st.columns(2)
    
    with rcol1:
        st.markdown(f"""
            <div class="result-card">
                <p style="color: #64748b; margin-bottom: 5px;">💼 TARGET ROLES</p>
                <div class="accent-text">Python Developer / Data Scientist</div>
            </div>
        """, unsafe_allow_html=True)

    with rcol2:
        st.markdown(f"""
            <div class="result-card">
                <p style="color: #64748b; margin-bottom: 5px;">💰 EST. SALARY (2026)</p>
                <div class="accent-text" style="color: #10b981;">₹4.8L - ₹7.5L</div>
            </div>
        """, unsafe_allow_html=True)

    # Manageability warning for gaps
    if gap_years >= 1:
        st.warning(f"💡 {gap_years} Year Career Gap: Focus on building a strong GitHub portfolio with 2 fresh projects.")
    else:
        st.balloons()
        st.success("🌟 Fresh Profile! High chances in Chennai walk-ins.")

# Footer
st.markdown("<br><p style='text-align:center; color:#94a3b8; font-size:0.9rem;'>Made with ❤️ for Chennai Job Seekers | Updated for 2026 Market</p>", unsafe_allow_html=True)
