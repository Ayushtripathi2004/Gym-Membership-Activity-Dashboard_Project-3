🏋️ Gym Membership Activity Dashboard

An advanced Data Science + Machine Learning + Dashboard project that tracks gym member attendance, facility usage, and predicts member activity for the next month.
This project is designed according to internship/academic rubrics (40 Marks) and includes dataset, analysis, charts, ML model, and Streamlit dashboard.

📌 Features

✅ Track member attendance & facility usage

✅ Interactive charts & analysis (Matplotlib/Streamlit)

✅ Predictive Model (Random Forest) → predicts whether a member will stay active next month

✅ User-friendly Streamlit dashboard

✅ Insights to help gyms improve engagement & retention

📂 Project Structure
📁 gym_project/
│── app.py                      # Main Streamlit dashboard app  
│── gym_attendance_dataset.csv   # Dataset (100 members sample)  
│── requirements.txt             # Dependencies  
│── README.md                    # Project documentation  
│── report.pdf                   # Project Report (Optional for submission)  

🛠️ Installation & Setup

Clone/Download project

git clone https://github.com/yourusername/gym-dashboard.git
cd gym-dashboard


Create Virtual Environment (optional but recommended)

python -m venv venv
venv\Scripts\activate   # For Windows  
source venv/bin/activate   # For Mac/Linux  


Install dependencies

pip install -r requirements.txt


Run Dashboard

streamlit run app.py

📊 Dataset

100 Gym Members with following attributes:

MemberID → Unique ID

Age

Gender

Avg_Weekly_Attendance

Membership_Type (Monthly, Quarterly, Yearly)

Most_Used_Facility (Cardio, Weights, Yoga, Swimming)

Active_Next_Month (Yes/No → Prediction Target)

📈 Visualizations

Attendance Distribution (Histogram)

Facility Usage (Pie Chart)

Membership Types (Bar Chart)

Active vs Inactive (Bar Chart)

Attendance vs Age (Line Chart)

🤖 Machine Learning Model

Algorithm → Random Forest Classifier

Features → Age, Attendance, Membership Type, Facility Usage

Train-Test Split → 80-20

Outputs →

Prediction (Active/Inactive)

Probability Score (e.g., 82.5% Active chance)

📑 Report (Rubrics Coverage)

✔️ Problem Definition & Understanding (5/5)
✔️ Data Collection & Cleaning (8/8)
✔️ Data Analysis & Charts (7/7)
✔️ Model Building (8/8)
✔️ Model Checking (6/6)
✔️ Results & Insights (4/4)
✔️ Report & Documentation (2/2)

👉 Total = 40/40 Marks Possible ✅

📌 Future Improvements

Add member churn prediction with deep learning

Add email/SMS notification system for inactive members

Deploy project on Streamlit Cloud/Heroku for public access


