import streamlit as st
import pandas as pd
import numpy as np

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="HERO Learning App", layout="wide")

# =========================
# CUSTOM CSS (Colorful Pastel Theme)
# =========================
st.markdown("""
<style>
body {
    background-color: #E0F7FA;  /* soft blue */
}
.main {
    background-color: #E0F7FA;
}
.card {
    padding: 15px;
    border-radius: 15px;
    color: black;
    text-align: center;
    font-weight: bold;
}
.video-box {
    background-color: #0277BD;  /* darker blue for videos */
    height: 120px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 10px;
    color: white;
    font-size: 30px;
}
.stSidebar {
    background-color: #B3E5FC;  /* soft blue */
}
.stButton>button {
    background-color: #B3E5FC;
    color: black;
    border-radius: 10px;
}
.horizontal-scroll {
    display: flex;
    overflow-x: auto;
    gap: 15px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
st.sidebar.image("logo.png", width=150)  # logo di sidebar
st.sidebar.title("HERO'S 🚀")
st.sidebar.write("🔔 ⚙️")  # notification and settings icons
page = st.sidebar.radio("Menu", ["Home", "Video Learning", "Virtual Lab", "Score Page"])

# =========================
# USER HEADER
# =========================
def user_header():
    col1, col2 = st.columns([1, 5])
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/149/149071.png", width=80)
    with col2:
        st.write("**Kurni Ramadhani | Grade 10 High School**")

# =========================
# HOME PAGE
# =========================
if page == "Home":
    st.container()
    user_header()
    st.title("Welcome to HERO'S 🧠")
    st.subheader("Recommended Learning Videos for You")

    subjects = {
        "Physics": "#81D4FA",
        "Chemistry": "#A5D6A7",
        "Biology": "#F48FB1",
        "Math": "#FFF176"
    }

    for subject, bg_color in subjects.items():
    st.markdown(f"<h3 style='background-color:{bg_color};padding:5px;border-radius:10px'>{subject} (High School)</h3>", unsafe_allow_html=True)
    videos = [f"{subject} Topic {i+1}" for i in range(16)]  # 16 videos per subject
    cols = st.columns(4)
    for i, video_name in enumerate(videos):
        col_index = i % 4
        with cols[col_index]:
            st.markdown(f"""
            <div class='card' style='background-color:{bg_color}'>
                <div class='video-box'>▶</div>
                {video_name}
            </div>
            """, unsafe_allow_html=True)  # <-- tambahkan kurung tutup di sini

# =========================
# VIDEO LEARNING
# =========================
elif page == "Video Learning":
    user_header()
    st.title("📚 Physics Learning Journey")
    st.write("Learning is a process, not an instant result. Keep progressing and understand each concept ✨")

    physics_videos = [
        "Kinematics Part 1", "Kinematics Part 2", "Kinematics Part 3", "Kinematics Part 4"
    ]

    for idx, video in enumerate(physics_videos):
        if idx == 0:
            st.subheader(f"🎬 {video} (Unlocked)")
            st.video("https://www.youtube.com/watch?v=3o8v6c6l3X8")
        else:
            st.subheader(f"🔒 {video}")
            st.info("Complete the previous video to unlock this one")

# =========================
# VIRTUAL LAB
# =========================
elif page == "Virtual Lab":
    user_header()
    st.title("🔬 Virtual Laboratory")

    subject = st.selectbox("Choose Subject", ["Physics", "Chemistry", "Biology", "Math"])
    st.subheader(f"{subject} Simulation")

    if subject == "Physics":
        force = st.slider("Force (N)", 0, 100, 50)
        mass = st.slider("Mass (kg)", 1, 10, 5)
        st.write(f"Acceleration ≈ {force/mass:.2f} m/s²")
    elif subject == "Chemistry":
        temp = st.slider("Temperature (°C)", 0, 100, 25)
        st.write("Higher temperature → faster reaction")
    elif subject == "Biology":
        light = st.slider("Light Intensity", 0, 100, 50)
        st.write("Photosynthesis increases with light intensity")
    elif subject == "Math":
        x = st.slider("Value of x", 0, 10, 5)
        st.write(f"y = x² → {x**2}")

    st.subheader("📄 Worksheet (LKS)")
    st.text_input("1. What did you observe?")
    st.text_input("2. Explain the concept")
    st.text_area("3. Conclusion")

# =========================
# SCORE PAGE
# =========================
elif page == "Score Page":
    user_header()
    st.title("📊 Your Learning Progress")
    st.write("Every small step is a big progress 🚀")

    days = pd.date_range(start='2026-01-01', periods=90)
    scores = {
        'Math': np.random.randint(60, 100, size=90),
        'Physics': np.random.randint(55, 95, size=90),
        'Chemistry': np.random.randint(65, 100, size=90),
        'Biology': np.random.randint(60, 98, size=90)
    }

    colors = {'Math':'#FFEB3B','Physics':'#03A9F4','Chemistry':'#4CAF50','Biology':'#E91E63'}

    for subject, values in scores.items():
        st.subheader(f"{subject} Daily Progress")
        df = pd.DataFrame({'Day': days, 'Score': values})
        chart = st.line_chart(df.set_index('Day'), use_container_width=True)
        st.write(f"Average score: {np.mean(values):.2f}")
        if np.mean(values) >= 85:
            st.write("Performance: Excellent 🟢")
        elif np.mean(values) >= 70:
            st.write("Performance: Good 🟡")
        else:
            st.write("Performance: Needs Improvement 🔴")
