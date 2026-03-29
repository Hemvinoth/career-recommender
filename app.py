import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Chennai Career Recommender",
    page_icon="🎯",
    layout="centered"
)

# 2. Vibrant & Colorful Professional CSS
st.markdown("""
<style>
    /* Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }

    /* Professional White Card */
    [data-testid="stVerticalBlock"] > div:has(div.stSelectbox) {
        background-color: white !important;
        padding: 40px !important;
        border-radius: 30px !important;
        box-shadow: 0 20px 50px rgba(0,0,0,0.2) !important;
    }

    /* Text Visibility and Styling */
    label, p, h3 {
        color: #2d3748 !important;
        font-weight: 700 !important;
    }

    /* Subtitle inside the card */
    .card-subtitle {
        color: #4a5568 !important;
        text-align: center;
        background: #f7fafc;
        padding: 12px;
        border-radius: 15px;
        margin-bottom: 25px !important;
        font-weight: 500;
        border: 1px solid #edf2f7;
    }

    /* Gradient Action Button (Orange-Pink) */
    .stButton>button {
        background: linear-gradient(90deg, #f093fb 0%, #f5576c 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 15px !important;
        height: 3.8rem !important;
        font-weight: bold !important;
        font-size: 1.2rem !important;
        width: 100%;
        margin-top: 10px;
        box-shadow: 0 10px 25px rgba(245, 87, 108, 0.4) !important;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 30px rgba(245, 87, 108, 0.5) !important;
    }

    /* Results Styling */
    .res-card {
        background: white;
        border-radius: 20px;
        padding: 20px;
        border-left: 6px solid #f5576c;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# 3. App Header (Outside Card)
st.markdown("<h1 style='text-align:center; color:white; font-size:3rem; margin-bottom:0;'>🎯 Chennai Career Guide</h1>", unsafe_allow_html=True)

# 4. Main Application Card
with st.container():
    # Subtitle shifted inside the white box
    st.markdown('<p class="card-subtitle">Real-Time Personalized Roadmap for Chennai IT Job Market (2026)</p>', unsafe_allow_html=True)
    
    st.subheader("👤 Your Profile Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        qual_options = ['B.Tech / BE', 'B.Sc CS/IT', 'BCA', 'M.Sc / MCA', 'Diploma', 'Other']
        qualification = st.selectbox("Highest Qualification", qual_options)
        
        # --- THE FIX: Conditional Input for "Other" ---
        user_degree = ""
        if qualification == "Other":
            user_degree = st.text_input("🎓 Type your specific degree here", placeholder="e.g., B.Com, MBA, B.E ECE")
        else:
            user_degree = qualification

    with col2:
        gap_options = [f"{i} Year{'s' if i > 1 else ''}" for i in range(0, 11)]
        career_gap = st.selectbox("Career Gap", gap_options)

    skills = st.text_area("Current Skills (comma separated)", placeholder="e.g. PowerBI, Python, SQL, Excel", height=100)
    
    # Analyze Button
    if st.button("🚀 Generate My Professional Roadmap"):
        st.session_state['processed'] = True
        st.session_state['final_degree'] = user_degree

# 5. Results Section
if st.session_state.get('processed', False):
    st.markdown("---")
    
    # Colorful Result Display
    rcol1, rcol2 = st.columns(2)
    
    with rcol1:
        st.markdown(f"""
            <div class="res-card">
                <p style="color: #f5576c; margin-bottom: 5px;">💼 TARGET ROLES FOR {st.session_state['final_degree'].upper()}</p>
                <h3 style="margin-top: 0;">Data Analyst / BI Specialist</h3>
            </div>
        """, unsafe_allow_html=True)
        
    with rcol2:
        st.markdown("""
            <div class="res-card" style="border-left-color: #667eea;">
                <p style="color: #667eea; margin-bottom: 5px;">💰 EST. SALARY (CHENNAI 2026)</p>
                <h3 style="margin-top: 0;">₹4.2L - ₹7.8L per annum</h3>
            </div>
        """, unsafe_allow_html=True)

    st.balloons()

# Footer
st.markdown("<br><p style='text-align:center; color:#e2e8f0; font-size:0.9rem;'>Updated for 2026 Market | Professional Web Dashboard</p>", unsafe_allow_html=True)
