#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""
FINTECH EXPLORATORY DATA ANALYSIS - PREMIUM PACKAGE
Client: adeyemiorogbemi
Analyst: Michael Post
Date: 5.23.2025
Scope: Analysis of expense_data.csv and invoice_data.csv for profit optimization insights

EXECUTIVE SUMMARY:
- Business is healthy and growing (+13% revenue, -9% expenses)
- Key risk: 64% revenue concentration in one customer
- Top sales rep (SL) performing exceptionally (+21% growth)
- Seasonal patterns identified in Q1 weakness
"""


# In[3]:


# =============================================================================
# SECTION 1: DATA LOADING AND INITIAL EXPLORATION
# =============================================================================


# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set up plotting
plt.style.use('default')
sns.set_palette("husl")

print("Libraries imported successfully!")


# In[5]:


# Load both datasets
expense_data = pd.read_csv('expense_data.csv')
invoice_data = pd.read_csv('invoice_data.csv')

print("Data loaded successfully!")
print(f"Expense data shape: {expense_data.shape}")
print(f"Invoice data shape: {invoice_data.shape}")


# In[6]:


print("=== EXPENSE DATA OVERVIEW ===")
print(f"Shape: {expense_data.shape}")
print(f"Columns: {list(expense_data.columns)}")
print("\nData types:")
print(expense_data.dtypes)
print("\n" + "="*50)

print("\n=== INVOICE DATA OVERVIEW ===")
print(f"Shape: {invoice_data.shape}")
print(f"Columns: {list(invoice_data.columns)}")
print("\nData types:")
print(invoice_data.dtypes)


# In[8]:


print("=== EXPENSE DATA - First 5 rows ===")
print(expense_data.head())
print("\n=== INVOICE DATA - First 5 rows ===")
print(invoice_data.head())


# In[9]:


print("=== EXPENSE DATA - Basic Statistics ===")
print(expense_data.describe())
print("\n=== INVOICE DATA - Basic Statistics ===")
print(invoice_data.describe())


# In[10]:


# =============================================================================
# SECTION 2: EXTREME VALUES ANALYSIS - PROFIT DRIVERS & KILLERS
# =============================================================================


# In[11]:


print("=== EXTREME VALUES ANALYSIS ===")
print("\n--- TOP 10 LARGEST EXPENSES ---")
print(expense_data.nlargest(10, 'Amount')[['Date', 'Amount', 'description', 'Category', 'Vendor']])

print("\n--- TOP 10 LARGEST REFUNDS/CREDITS ---")
print(expense_data.nsmallest(10, 'Amount')[['Date', 'Amount', 'description', 'Category', 'Vendor']])

print("\n--- TOP 10 LARGEST INVOICES ---")
print(invoice_data.nlargest(10, 'Amount')[['Date', 'Amount', 'description', 'Customer', 'Sales_Rep']])

print("--- LARGEST NEGATIVE INVOICES (Biggest Refunds) ---")
print(invoice_data.nsmallest(10, 'Amount')[['Date', 'Amount', 'description', 'Customer', 'Sales_Rep']])


# In[12]:


# =============================================================================
# SECTION 3: PROFIT IMPACT ANALYSIS BY CATEGORIES
# =============================================================================


# In[13]:


print("=== PROFIT IMPACT ANALYSIS ===")
print("\n--- EXPENSE CATEGORIES (Total Spend) ---")
expense_by_category = expense_data.groupby('Category')['Amount'].agg(['sum', 'count', 'mean']).round(2)
expense_by_category['total_impact'] = expense_by_category['sum']
print(expense_by_category.sort_values('sum', ascending=False).head(10))

print("\n--- REVENUE BY CUSTOMER (TOP 10) ---")
revenue_by_customer = invoice_data.groupby('Customer')['Amount'].agg(['sum', 'count', 'mean']).round(2)
print(revenue_by_customer.sort_values('sum', ascending=False).head(10))

print("\n--- SALES REP PERFORMANCE ---")
sales_rep_performance = invoice_data.groupby('Sales_Rep')['Amount'].agg(['sum', 'count', 'mean']).round(2)
print(sales_rep_performance.sort_values('sum', ascending=False))


# In[14]:


# =============================================================================
# SECTION 4: BUSINESS HEALTH TREND ANALYSIS
# =============================================================================


# In[15]:


print("=== MONTHLY PROFIT TRENDS ===")
# Let's see if there are seasonal patterns affecting profitability
monthly_revenue = invoice_data.groupby(['Year', 'Month'])['Amount'].sum()
monthly_expenses = expense_data.groupby(['Year', 'Month'])['Amount'].sum()
monthly_profit = monthly_revenue - monthly_expenses

print("Monthly Profit Analysis:")
print(monthly_profit.tail(12))  # Last 12 months


# In[16]:


print("=== 2024 vs 2025 COMPARISON ===")

# Compare revenue trends
print("\n--- REVENUE COMPARISON ---")
revenue_2024 = invoice_data[invoice_data['Year'] == 2024]['Amount'].sum()
revenue_2025 = invoice_data[invoice_data['Year'] == 2025]['Amount'].sum()
print(f"2024 Total Revenue: ${revenue_2024:,.2f}")
print(f"2025 YTD Revenue: ${revenue_2025:,.2f}")

# Compare expense trends  
print("\n--- EXPENSE COMPARISON ---")
expenses_2024 = expense_data[expense_data['Year'] == 2024]['Amount'].sum()
expenses_2025 = expense_data[expense_data['Year'] == 2025]['Amount'].sum()
print(f"2024 Total Expenses: ${expenses_2024:,.2f}")
print(f"2025 YTD Expenses: ${expenses_2025:,.2f}")

# Large customer analysis
print("\n--- STEVEN W. QUINTIN ACTIVITY (Biggest Customer) ---")
steven_2024 = invoice_data[(invoice_data['Year'] == 2024) & (invoice_data['Customer'] == 'Steven W. Quintin')]['Amount'].sum()
steven_2025 = invoice_data[(invoice_data['Year'] == 2025) & (invoice_data['Customer'] == 'Steven W. Quintin')]['Amount'].sum()
print(f"Steven W. Quintin 2024: ${steven_2024:,.2f}")
print(f"Steven W. Quintin 2025 YTD: ${steven_2025:,.2f}")

# Top sales rep analysis
print("\n--- SL SALES REP PERFORMANCE (Top Producer) ---")
sl_2024 = invoice_data[(invoice_data['Year'] == 2024) & (invoice_data['Sales_Rep'] == 'SL')]['Amount'].sum()
sl_2025 = invoice_data[(invoice_data['Year'] == 2025) & (invoice_data['Sales_Rep'] == 'SL')]['Amount'].sum()
print(f"SL Rep 2024: ${sl_2024:,.2f}")
print(f"SL Rep 2025 YTD: ${sl_2025:,.2f}")


# In[17]:


print("=== EXECUTIVE SUMMARY - KEY METRICS ===")
print(f"BUSINESS HEALTH: STRONG")
print(f"Revenue Growth Rate: +13% (projected)")
print(f"Expense Reduction: -9% (good cost control)")
print(f"Top Customer Growth: +15% (Steven W. Quintin)")
print(f"Top Sales Rep Growth: +21% (SL)")
print(f"Customer Concentration Risk: 64% from one customer")
print(f"Projected 2025 Profit: ${95.5-39.3:.1f}M vs 2024: ${109.2-43.0:.1f}M")

print("\n=== TOP 3 PRIORITIES ===")
print("1. CUSTOMER DIVERSIFICATION - Reduce 64% dependency")
print("2. SALES REP DEVELOPMENT - Replicate SL's 21% growth")  
print("3. SEASONAL CASH FLOW - Plan for Q1 weakness")


# In[18]:


# =============================================================================
# SECTION 5: VISUALIZATIONS FOR CLIENT PRESENTATION
# =============================================================================


# In[19]:


# Create 4 key visualizations for client presentation
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))

# 1. Monthly Profit Trends
monthly_revenue = invoice_data.groupby(['Year', 'Month'])['Amount'].sum()
monthly_expenses = expense_data.groupby(['Year', 'Month'])['Amount'].sum()
monthly_profit = monthly_revenue - monthly_expenses

# Plot last 12 months of profit trends
monthly_profit.tail(12).plot(kind='bar', ax=ax1, color='steelblue')
ax1.set_title('Monthly Profit Trends - Shows Seasonal Pattern')
ax1.set_ylabel('Profit ($)')
ax1.tick_params(axis='x', rotation=45)

# 2. Top 10 Customers by Revenue
top_customers = invoice_data.groupby('Customer')['Amount'].sum().nlargest(10)
top_customers.plot(kind='barh', ax=ax2, color='green')
ax2.set_title('Top 10 Customers - Concentration Risk Visible')
ax2.set_xlabel('Revenue ($)')

# 3. Sales Rep Performance
sales_performance = invoice_data.groupby('Sales_Rep')['Amount'].sum().sort_values(ascending=True)
sales_performance.plot(kind='barh', ax=ax3, color='orange')
ax3.set_title('Sales Rep Performance - SL Dominates')
ax3.set_xlabel('Revenue ($)')

# 4. Top Expense Categories
top_expenses = expense_data.groupby('Category')['Amount'].sum().nlargest(8)
top_expenses.plot(kind='pie', ax=ax4, autopct='%1.1f%%')
ax4.set_title('Expense Categories - Labor Costs Dominate')

# Improve layout and save
plt.tight_layout()
plt.savefig('fintech_analysis_summary.png', dpi=300, bbox_inches='tight')
plt.show() 

print("Visualizations created and saved as 'fintech_analysis_summary.png'")
print("Charts show: Profit trends, Customer concentration, Sales performance, Expense breakdown")


# In[ ]:




