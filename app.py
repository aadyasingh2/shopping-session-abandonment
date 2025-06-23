import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Shopping Session Analyzer", layout="centered")
st.title("Shopping Session Abandonment Analyzer")
st.markdown("Analyze how users behave in shopping sessions and why they abandon carts.")

df=pd.read_csv("shopping_abandonment.csv")
total=df.shape[0]
abandoned=df[df['abandoned']==1].shape[0]
completed=df[df['abandoned']==0].shape[0]
rate=(completed/total)*100

st.header("📊 Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Sessions", total)
col2.metric("Abandoned", abandoned)
col3.metric("Conversion Rate", f"{rate:.2f}%")

overall_avg=df['cart_value'].mean()
abandon_only=df[df['abandoned']==1]
abandon_avg=abandon_only['cart_value'].mean()
complete_only=df[df['abandoned']==0]
complete_avg=complete_only['cart_value'].mean()


st.header("🧾 Average Cart Value & Time")

st.subheader("💠Cart Value")
col1, col2, col3 = st.columns(3) 
col1.write(f"**Cart (All):** ₹{overall_avg:.2f}")
col2.write(f"**Cart (Abandoned):** ₹{abandon_avg:.2f}")
col3.write(f"**Cart (Completed):** ₹{complete_avg:.2f}")



overall_avg_time=df['time_on_site'].mean()
abandon_only_time=df[df['abandoned']==1]
abandon_avg_time=abandon_only_time['time_on_site'].mean()
complete_only_time=df[df['abandoned']==0]
complete_avg_time=complete_only_time['time_on_site'].mean()

st.subheader("💠Time Spent")
col4, col5, col6 = st.columns(3)
col4.write(f"**Time (All):** {overall_avg_time:.2f}s")
col5.write(f"**Time (Abandoned):** {abandon_avg_time:.2f}s")
col6.write(f"**Time (Completed):** {complete_avg_time:.2f}s")


st.header("📈 Visual Insights")


import plotly.graph_objects as go

fig1 = go.Figure(data=[
    go.Pie(labels=["Completed", "Abandoned"],
           values=[completed, abandoned],
           marker_colors=["#005fb8", "#fd5d5d"])
])

st.subheader("Session Outcome Distribution")
st.plotly_chart(fig1)

import plotly.express as px
time_df = pd.DataFrame({
    "Session Type": ["Overall", "Abandoned", "Completed"],
    "Avg Time on Site": [overall_avg_time, abandon_avg_time,complete_avg_time]
})

fig2 = px.bar(time_df, x="Session Type", y="Avg Time on Site", color="Session Type",
              color_discrete_map={
                  "Overall": "#288ae6",
                  "Abandoned": "#3ca0fe",
                  "Completed": "#8ec8ff"
              })

st.subheader("Average Time on Site by Session Type")
st.plotly_chart(fig2)

cart_df = pd.DataFrame({
    "Session Type": ["Overall", "Abandoned", "Completed"],
    "Avg Cart Value": [overall_avg,abandon_avg, complete_avg]
})

fig3 = px.bar(cart_df, x="Session Type", y="Avg Cart Value", color="Session Type",
              color_discrete_map={
                  "Overall": "#d74343",
                  "Abandoned": "#f96868",
                  "Completed": "#ff9191"
              })

st.subheader("Average Cart Value by Session Type")
st.plotly_chart(fig3)

