import streamlit as st
import pandas as pd
from datetime import date
from ai_agent import gemini_agent
from Ir import get_recommendations  # Import your IR model function

# ----------------- PAGE SETUP -----------------
st.set_page_config(page_title="Smart Trip Planner", page_icon="🌍", layout="wide")

# ----------------- STYLING -----------------
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
[data-testid="stHeader"] {
    background: rgba(0, 0, 0, 0);
}
[data-testid="stSidebar"] {
    background-color: rgba(0,0,0,0.5);
    color: white;
}
h1, h2, h3, h4, h5, h6, p, div {
    color: white !important;
}
.card {
    background-color: rgba(255,255,255,0.15);
    border-radius: 15px;
    padding: 20px;
    margin: 10px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    transition: 0.3s;
}
.card:hover {
    transform: scale(1.02);
    box-shadow: 0 6px 12px rgba(0,0,0,0.3);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ----------------- HEADER -----------------
st.title("🌍 Smart Trip Planner")
st.markdown("Plan your next adventure based on your **budget**, **dates**, and **availability**!")

# ----------------- SIDEBAR -----------------
st.sidebar.header("🧭 Trip Preferences")

user_name = st.sidebar.text_input("Your Name", placeholder="Enter your name")
budget = st.sidebar.number_input("Total Budget (₹)", min_value=1000, max_value=1000000, step=500)
start_date = st.sidebar.date_input("Start Date", min_value=date.today())
end_date = st.sidebar.date_input("End Date", min_value=start_date)
people = st.sidebar.slider("Number of Travelers", 1, 10, 1)
interest = st.sidebar.multiselect(
    "Select Your Interests",
    ["Beaches", "Mountains", "Adventure", "Culture", "Wildlife", "Shopping", "Food"],
)

# ----------------- FIND TRIP BUTTON -----------------
if st.sidebar.button("Find My Trip"):
    st.session_state['search_triggered'] = True

# ----------------- MAIN CONTENT -----------------
if 'search_triggered' in st.session_state and st.session_state['search_triggered']:
    st.subheader(f"✨ Personalized Trip Plan for {user_name if user_name else 'You'}")

    try:
        # --- Gemini Agent gives personalized plan + IR recommendations ---
        ai_summary, filtered_df = gemini_agent(user_name, budget, interest, start_date, end_date)

        # --- Display AI summary ---
        st.markdown("#### 💡 Smart AI Travel Summary")
        st.info(ai_summary)

        # --- Display IR recommendations ---
        if not filtered_df.empty:
            st.success("Here are some destinations matching your preferences 👇")

            cols = st.columns(3)
            for idx, row in filtered_df.iterrows():
                with cols[idx % 3]:
                    st.markdown(
                        f"""
                        <div class="card">
                            <h3>{row['Destination']}</h3>
                            <p>🕒 Best Time: {row['Best Time']}</p>
                            <p>💰 Cost: ₹{row['Cost']}</p>
                            <p>🏖 Category: {row['Category']}</p>
                            <p>🌤 Weather: {row['Weather']}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
        else:
            st.warning("No destinations found matching your preferences.")
    except Exception as e:
        st.error(f"⚠️ Error: {e}")
