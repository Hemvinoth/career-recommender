import streamlit as st

st.set_page_config(
    page_title="Chennai Career Recommender",
    page_icon="🎯",
    layout="centered"
)

# --- IMPROVED CSS ---
st.markdown("""
<style>
    /* 1. Fix Background and Text Visibility */
    .stApp {
        background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
    }
    
    /* Force all standard labels to be white so they are visible */
    label, .stMarkdown, p, h1, h2, h3, h4, .stSelectbox p {
        color: white !important;
    }

    /* 2. Style the Input Card properly */
    .main-card {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        margin-bottom: 20px;
    }
    
    /* Fix labels inside the white card to be dark again */
    .main-card label, .main-card p, .main-card h3 {
        color: #1e2937 !important;
    }

    /* 3. Button Styling */
    .stButton>button {
        background: linear-gradient(90deg, #f59e0b, #ea580c) !important;
        color: white !important;
        border: none !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
        border-radius: 50px !important;
        padding: 10px 20px !important;
        width: 100%;
        transition: transform 0.2s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1 style='text-align: center; color: white;'>🎯 Chennai Career Recommender</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #dbeafe; font-size: 1.2rem;'>Real-Time Personalized Roadmap for Chennai IT Job Market (2026)</p>", unsafe_allow_html=True)

# --- INPUT SECTION ---
# To fix the "empty box", we wrap everything in a single 'with' block 
# and use a container for the custom styling.
with st.container():
    # This creates the white background 'card' effect safely
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
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
        height=100
    )
    
    # Logic for Button
    submit = st.button("🚀 Get My Personalized Career Roadmap")
    st.markdown('</div>', unsafe_allow_html=True)

# --- RESULTS SECTION ---
if submit:
    curr_list = [s.strip().lower() for s in current_skills.split(',') if s.strip()]
    
    # Professional Result Container
    with st.container():
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.header("🔍 Your Personalized Roadmap")
        
        # ... (Your Logic for Salary and Roles remains the same here) ...
        # (Example: Just showing the result)
        st.success(f"Targeting Roles in Chennai for: {', '.join(curr_list).title()}")
        
        st.metric("Realistic Annual Package (2026)", "₹4.5L - ₹7.8L")
        
        st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><p style='text-align:center; color:#dbeafe;'>Made with ❤️ for Chennai Job Seekers | 2026 Edition</p>", unsafe_allow_html=True)
