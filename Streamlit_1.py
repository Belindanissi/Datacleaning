# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 07:57:04 2025

@author: BelindaNyakake
"""
import streamlit as st
import pandas as pd
import numpy as np
import Datacleaningfunctions as fx

st.subheader('My data cleaning app')

file = st.file_uploader("Select a file", type="xlsx")
if file is not None:

    data = pd.read_excel(file)
    
    df = fx.Clean(data)
    st.write(df.shape)
    st.write(df.head())
    
    col1, col2, col3 = st.columns(3)
    with col1:
        #Show loan amount
        amount = df['Loan_amount'].sum()
        st.metric('The loan Amount is:', amount)
    
    with col2:
        #Show number of loans
        number = df['Borrower_ID'].count()
        st.metric('The Number of Loans is:',number)
    
    with col3:
        mask = df['Age']<=35
        youths = df[mask]['Borrower_ID'].count()
        st.metric('The Number of Youths is:', youths)
    
    with col1:
        mask = df['Gender']== 'Female'
        women = df[mask]['Borrower_ID'].count()
        st.metric('The Number of Women is:', women)
    
    with col2:
        mask = (df['Gender']=='Female') & (df['Age']<=35)
        youngwomen = df[mask]['Borrower_ID'].count()
        st.metric('The Number of Young Women is:', youngwomen)
    
    with col3:
        #Show interest rate
        rate = round(df['Interest_rate'].mean(),2)
        st.metric('Average Interest Rate:', rate)
        
    st.download_button(
        label= 'Click to Download data',
        data= df.to_csv(index=False),
        file_name = 'Clean_data.csv')