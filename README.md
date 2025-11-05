 🧭 Smart Trip Planner

**Smart Trip Planner** is an AI-powered travel assistant that helps users plan customized trips based on their preferences, such as destination, budget, duration, and interests. It leverages intelligent route planning, weather insights, and attraction suggestions to create the perfect travel itinerary — all in one place.

---

## 🚀 Features

* 🗺️ **Personalized Trip Planning** — Get tailored itineraries based on your travel goals, interests, and available time.
* 🤖 **AI Travel Assistant** — The `ai_agent.py` module uses AI to generate smart recommendations.
* 🌦️ **Weather-Aware Planning** — Suggests destinations or modifies plans based on weather conditions.
* 💰 **Budget Optimization** — Suggests affordable travel options based on your budget range.
* 🏨 **Attraction & Stay Recommendations** — Suggests popular spots, restaurants, and stays using integrated APIs.
* 🧠 **User-Friendly Interface** — Simple Flask-based backend (`app.py`) for API and UI integration.

---

## 🏗️ Project Structure

```
smart-trip-planner/
│
├── __pycache__/              # Compiled cache files
├── .env                      # Environment variables (API keys, config)
├── Ir.py                     # Itinerary recommendation logic
├── ai_agent.py               # AI-powered trip planning agent
├── app.py                    # Flask application entry point
└── README.md                 # Project documentation
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/anaya0103/smart-trip-planner.git
cd smart-trip-planner
```

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate       # On macOS/Linux
venv\Scripts\activate          # On Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add your environment variables

Create a `.env` file in the root directory and include your API keys, e.g.:

```
OPENAI_API_KEY=your_openai_api_key
GOOGLE_MAPS_API_KEY=your_google_maps_key
```

### 5️⃣ Run the app

```bash
python app.py
```

Then open your browser and visit:
👉 `http://127.0.0.1:5000/`

---

## 🧩 Tech Stack

* **Backend:** Python (Flask / FastAPI)
* **AI Agent:** OpenAI / Gemini API
* **APIs Used:** Google Maps API, Weather API (optional)
* **Environment:** Python 3.9+
* **Database (optional):** SQLite / MongoDB

---

## 💡 Future Enhancements

* 📍 Add map visualization and live route optimization
* 📅 Enable saving and sharing of itineraries
* 🌐 Multi-language support for travelers
* 🧳 Integrate booking APIs for hotels and flights

---

## 🤝 Contributing

Contributions are always welcome!
If you'd like to add new features or fix bugs:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

## 📄 License

This project is open-source under the **MIT License**.



## 👩‍💻 Author

**Sunidhi**
🌍 GitHub: [@anaya0103](https://github.com/anaya0103)


