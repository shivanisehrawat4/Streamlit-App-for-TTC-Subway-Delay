import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="TTC Subway Dashboard", page_icon=":bar_chart:", layout="wide")

header = st.container()
# dataset = st.beta_container()

# st.markdown(
#     """
#     <style>
#     .main {
#     background-color: #F5F5F5;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

@st.cache
def get_data(filename):
	ttc_data = pd.read_csv(filename)

	return ttc_data


def show_explore():
    st.title('Welcome to my TTC Subway Delay Project!')
#     st.text('In this project I look into the ...')
    
    st.header('Dataset')
    st.text('I found this dataset on https://open.toronto.ca/dataset/ttc-subway-delay-data/')
    
    ttc_data = get_data('data/ttc_subway_delay_data_2014_to_2022.csv')
    st.write(ttc_data)
    
    st.subheader('Longest delay times by reason for delay')
    most_delayed_subways = ttc_data.sort_values(by='Min_Delay', ascending=False).head(10)
    st.bar_chart(x = 'Min_Delay', 
                y = 'CODE_DESCRIPTION', 
                data = most_delayed_subways)
    
    st.subheader('Station with longest delay times')
    fig1 = plt.figure(figsize=(12, 8))
    sns.barplot(x = 'Min_Delay',
            y = 'Station', 
            hue = 'Station',
            data = most_delayed_subways)
    plt.title('Longest Delay Times by Station')
    plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.5)
    st.pyplot(fig1)

#     fig2 = sns.pairplot(most_delayed_subways)
#     plt.figure(figsize=(6, 6))
#     st.pyplot(fig2)
    st.subheader('Percentage of subway running on different days of the week')
    fig2 = plt.figure(figsize=(6, 6))
    ttc_data['DayOfWeek'].value_counts().plot.pie(autopct='%.0f%%')
    st.pyplot(fig2)

    st.subheader('Delay mainly happened on bound West (W)')
    fig3 = plt.figure(figsize=(6, 6))
    ttc_data['Bound'].value_counts().plot.pie(autopct='%.0f%%')
    st.pyplot(fig3)

