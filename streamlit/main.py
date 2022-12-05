import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Styling
st.set_page_config(page_title='UE3 Data Visualization')
hide_menu_style = """
        <style>
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


df = pd.read_csv('data/bank.csv')

# Control sidebar
st.sidebar.image("images/logo-univ-2.png", use_column_width=True)

add_selectbox = st.sidebar.selectbox(
    "Please select a option for the distribution chart",
    options=df.columns
)

# add_selectbox_2 = st.sidebar.selectbox(
#     "Please select x for the bubble chart",
#     options=df.columns
# )

# add_selectbox_3 = st.sidebar.selectbox(
#     "Please select y option for the bar chart",
#     options=df.columns
# )

# add_selectbox_4 = st.sidebar.selectbox(
#     "Please select size option for the bar chart",
#     options=df.columns
# )

# add_selectbox_5 = st.sidebar.selectbox(
#     "Please select color option for the bar chart",
#     options=df.columns
# )


max_age = df['age'].max()
min_age = df['age'].min()

age_choose = st.sidebar.slider('Choose age range', min_age, max_age, (min_age, max_age))
df = df[(df['age'] <= int(age_choose[1])) & (df['age'] >= int(age_choose[0]))]

max_balance = df['balance'].max()
min_balance = df['balance'].min()

balance_choose = st.sidebar.slider('Choose balance range', min_balance, max_balance, (min_balance, max_balance))
df = df[(df['balance'] <= balance_choose[1]) & (df['balance'] >= balance_choose[0])]

max_duration = df['duration'].max()
min_duration = df['duration'].min()

duration_choose = st.sidebar.slider('Choose duration range', min_duration, max_duration, (min_duration, max_duration))
df = df[(df['duration'] <= duration_choose[1]) & (df['duration'] >= duration_choose[0])]

# st.sidebar.write('Choose type of housing')
housing_choose=st.sidebar.radio('Choose type of housing',('All', 'Yes', 'No'))

if housing_choose == 'All':
    pass
elif housing_choose == 'Yes':
    df = df[df['housing'] != 'no']
elif housing_choose == 'No':
    df = df[df['housing'] != 'yes']

loan_choose=st.sidebar.radio('Choose type of loan',('All', 'Yes', 'No'))

if loan_choose == 'All':
    pass
elif loan_choose == 'Yes':
    df = df[df['loan'] != 'no']
elif loan_choose == 'No':
    df = df[df['loan'] != 'yes']

st.write('# Data visualization for bank marketing dataset')

# Bar chart
job = df[add_selectbox]
fig = px.bar(job.value_counts(), 
            title=f'Distribution of {add_selectbox}')
st.plotly_chart(fig, use_container_width=True)


# Bubble chart
# df[df['balance']>0]
fig_2 = px.scatter(df, x="age", y="balance",
	               size="duration", color="job",
                   hover_name="job", log_x=True, size_max=60)

st.plotly_chart(fig_2, use_container_width=True)


#job and deposit
j_df = pd.DataFrame()

j_df['yes'] = df[df['deposit'] == 'yes']['job'].value_counts()
j_df['no'] = df[df['deposit'] == 'no']['job'].value_counts()

fig_job_deposit = px.bar(j_df,
                        title="Term deposit by job", 
                        barmode='group')
st.plotly_chart(fig_job_deposit, use_container_width=True)


col1, col2 = st.columns(2)


#marital and deposit
mari_df = pd.DataFrame()

mari_df['yes'] = df[df['deposit'] == 'yes']['marital'].value_counts()
mari_df['no'] = df[df['deposit'] == 'no']['marital'].value_counts()

fig_mari_deposit = px.bar(mari_df,
                        title="Term deposit by marital", 
                        barmode='group')
st.plotly_chart(fig_mari_deposit, use_container_width=True)


col1, col2 = st.columns(2)

# Pie chart
# st.dataframe(df['deposit'].value_counts())    
with col1:
    term_subscribe_fig = px.pie(df['deposit'].value_counts(),
                                title="Term deposit", 
                                values='deposit',
                                names=df['deposit'].value_counts().index)
    st.plotly_chart(term_subscribe_fig, use_container_width=True)

with col2:
    # st.dataframe(df[['education', 'deposit']].groupby('education').value_counts().reset_index())
    sub_groupby = df[['education', 'deposit']].groupby('education').value_counts().reset_index()
    # st.write(type(sub_groupby))
    # Bar chart group by
    term_subscribe_by_fig = px.bar(sub_groupby,
                                title="Term deposit by education", 
                                x=sub_groupby['education'], 
                                y=sub_groupby[0], 
                                color=sub_groupby['deposit'],
                                barmode='group')
    st.plotly_chart(term_subscribe_by_fig, use_container_width=True)


# distribute chart
fig_3 = px.scatter(df, x="balance", y="duration", color="marital", 
                 marginal_x="box", marginal_y="violin")
fig_3.update_layout(
    title={
         'text': "Purpose Of Low Amount Of Balance."},
    xaxis_title="Duration",
    yaxis_title=" Balance",
    legend_title="Marital Status"
)

st.plotly_chart(fig_3, use_container_width=True)




suscribed_df = df.loc[df["deposit"] == "yes"]

occupations = df["job"].unique().tolist()

# Get the balances by jobs
management = suscribed_df["age"].loc[suscribed_df["job"] == "management"].values
technician = suscribed_df["age"].loc[suscribed_df["job"] == "technician"].values
services = suscribed_df["age"].loc[suscribed_df["job"] == "services"].values
retired = suscribed_df["age"].loc[suscribed_df["job"] == "retired"].values
blue_collar = suscribed_df["age"].loc[suscribed_df["job"] == "blue-collar"].values
unemployed = suscribed_df["age"].loc[suscribed_df["job"] == "unemployed"].values
entrepreneur = suscribed_df["age"].loc[suscribed_df["job"] == "entrepreneur"].values
housemaid = suscribed_df["age"].loc[suscribed_df["job"] == "housemaid"].values
self_employed = suscribed_df["age"].loc[suscribed_df["job"] == "self-employed"].values
student = suscribed_df["age"].loc[suscribed_df["job"] == "student"].values


ages = [management, technician, services, retired, blue_collar, unemployed, 
         entrepreneur, housemaid, self_employed, student]

# colors = ['rgba(93, 164, 214, 1)', 'rgba(255, 144, 14, 1)',
#           'rgba(44, 160, 101, 1)', 'rgba(255, 65, 54, 1)', 
#           'rgba(207, 114, 255, 1)', 'rgba(127, 96, 0, 1)',
#          'rgba(229, 126, 56, 1)', 'rgba(229, 56, 56, 1)',
#          'rgba(174, 229, 56, 1)', 'rgba(229, 56, 56, 1)']

traces = []

for xd, yd in zip(occupations, ages):
        traces.append(go.Box(
            y=yd,
            name=xd,
            boxpoints='all',
            # jitter=0.5,
            # whiskerwidth=0.2,
            # fillcolor=cls,
            marker=dict(
                size=3,
            ),
            # line=dict(width=1),
        ))

layout = go.Layout(
    title='Distribution of ages by job',
    yaxis=dict(
        autorange=True,
        showgrid=True,
        zeroline=True,
        dtick=5,
        # gridcolor='rgb(255, 255, 255)',
        # gridwidth=1,
        # zerolinecolor='rgb(255, 255, 255)',
        # zerolinewidth=2,
    ),
    # margin=dict(
    #     l=40,
    #     r=30,
    #     b=80,
    #     t=100,
    # ),
    # showlegend=False
)

fig_4 = go.Figure(data=traces, layout=layout)

st.plotly_chart(fig_4, use_container_width=True)