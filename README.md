# Winelibrary - A Taste-Driven Wine Search Engine for Connoisseurs

## 📝 Overview

**WineLibrary** is a personalized wine search engine designed to help users find the perfect bottle tailored to their unique taste preferences. 
Instead of browsing endless wine lists, users can simply describe what they’re craving — like *“fruity and bold with a hint of spice”* — and WineLibrary will return curated recommendations that match their palate.

Built with Python, Django, and Scikit-learn, this project uses natural language processing to interpret flavor descriptions and match them with the right wines. It's a solo project aimed at making wine discovery intuitive, fun, and taste-driven.


Table of Contents
- [Overview](#overview)
- Getting Started
- [Tech Stack](#tech-stack)
- [Usage](#usage)
- [How it Works](#how-it-works)
- [Demo](#demo)
- [Challenges](#challenges)
- [License](#license)


## 🛠️ Tech Stack

**Backend:**
- **Python** – Core language for backend logic
- **Django** – Web framework for rapid development and clean architecture
- **Scikit-learn** – Used for vectorization and similarity-based wine recommendation
- **NLTK** – For natural language processing and text preprocessing

**Frontend:**
- **HTML/CSS** – Page structure and styling
- **Bootstrap** – Responsive UI and quick design components

**Performance:**
- **Caching (Joblib)** – Speeds up repeated wine searches

**Database:**
- **SQLite** – Lightweight database used for development

**Other Tools:**
- **Git** – Version control
- **Virtualenv** – Isolated Python environment





## 🧑‍🍷 Usage

Once the server is running, you can start exploring WineLibrary via your browser.

### 🔍 Search for Wines
1. Navigate to the homepage.
2. Enter a taste description (e.g., *“crisp and floral with citrus notes”*).
3. Submit your query to receive wine recommendations tailored to your palate.

### 💡 How It Works
- The app uses **NLP techniques** to analyze your input and match it with wine flavor profiles.
- Recommendations are generated using a **vector similarity model** built with Scikit-learn.
- **Caching** is used to speed up repeat searches.

**WineLibrary** is all about simplifying the wine discovery process — just type what you're in the mood for, and let the engine do the rest!
