from dotenv import load_dotenv
import os
import google.generativeai as genai
from Ir import get_recommendations, get_weather

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def gemini_agent(user_name, budget, interests, start_date, end_date):
    """
    Uses Gemini AI to generate a personalized travel summary.
    Also calls your IR model to get recommendations with live weather.
    """
    # --- Step 1: Create a travel assistant prompt ---
    prompt = f"""
    You are a smart travel planning assistant.
    User: {user_name}
    Budget: ₹{budget}
    Interests: {interests}
    Travel Dates: {start_date} to {end_date}

    Based on this, suggest suitable destinations in India.
    Give a short summary plan (2–3 sentences) highlighting:
    - Why these places are ideal for this user's interests
    - How to make the most of their trip
    """

    # --- Step 2: Generate AI plan using Gemini ---
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    ai_plan = response.text

    # --- Step 3: Get IR model-based destinations ---
    df = get_recommendations(budget, interests, start_date, end_date)

    if not df.empty:
        df["Weather"] = df["Destination"].apply(get_weather)

    return ai_plan, df
