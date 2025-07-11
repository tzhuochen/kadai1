#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import streamlit as st
import plotly.express as px


# In[13]:


merged_df = pd.read_csv("merged.csv")


# In[14]:


st.title("レストランサーチ")

price_limit = st.slider("最低食費価格の上限",min_value=1499,max_value=4750,step=200,value=6000)
score_limit = st.slider("人気スコアの下限",min_value=0.0, max_value=113.0, step=2.0, value=5.0)


# In[16]:


filtered_df = merged_df[
    (merged_df['Avg Price (JPY)']<= price_limit) &
    (merged_df['Recommendation Score']>= score_limit)
]


# In[18]:


fig = px.scatter(
    filtered_df,
    x='Recommendation Score',
    y='Avg Price (JPY)',
    hover_data=['Store Name','Genre/Area','Rating','Review Count'],
)

st.plotly_chart(fig)


# In[19]:


selected_restrant = st.selectbox('気になるレストランを選んで詳細を確認',filtered_df['Store Name'])

if selected_restrant:
    url = filtered_df[filtered_df['Store Name'] == selected_restrant]['URL'].values[0]
    st.markdown(f"[{selected_restrant}のペ-ジ八移動]({url})",unsafe_allow_html=True)


# In[20]:


sort_key = st.selectbox(
    "ランキング基準を選んでください",
    ("Rating", "Recommendation Score","Review Count","Avg Price (JPY)")
)
ascending = True if sort_key == "Avg Price (JPY)" else False


# In[21]:


st.subheader(f"{sort_key} によるレストランランキング(上位10件")
ranking_df = filtered_df.sort_values(by=sort_key, ascending=ascending).head(10)
# 必要な列だけ表示
st.dataframe(ranking_df[["Store Name","Avg Price (JPY)","Recommendation Score","Rating","Review Count","Genre/Area"]])


# In[22]:


print(merged_df.columns.tolist())


# In[ ]:




