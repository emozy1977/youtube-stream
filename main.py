import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.01)
'Done!'



left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')

# text = st.text_input('あなたの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味は', text, 'です。'
# 'コンディション：', condition



# 'あなたの好きな数字は、',option,'です。'

# if st.checkbox('Show Image'):
#     img=Image.open('sample.png')
#     st.image(img, caption='Pink Panther', use_column_width=True)



# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import pandas as pd
# import numpy as np
# ```


# """