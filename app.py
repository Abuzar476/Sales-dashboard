import analyzer
import loader
import streamlit as st
import pandas as pd
st.title("Sales Dashboard")
upload_file = st.file_uploader("Upload sales csv", type="csv")
if upload_file is not None:
    df = pd.read_csv(upload_file, low_memory=False)
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    text_cols = df.select_dtypes(include='object').columns.tolist()
    st.subheader("Configure your dashboard")
    with st.form("config_form"):
            revenue_col = st.selectbox("Select revenue column",[None] + numeric_cols)
            category_col = st.selectbox("Select category column",[None] + text_cols)
            date_col = st.selectbox("Select date/month column",[None] + text_cols + numeric_cols)
            payment_col = st.selectbox("Select payment column", [None] + text_cols)
            currency = st.selectbox("Select currency", ["$","PKR", "€", "£", "¥"])
            submitted = st.form_submit_button("Generate Dashboard")
    if submitted:
            selected = [col for col in [revenue_col, category_col, date_col, payment_col] if col is not None]
            if len(selected) < 2:
                 st.warning("Please select at least 2 columns to generate insights")
            else:
                        
                total_revenue, total_orders, sales_by_category, sales_by_month, sales_by_payment = analyzer.analyze(df, revenue_col, category_col, date_col, payment_col)
                if total_revenue is not None and revenue_col is not None:
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Total Revenue", f"{currency}{total_revenue:,.2f}")
                    with col2:
                        st.metric("Total Orders", total_orders)
                if sales_by_category is not None and category_col is not None:
                    st.subheader("Sales/Revenue by category")
                    st.bar_chart(sales_by_category)
                if sales_by_month is not None and date_col is not None:
                    st.subheader("Monthly sales")
                    st.bar_chart(sales_by_month)
                if sales_by_payment is not None and payment_col is not None:
                    st.subheader("Payment methods")
                    st.bar_chart(sales_by_payment)
                if date_col is not None and category_col is not None:
                     st.subheader(f"{category_col} by {date_col}")
                     st.bar_chart(analyzer.cross_analyze(df,date_col,category_col))
                if date_col is not None and payment_col is not None:
                     st.subheader(f"{payment_col} by {date_col}")
                     st.bar_chart(analyzer.cross_analyze(df,date_col,payment_col))
else:
    st.warning("Upload a csv to get started")

