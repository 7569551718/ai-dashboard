import streamlit as st
import pandas as pd
import plotly.express as px

st.title("AI Dashboard Generator")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df)

    st.subheader("Generate Chart")

    x_axis = st.selectbox(
        "Select X Axis",
        df.columns
    )

    y_axis = st.selectbox(
        "Select Y Axis",
        df.columns
    )

    chart_type = st.selectbox(
        "Chart Type",
        ["Bar", "Line", "Pie"]
    )

    if chart_type == "Bar":
        fig = px.bar(df, x=x_axis, y=y_axis)

    elif chart_type == "Line":
        fig = px.line(df, x=x_axis, y=y_axis)

    else:
        fig = px.pie(df, names=x_axis, values=y_axis)

    st.plotly_chart(fig)