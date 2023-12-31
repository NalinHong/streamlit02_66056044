import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#
# # --- 01
# # https://docs.streamlit.io/library/api-reference/write-magic
# st.markdown('สวัสดี! **Streamlit**')
# st.write('จากโค้ด', '`st.markdown("สวัสดี!")`')
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40],
# }))
# st.divider()

# --- 02
# binom_dist = np.random.binomial(1, .5, 100)
# st.write(np.mean(binom_dist))

# --- 03
# binom_dist = np.random.binomial(1, .5, 1000)
# list_of_means = []
# for i in range(0, 1000):
#     list_of_means.append(
#         np.random.choice(binom_dist, 100, replace=True).mean())
#
# fig1, ax1 = plt.subplots()
# ax1 = plt.hist(list_of_means)
# st.pyplot(fig1)
#
# --- 04
# fig2, ax2 = plt.subplots()
# ax2 = plt.hist([1, 1, 1, 1])
# st.pyplot(fig2)

# --- 05
# perc_heads = st.number_input(label='Chance of Coins Landing on Heads',
#                              min_value=0.0, max_value=1.0,
#                              value=.5)
# graph_title = 'Histogram of a thousand coin flips'
# # 4. https://docs.streamlit.io/library/api-reference/widgets
# # 5. เพ่ิม header, subheader ด้วย
# # An Inllustration of Central Limit Theorem
# # This app simulates a thousand coin flips using the chance of heads input below,
# # and then samples with replacement from that population and plots the histogram of the
# # means of the samples in order to illustrate the central limit theorem!
# # https://docs.streamlit.io/library/api-reference/text
#
# binom_dist = np.random.binomial(1, .5, 1000)
# # 1. where to replace `perc_heads`?
# list_of_means = []
# for i in range(0, 1000):
#     list_of_means.append(
#         np.random.choice(binom_dist, 100, replace=True).mean())
#
# fig1, ax1 = plt.subplots()
# ax1 = plt.hist(list_of_means)
# ax1 = plt.title('ป้อนค่าอะไรลงไปดี')
# # 2. how to setup limit of x-axis value to 0.0 - 1.0?
# # 3. how to setup more bins, like 20 or 40?
# st.pyplot(fig1)
# all#=ctrl+/

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.markdown('สวัสดี! **Streamlit**')
st.title('Layout and decoration')
st.write('''ลองทำSan Francisco Dataset กัน''')

trees_df = pd.read_csv('trees.csv')
df_dbh_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns=['tree_count']

col1, col2, col3 =st.columns(3)
with col1:
    st.line_chart(df_dbh_grouped)
with col2:
    st.bar_chart(df_dbh_grouped)
with col3:
    st.area_chart(df_dbh_grouped)

trees_df = pd.read_csv('trees.csv')
df_dbh_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns=['tree_count']
st.line_chart(df_dbh_grouped)
st.caption('กราฟ แสดงจำนวนต้นไม้ จัดกลุ่มตามเส้นผ่านศนย์กลาง')
st.title('แปลผล')
st.write('''ส่วนใหญ่ของต้นไม้ใน SF มีเส้นผ่าศูนย์กลาง 3''')

trees_df =trees_df.dropna(subset=['longitude','latitude'])
trees_df= trees_df.sample(n=1000,replace=True)
st.map(trees_df)