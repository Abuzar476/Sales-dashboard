import pandas as pd
def analyze(df, revenue_col=None, category_col=None, date_col=None, payment_col=None):
    total_revenue = df[revenue_col].sum() if revenue_col else None
    total_orders = len(df)
    sales_by_category = df.groupby(category_col)[revenue_col].sum() if category_col and revenue_col else\
                        df[category_col].value_counts() if category_col else None
    sales_by_month = df.groupby(date_col)[revenue_col].sum() if date_col and revenue_col else\
                     df[date_col].value_counts() if date_col else None
    sales_by_payment = df.groupby(payment_col)[revenue_col].sum() if payment_col and revenue_col else\
                       df[payment_col].value_counts() if payment_col else None 
    return total_revenue, total_orders, sales_by_category, sales_by_month, sales_by_payment
def cross_analyze(df,col1,col2):
    return df.groupby([col1,col2]).size().unstack(fill_value=0)
