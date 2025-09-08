import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# -------------------------------
# Load dataset
# -------------------------------
df = pd.read_csv("gym_attendance_dataset_100.csv")

st.set_page_config(page_title="Gym Dashboard", layout="wide")
st.title("🏋️‍♂️ Gym Membership Activity Dashboard")

# -------------------------------
# Sidebar Filters
# -------------------------------
st.sidebar.header("🔍 Filters")
selected_membership = st.sidebar.multiselect(
    "Membership Type", 
    df["Membership_Type"].unique(), 
    df["Membership_Type"].unique()
)
selected_facility = st.sidebar.multiselect(
    "Facility", 
    df["Most_Used_Facility"].unique(), 
    df["Most_Used_Facility"].unique()
)

filtered_df = df[
    (df["Membership_Type"].isin(selected_membership)) &
    (df["Most_Used_Facility"].isin(selected_facility))
]

# -------------------------------
# Top Metrics
# -------------------------------
col1, col2, col3 = st.columns(3)
col1.metric("👥 Total Members", len(filtered_df))
col2.metric("✅ Active", filtered_df['Active_Next_Month'].value_counts().get("Yes", 0))
col3.metric("❌ Inactive", filtered_df['Active_Next_Month'].value_counts().get("No", 0))

# -------------------------------
# Charts - Row 1
# -------------------------------
st.markdown("### 📊 Quick Insights")
col1, col2, col3 = st.columns(3)

with col1:
    fig, ax = plt.subplots(figsize=(3,2))
    ax.hist(filtered_df['Avg_Weekly_Attendance'], bins=7, color="skyblue", edgecolor="black")
    ax.set_title("Attendance Dist.", fontsize=9)
    st.pyplot(fig)

with col2:
    fig2, ax2 = plt.subplots(figsize=(3,2))
    facility_counts = filtered_df['Most_Used_Facility'].value_counts()
    ax2.pie(facility_counts, labels=facility_counts.index, autopct='%1.0f%%', textprops={'fontsize':7})
    ax2.set_title("Facility Usage", fontsize=9)
    st.pyplot(fig2)

with col3:
    fig3, ax3 = plt.subplots(figsize=(3,2))
    membership_counts = filtered_df['Membership_Type'].value_counts()
    ax3.bar(membership_counts.index, membership_counts.values, color="orange")
    ax3.set_title("Membership Types", fontsize=9)
    st.pyplot(fig3)

# -------------------------------
# Charts - Row 2
# -------------------------------
col4, col5, col6 = st.columns(3)

with col4:
    fig4, ax4 = plt.subplots(figsize=(3,2))
    active_counts = filtered_df['Active_Next_Month'].value_counts()
    ax4.bar(active_counts.index, active_counts.values, color=['green', 'red'])
    ax4.set_title("Active vs Inactive", fontsize=9)
    st.pyplot(fig4)

with col5:
    fig5, ax5 = plt.subplots(figsize=(3,2))
    ax5.plot(filtered_df.groupby("Age")["Avg_Weekly_Attendance"].mean(), marker="o", color="blue", linewidth=1)
    ax5.set_title("Attendance by Age", fontsize=9)
    st.pyplot(fig5)

with col6:
    st.dataframe(filtered_df.head(5), height=140)

# -------------------------------
# Prediction Model
# -------------------------------
st.markdown("### 🤖 Predict Member Activity")

# Encode dataset
df_encoded = pd.get_dummies(df.drop(columns=['Member_ID']), drop_first=True)
X = df_encoded.drop(columns=['Active_Next_Month_Yes'])
y = df_encoded['Active_Next_Month_Yes']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier().fit(X_train, y_train)

# Input UI
age = st.slider("Age", 15, 65, 25)
attendance = st.slider("Avg Weekly Attendance", 0, 7, 3)
membership = st.selectbox("Membership Type", df['Membership_Type'].unique())
facility = st.selectbox("Most Used Facility", df['Most_Used_Facility'].unique())

# Prepare input
input_df = pd.DataFrame({
    "Age": [age],
    "Avg_Weekly_Attendance": [attendance],
    "Membership_Type": [membership],
    "Most_Used_Facility": [facility]
})
input_encoded = pd.get_dummies(input_df, drop_first=True)
input_encoded = input_encoded.reindex(columns=X.columns, fill_value=0)

# Predict
pred = model.predict(input_encoded)[0]
proba = model.predict_proba(input_encoded)[0]  # [inactive%, active%]

if pred == 1:
    st.success(f"✅ Likely ACTIVE next month! ({proba[1]*100:.1f}% confidence)")
else:
    st.error(f"❌ Likely INACTIVE next month. ({proba[0]*100:.1f}% confidence)")
