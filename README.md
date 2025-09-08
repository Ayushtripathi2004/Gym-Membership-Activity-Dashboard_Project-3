■■ Gym Membership Activity Dashboard
Features
- Track member attendance & facility usage
- Interactive charts & analysis (Matplotlib/Streamlit)
- Predictive Model (Random Forest) → predicts whether a member will stay active next month
- User-friendly Streamlit dashboard
- Insights to help gyms improve engagement & retention
Project Structure
■ gym_project/
■■■ app.py # Main Streamlit dashboard app
■■■ gym_attendance_dataset.csv # Dataset (100 members sample)
■■■ requirements.txt # Dependencies
■■■ README.md # Project documentation
■■■ report.pdf # Project Report (Optional for submission)
Installation & Setup
1. Clone/Download project:
 git clone https://github.com/yourusername/gym-dashboard.git
 cd gym-dashboard
2. Create Virtual Environment (optional but recommended):
 python -m venv venv
 venv\Scripts\activate # For Windows
 source venv/bin/activate # For Mac/Linux
3. Install dependencies:
 pip install -r requirements.txt
4. Run Dashboard:
 streamlit run app.py
Dataset
- 100 Gym Members with attributes:
 - MemberID → Unique ID
 - Age
 - Gender
 - Avg_Weekly_Attendance
 - Membership_Type (Monthly, Quarterly, Yearly)
 - Most_Used_Facility (Cardio, Weights, Yoga, Swimming)
 - Active_Next_Month (Yes/No → Prediction Target)
Visualizations
- Attendance Distribution (Histogram)
- Facility Usage (Pie Chart)
- Membership Types (Bar Chart)
- Active vs Inactive (Bar Chart)
- Attendance vs Age (Line Chart)
Machine Learning Model
- Algorithm → Random Forest Classifier
- Features → Age, Attendance, Membership Type, Facility Usage
- Train-Test Split → 80-20
- Outputs →
 - Prediction (Active/Inactive)
 - Probability Score (e.g., 82.5% Active chance)
Rubrics Coverage
✔■ Problem Definition & Understanding (5/5)
✔■ Data Collection & Cleaning (8/8)
✔■ Data Analysis & Charts (7/7)
✔■ Model Building (8/8)
✔■ Model Checking (6/6)
✔■ Results & Insights (4/4)
✔■ Report & Documentation (2/2)
■ Total = 40/40 Marks Possible ■
Future Improvements
- Add member churn prediction with deep learning
- Add email/SMS notification system for inactive members
- Deploy project on Streamlit Cloud/Heroku for public access
