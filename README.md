# FitSync AI - Gamified Fitness Web App

## 📌 Overview
FitSync AI is an **AI-powered gamified fitness web app** inspired by **Duolingo**, designed to make workouts engaging and interactive. It provides **AI-generated exercise suggestions, animated exercise demonstrations, personalized meal plans, and a fitness league with XP levels** to track progress.

## 🚀 Features
- ✅ **AI-Powered Daily Exercise Suggestions**
- ✅ **Smart Timer** with beep alerts
- ✅ **Fitness League & Leaderboard** to track progress
- ✅ **Animated Exercise Demonstrations** using **Lottie.js**
- ✅ **AI-Generated Meal Plans** displayed dynamically
- ✅ **FitBot** - your fitness chatbot
- ✅ **Firebase Integration** for real-time database functionality

## 📸 Screenshots & Videos
### **Homepage**

https://github.com/user-attachments/assets/bbbac712-f65c-4ba6-989e-acc53ed72724

### **Nutrition Section**

https://github.com/user-attachments/assets/0cd12834-d909-46c9-a72a-07b8ed2d851d

### **Training Section**

https://github.com/user-attachments/assets/80e45eeb-b58a-4063-b5db-360804b27515

### **FitBot**
![image](https://github.com/user-attachments/assets/d0669dbe-7cc7-4352-b70d-cfa97ca10aae)

## 🛠️ Tech Stack
**Frontend:**
- ✅ Streamlit – For the web-based UI and interactive elements
- ✅ OpenCV – For capturing and processing video frames
- ✅ Plotly – For data visualization and analytics

**Backend & Computation:**
- ✅ Python – Core programming language
- ✅ NumPy – For numerical calculations and interpolations
- ✅ Math Library – For angle calculations using atan2 and degrees

**Computer Vision & AI:**
- ✅ PoseDetector (likely using Mediapipe or OpenCV) – For pose estimation and detecting key body points

**Hardware & Integrations:**
- ✅ Webcam (via OpenCV) – Capturing real-time exercise data

## 🔧 Setup & Installation

### 📌 Prerequisites
Ensure you have the following installed:
- 🐍 Python 3.8+
- 📦 pip (Python package manager)
- 💻 Git (optional, for cloning)
- 📂 Virtual Environment (recommended)

### 🚀 Installation Steps

1️⃣ **Clone the Repository (if using Git)**
```bash
git clone https://github.com/your-username/FitnessTrainer.git
cd FitnessTrainer
```

2️⃣ **Create & Activate a Virtual Environment**
```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
```

3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

4️⃣ **Set Up Secrets (if applicable)**
Add API keys or credentials in `secrets.toml` (if needed).

5️⃣ **Run the Application**
```bash
python styles/1_🏠_HomePage.py
```

### 🎯 Using the Features
```bash
# Tutorials
python pages/2_📘_Tutorials.py

# Train Mode
python pages/3_🏃_Train.py

# Chatbot
python pages/4_🤖_Chatbot.py

# Nutrition Guide
python pages/5_🍎_Nutrition.py
```

### 🎯 Additional Notes
To deactivate the virtual environment, run:
```bash
deactivate
```
If you face missing dependencies, manually install them:
```bash
pip install some_package_name
```

## 🚀 Deployment
### **GitHub Pages**
1. Push your code to GitHub.
2. Go to **Settings → Pages**
3. Set the branch to `main` and save.

## 📬 Contact
For queries or contributions, reach out to **Pallavi Gudupalli** at [your-email@example.com](mailto:your-email@example.com).
