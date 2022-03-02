#include important module
import streamlit as st
import pandas as pd
import plotly.express as px

DATA_FILE = 'output/output.csv'

st.title("FINAL ANALYSIS OF RFM CHURN DETECTION")

@st.cache(persist=False)
def load_data():
    data = pd.read_csv(DATA_FILE)
    data = data[(data['MONETARY'] > 0) & (data['RECENCY'] <=31) & (data['FREQUENCY'] <= 100)]
    return data

data = load_data()
category = data['CATEGORY'].unique()

#build app filters
column = st.sidebar.multiselect('category', category)
recency = st.sidebar.number_input('Smaller Than Recency', 0, 360, 360)
frequency= st.sidebar.number_input('Smaller Than Frequency', 0, 100, 100)
monetary = st.sidebar.number_input('Smaller Than Monetary', 0, 100000, 100000)

data = data[(data['RECENCY']<=recency) & (data['FREQUENCY']<=frequency) & (data['MONETARY']<=monetary)]

#manage the multiple field filter
if column == []:
    data = data
else:
    data = data[data['CATEGORY'].isin(column)]
data

st.subheader('RFM Scatter Plot')
#scatter plot
fig_scatter = px.scatter(data, x="RECENCY", y="FREQUENCY", color="CATEGORY",
                 size='MONETARY', hover_data=['RN', 'FN', 'MN'])

st.plotly_chart(fig_scatter)

#show distribution of values
#recency
fig_r = px.histogram(data, x="RECENCY", y="PHONE", marginal="box",
                   hover_data=data.columns, title='Recency Plot')
st.plotly_chart(fig_r)

#frequency
fig_f = px.histogram(data, x="FREQUENCY", y="PHONE", marginal="box",
                   hover_data=data.columns, title='Frequency Plot')
st.plotly_chart(fig_f)

#monetary
fig_m = px.histogram(data, x="MONETARY", y="PHONE", marginal="box",
                   hover_data=data.columns, title='Monetary Plot')
st.plotly_chart(fig_m)
