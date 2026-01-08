import streamlit as st
import random
import math

st.title("2進数を10進数に変換クイズ")

#参考https://ex-ture.com/blog/2024/07/23/streamlit_guide/
if 'count' not in st.session_state:
    #st.write('カウント変数を設定')
    st.session_state['count'] = 0
if 'nowAns' not in st.session_state:
    st.session_state['nowAns'] = 0 #st.write('初回の答え変数を設定')

with st.form("my_form", clear_on_submit=False):
#問題作成(乱数)
    numsList = list()
    numStr = "" #writeの改行なしがわからなかったので代案
    setpow = [1,2,4,8]
    
    st.session_state['prevAns'] = st.session_state['nowAns']
    st.session_state['nowAns'] = 0 
    for set in range(4):
        numsList.append(random.randint(0,1))
        st.session_state['nowAns'] +=  (numsList[set] * setpow[3-set])
        numStr += str(numsList[-1])
    #問題文出力
    st.write(numStr)
    
    #回答スキャン
    playAns = st.text_input("10進数で答えを入力")
    submitted = st.form_submit_button("回答する")    

    #ボタン押して合否判定エリア
    if submitted:
        st.write('前回の答え',st.session_state.prevAns)
        st.write('あなたの答え',playAns)
        if playAns == str(st.session_state.prevAns):
            st.write('正解!')
            st.session_state.count += 1
            # st.session_state['count'] += 1 でもOK
        else :
            st.write('不正解')
        
    st.write('勝利記録 = ', st.session_state.count) 
