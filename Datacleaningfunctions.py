# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 08:35:33 2025

@author: BelindaNyakake
"""
import pandas as pd
def Clean(data):
    data.drop(columns=['id'], inplace = True)
    data['name_of_borrower']=data['name_of_borrower'].str.title()
    data['email_of_borrower'].fillna('No_Email', inplace=True)
    data['highest_education_level']=data['highest_education_level'].fillna('Not_Available')
    data['employment_status']=data['employment_status'].str.replace('Self-employed','Self_employed')
    data['Gender']= data['Gender'].str.replace(' ','')
    data['Loan_amount']=data['Loan_amount'].str.replace(' ','')
    data['Loan_amount']=data['Loan_amount'].str.replace(',','')
    data['Loan_amount']= pd.to_numeric(data['Loan_amount'])
    data['Loan_amount']=data['Loan_amount'].astype(int)
    data['Date_of_loan_issue']= pd.to_datetime(data['Date_of_loan_issue'])
    data['Date_of_repayments_commencement']=pd.to_datetime(data['Date_of_repayments_commencement'])
    data['Tenure_of_loan']=round(pd.to_numeric(data['Tenure_of_loan'].str.replace('days',''))/30,0)
    data['Tenure_of_loan'].astype('Int64')
    data['Interest_rate']=data['Interest_rate']/100
    data['Loan_type']=data['Loan_type'].str.replace(' ','')
    data['Loan_term_value']='Months'
    data['Location_of_borrower']=data['Location_of_borrower'].str.title()
    data['Expected_monthly_installment']= pd.to_numeric(data['Expected_monthly_installment'].str.replace(',','')).astype(int)
    data.drop(columns=['created'],inplace=True)
    data['Length_of_time_running']=data['Date_of_loan_issue']-pd.to_datetime(data['Length_of_time_running'], format='mixed',errors='coerce')
    data['Length_of_time_running']=(data['Length_of_time_running'].dt.days//365).astype('Int64')
    data['Person_with_disabilities']=data['Person_with_disabilities'].str.replace('false','No').str.replace(' ','')
    data['Activity']=data['Loan_purpose']+data['Line_of_business']
    sector_keywords={
    'Enterprise': ['business'],
    'Agriculture': ['agri','GROWING'],
    'Transport' : ['BODA BODA']
}
    data['Sector']='none'
    for belz, harris in data.iterrows():
        andrew=harris['Activity']
        for a,b in sector_keywords.items():
            for bright in b:
                if bright in andrew:
                    data.at[belz, 'Sector']=a
                    break
    district_keywords={
        'Kabale': ['kabale'],
}
    data['District']='none'
    
    for index, row in data.iterrows():
        location=row['Location_of_borrower'].lower()
        for district,loc in district_keywords.items():
            for a in loc:
                if a in location:
                    data.at[index, 'District']=a
                    break
    region_keywords={
        'South Western': ['kabale','rukiga','ntungamo'],
        'Western': ['kasese']  
    }
    data['Region']='none'
    
    for index, row in data.iterrows():
        district=row['District'].lower()
        for region,loc in region_keywords.items():
            for a in loc:
                if a in district:
                    data.at[index, 'Region']=region
                    break
    return data